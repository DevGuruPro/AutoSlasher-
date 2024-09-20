import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
import numpy as np
import matplotlib.animation as animation

# Function to resample the traversal path
def resample_path(traversal_path, spacing=0.75):
    """
    Resample a traversal path to have points at fixed intervals.

    Parameters:
    - traversal_path: List of (x, y) tuples representing the original path.
    - spacing: Desired distance between consecutive points.

    Returns:
    - resampled_path: List of (x, y) tuples with fixed spacing.
    """
    if len(traversal_path) < 2:
        return traversal_path  # Not enough points to resample

    line = LineString(traversal_path)
    length = line.length

    # Calculate number of points based on desired spacing
    num_points = int(length // spacing)

    # Handle case where spacing doesn't divide length evenly
    if num_points == 0:
        return traversal_path

    # Generate equally spaced points along the line
    distances = np.linspace(0, length, num_points + 1)
    resampled_path = [line.interpolate(distance).coords[0] for distance in distances]

    return resampled_path

# Class to handle the simulation
class PolygonDrawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 8))

        # Initialize plot limits centered at starting position
        self.machine_pos = np.array([0.0, 0.0])  # Starting at (0, 0)
        self.view_range = 100  # Half-width and half-height of the visible area
        self.ax.set_xlim(self.machine_pos[0] - self.view_range, self.machine_pos[0] + self.view_range)
        self.ax.set_ylim(self.machine_pos[1] - self.view_range, self.machine_pos[1] + self.view_range)
        self.ax.set_aspect('equal')

        # Initialize modes
        self.mode = 'boundary_drawing'  # Modes: 'boundary_drawing', 'free_drive', 'obstacle_drawing', 'infill', 'finished'
        self.boundary = []
        self.obstacles = []
        self.infill_lines = []
        self.current_obstacle_path = []
        self.current_line = []
        self.infill_line_objects = []  # To keep track of line objects for infill lines
        self.preview_line = None  # For the live preview line during infill drawing

        self.offset_boundary_path = None  # Store the offset boundary path
        self.offset_line = None  # Line object for the offset path

        # Machine simulation variables
        self.machine_speed_normal = 2.22  # 8 km/h in m/s
        self.machine_speed_fast = 8.33    # 30 km/h in m/s
        self.fast_mode = False            # Fast mode flag
        self.machine_direction = np.array([0.0, 0.0])  # Direction vector
        self.machine_path = [self.machine_pos.copy()]  # Record of positions
        self.update_interval = 100  # Update every 0.1 seconds (100 ms)

        # Key press states
        self.key_states = {'up': False, 'down': False, 'left': False, 'right': False, 'B': False}

        # Draw the crosshair at the center
        self.crosshair_lines = self.draw_crosshair()

        # Instructions
        self.ax.set_title("Boundary Drawing Mode.\nUse arrow keys to outline boundary.\nPress 'E' to end boundary drawing.\nHold 'B' to draw obstacles by driving.")

        # Speed readout text
        self.speed_text = self.ax.text(0.05, 0.95, '', transform=self.ax.transAxes, fontsize=12,
                                       verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

        # Connect events
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.fig.canvas.mpl_connect('key_release_event', self.on_key_release)
        # Connect mouse events for infill drawing
        self.fig.canvas.mpl_connect('button_press_event', self.on_mouse_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_mouse_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)  # New connection for mouse movement

        # Start the animation
        self.ani = animation.FuncAnimation(self.fig, self.update_machine_position,
                                           interval=self.update_interval, blit=False,
                                           cache_frame_data=False)  # Suppress UserWarning

    def draw_crosshair(self):
        x0, y0 = self.machine_pos
        size = 5  # Length of crosshair lines
        line1, = self.ax.plot([x0 - size, x0 + size], [y0, y0], 'k-', linewidth=1.5, zorder=5)
        line2, = self.ax.plot([x0, x0], [y0 - size, y0 + size], 'k-', linewidth=1.5, zorder=5)
        return [line1, line2]

    def on_key_press(self, event):
        if event.key == 'up':
            self.key_states['up'] = True
        elif event.key == 'down':
            self.key_states['down'] = True
        elif event.key == 'left':
            self.key_states['left'] = True
        elif event.key == 'right':
            self.key_states['right'] = True
        elif event.key == ' ':
            self.fast_mode = True
        elif event.key.lower() == 'b':
            self.key_states['B'] = True
            self.enter_obstacle_drawing()
        elif event.key == 'e':
            if self.mode == 'boundary_drawing':
                self.finish_boundary_drawing()
            elif self.mode == 'infill':
                # Remove the grid when done and proceed to traversal selection
                self.finish_infill_drawing()
            elif self.mode == 'free_drive':
                # Proceed to Infill Drawing Mode from Free Drive Mode
                self.enter_infill_mode()
            else:
                pass  # Do nothing in other modes
        else:
            pass  # Other keys can be handled if needed

    def on_key_release(self, event):
        if event.key == 'up':
            self.key_states['up'] = False
        elif event.key == 'down':
            self.key_states['down'] = False
        elif event.key == 'left':
            self.key_states['left'] = False
        elif event.key == 'right':
            self.key_states['right'] = False
        elif event.key == ' ':
            self.fast_mode = False
        elif event.key.lower() == 'b':
            self.key_states['B'] = False
            if self.mode == 'obstacle_drawing':
                self.finish_obstacle_drawing()
        else:
            pass  # Other keys can be handled if needed

    def enter_obstacle_drawing(self):
        if self.mode not in ['free_drive', 'boundary_drawing']:
            print("Cannot enter obstacle drawing mode from current mode.")
            return
        self.mode = 'obstacle_drawing'
        self.current_obstacle_path = [tuple(self.machine_pos)]
        self.ax.set_title("Obstacle Drawing Mode: Drive the machine to outline the obstacle.\nRelease 'B' to finalize the obstacle.")
        self.fig.canvas.draw()

    def finish_obstacle_drawing(self):
        if len(self.current_obstacle_path) < 3:
            print("Obstacle must have at least 3 points. Obstacle not added.")
        else:
            # Close the obstacle path
            self.current_obstacle_path.append(self.current_obstacle_path[0])
            # Create a polygon
            obstacle_polygon = Polygon(self.current_obstacle_path)
            if not obstacle_polygon.is_valid:
                print("Invalid obstacle polygon. Obstacle not added.")
            else:
                self.obstacles.append(self.current_obstacle_path.copy())
                # Plot the obstacle
                x, y = zip(*self.current_obstacle_path)
                self.ax.plot(x, y, 'r-', linewidth=2, label='Obstacle')
                # Update the legend without duplicates
                handles, labels = self.ax.get_legend_handles_labels()
                unique = dict(zip(labels, handles))
                self.ax.legend(unique.values(), unique.keys())
        # Reset
        self.current_obstacle_path = []
        self.mode = 'free_drive'
        self.ax.set_title("Free Drive Mode.\nHold 'B' to draw obstacles by driving.\nPress 'E' to proceed to Infill Drawing.")
        self.fig.canvas.draw()

    def finish_boundary_drawing(self):
        self.mode = 'free_drive'
        # Close the boundary by adding the starting point to the end
        if not np.array_equal(self.machine_path[-1], self.machine_path[0]):
            self.machine_path.append(self.machine_path[0])

        self.boundary = [tuple(pos) for pos in self.machine_path]

        self.ax.set_title("Free Drive Mode.\nHold 'B' to draw obstacles by driving.\nPress 'E' to proceed to Infill Drawing.")

        self.fig.canvas.draw()

    def update_machine_position(self, frame):
        if self.mode not in ['boundary_drawing', 'free_drive', 'obstacle_drawing', 'infill']:
            return

        # Update direction based on key states
        dx = dy = 0.0
        if self.key_states['up']:
            dy += 1.0
        if self.key_states['down']:
            dy -= 1.0
        if self.key_states['left']:
            dx -= 1.0
        if self.key_states['right']:
            dx += 1.0

        direction = np.array([dx, dy])
        if np.linalg.norm(direction) > 0:
            direction = direction / np.linalg.norm(direction)
        else:
            direction = np.array([0.0, 0.0])

        # Determine current speed
        current_speed = self.machine_speed_fast if self.fast_mode else self.machine_speed_normal

        # Move the machine
        dt = self.update_interval / 1000.0  # Convert ms to seconds
        distance = current_speed * dt
        movement = direction * distance
        new_pos = self.machine_pos + movement

        # Update position
        self.machine_pos = new_pos

        # Update plot limits to simulate panning (only if not in infill mode)
        if self.mode != 'infill':
            self.ax.set_xlim(self.machine_pos[0] - self.view_range, self.machine_pos[0] + self.view_range)
            self.ax.set_ylim(self.machine_pos[1] - self.view_range, self.machine_pos[1] + self.view_range)

        # Update path
        if self.mode == 'boundary_drawing':
            self.machine_path.append(self.machine_pos.copy())
            # Update the boundary path line
            path_x, path_y = zip(*self.machine_path)
            if hasattr(self, 'path_line'):
                self.path_line.set_data(path_x, path_y)
            else:
                self.path_line, = self.ax.plot(path_x, path_y, 'b-', label='Boundary', zorder=1)
        elif self.mode == 'obstacle_drawing':
            self.current_obstacle_path.append(tuple(self.machine_pos))
            # Update the obstacle path line (dashed for ongoing drawing)
            path_x, path_y = zip(*self.current_obstacle_path)
            if hasattr(self, 'current_obstacle_line'):
                self.current_obstacle_line.set_data(path_x, path_y)
            else:
                self.current_obstacle_line, = self.ax.plot(path_x, path_y, 'r--', linewidth=1.5, zorder=2)

        # Redraw crosshair at the center (only if not in infill mode)
        if self.mode != 'infill':
            self.update_crosshair()

        # Update speed readout
        self.speed_text.set_text(f"Speed: {current_speed * 3.6:.2f} km/h")

        self.fig.canvas.draw_idle()

    def update_crosshair(self):
        x0, y0 = self.machine_pos
        size = 5  # Length of crosshair lines
        self.crosshair_lines[0].set_data([x0 - size, x0 + size], [y0, y0])
        self.crosshair_lines[1].set_data([x0, x0], [y0 - size, y0 + size])

    def enter_infill_mode(self):
        self.mode = 'infill'
        self.calculate_and_display_offset_path()
        self.setup_grid()
        self.ax.set_title("Infill Drawing Mode.\nDraw infill lines with snapping to grid.\nLeft-click to add points, double-click to finish each line.\nPress 'E' when done to proceed.")

        # Hide the crosshair
        for line in self.crosshair_lines:
            line.set_visible(False)

        # Zoom the screen to fit the boundary better
        if self.boundary:
            boundary_poly = Polygon(self.boundary)
            minx, miny, maxx, maxy = boundary_poly.bounds
            padding = 10  # Adjust padding as needed
            self.ax.set_xlim(minx - padding, maxx + padding)
            self.ax.set_ylim(miny - padding, maxy + padding)

        # Initialize the preview line
        self.preview_line = None

        self.fig.canvas.draw()

    def on_mouse_press(self, event):
        if self.mode != 'infill':
            return
        if event.inaxes != self.ax:
            return
        if event.button == 1:  # Left mouse button
            self.add_infill_point(event)

    def on_mouse_release(self, event):
        if self.mode != 'infill':
            return
        if event.inaxes != self.ax:
            return
        # Double-click to finalize the current infill line
        if event.dblclick:
            self.finish_infill_line()

    def on_mouse_move(self, event):
        if self.mode != 'infill':
            return
        if event.inaxes != self.ax:
            return
        if not self.current_line:
            return  # No starting point yet

        ix, iy = event.xdata, event.ydata
        if self.snap:
            ix, iy = self.snap_to_grid(ix, iy)

        last_x, last_y = self.current_line[-1]

        # Remove the previous preview line if it exists
        if self.preview_line:
            self.preview_line.remove()

        # Draw a new preview line
        self.preview_line, = self.ax.plot([last_x, ix], [last_y, iy], 'm--', linewidth=1.0, zorder=3)

        self.fig.canvas.draw_idle()

    def add_infill_point(self, event):
        ix, iy = event.xdata, event.ydata
        if self.snap:
            ix, iy = self.snap_to_grid(ix, iy)
        if self.current_line:
            x0, y0 = self.current_line[-1]
            self.current_line.append((ix, iy))
            # Draw the infill line segment
            line_obj, = self.ax.plot([x0, ix], [y0, iy], 'm-', linewidth=1.5)
            self.infill_line_objects.append(line_obj)
            # Remove the preview line as it's now a finalized segment
            if self.preview_line:
                self.preview_line.remove()
                self.preview_line = None
        else:
            self.current_line.append((ix, iy))
            # Plot the first point
            point_obj, = self.ax.plot(ix, iy, 'mo', markersize=5)
            self.infill_line_objects.append(point_obj)
        self.fig.canvas.draw()

    def finish_infill_line(self):
        if self.current_line:
            line = LineString(self.current_line)
            if self.is_line_valid(line):
                self.infill_lines.append(line)
                print("Infill line accepted.")
            else:
                print("Infill line is invalid and will not be added.")
                # Remove the invalid line from the plot
                for obj in self.infill_line_objects:
                    obj.remove()
            self.current_line = []
            self.infill_line_objects = []
            # Remove the preview line if it exists
            if self.preview_line:
                self.preview_line.remove()
                self.preview_line = None
        self.fig.canvas.draw()

    def finish_infill_drawing(self):
        # Finalize any remaining infill lines
        if self.current_line:
            self.finish_infill_line()
        self.clear_grid()
        self.mode = 'finished'  # New mode to indicate completion
        self.ax.set_title("Infill Drawing Completed.\nClosing the plot and proceeding to traversal selection.")
        self.fig.canvas.draw()
        plt.close(self.fig)  # Close the plot to proceed to traversal selection

    def is_line_valid(self, line):
        # Create the boundary polygon and obstacle polygons
        boundary_poly = Polygon(self.boundary)
        obstacles_poly = [Polygon(obs) for obs in self.obstacles]

        # Check if line is within or on the boundary
        if not boundary_poly.buffer(1e-8).covers(line):
            return False

        # Check if line intersects any obstacles
        for obs in obstacles_poly:
            if line.intersects(obs.buffer(1e-8)):
                return False
        return True

    def setup_grid(self):
        # Calculate grid spacing based on the boundary size
        boundary_poly = Polygon(self.boundary)
        minx, miny, maxx, maxy = boundary_poly.bounds
        width = maxx - minx
        height = maxy - miny

        # Set grid spacing (updated to 0.75)
        self.grid_spacing = 0.75  # Adjust this value as needed

        # Generate grid lines within the boundary bounds
        self.grid_x = np.arange(minx, maxx + self.grid_spacing, self.grid_spacing)
        self.grid_y = np.arange(miny, maxy + self.grid_spacing, self.grid_spacing)

        # Draw grid lines
        self.grid_lines = []
        for x in self.grid_x:
            line, = self.ax.plot([x, x], [miny, maxy], color='lightgray', linestyle='--', linewidth=0.5, zorder=0)
            self.grid_lines.append(line)
        for y in self.grid_y:
            line, = self.ax.plot([minx, maxx], [y, y], color='lightgray', linestyle='--', linewidth=0.5, zorder=0)
            self.grid_lines.append(line)

        # Enable snapping
        self.snap = True

        self.fig.canvas.draw()

    def clear_grid(self):
        # Remove grid lines
        for line in self.grid_lines:
            line.remove()
        self.grid_lines = []
        self.snap = False
        self.fig.canvas.draw()

    def snap_to_grid(self, x, y):
        # Snap x and y to the nearest grid point
        idx = (np.abs(self.grid_x - x)).argmin()
        idy = (np.abs(self.grid_y - y)).argmin()
        snapped_x = self.grid_x[idx]
        snapped_y = self.grid_y[idy]
        return snapped_x, snapped_y

    def calculate_and_display_offset_path(self):
        try:
            # Set offset distance (updated to 0.75)
            offset_distance = 0.75
            boundary_poly = Polygon(self.boundary)
            obstacles_poly = [Polygon(obs) for obs in self.obstacles]

            # Subtract obstacles from boundary
            if obstacles_poly:
                obstacles_union = unary_union(obstacles_poly)
                boundary_with_holes = boundary_poly.difference(obstacles_union)
            else:
                boundary_with_holes = boundary_poly

            # Generate the offset path
            offset_polygon = boundary_with_holes.buffer(-offset_distance, join_style=2)
            if offset_polygon.is_empty or not isinstance(offset_polygon, (Polygon, LineString)):
                print("Offset resulted in an empty or invalid geometry. Offset distance may be too large.")
                self.offset_boundary_path = None
                return

            # Get the exterior coordinates
            if isinstance(offset_polygon, Polygon):
                self.offset_boundary_path = list(offset_polygon.exterior.coords)
            elif isinstance(offset_polygon, LineString):
                self.offset_boundary_path = list(offset_polygon.coords)
            else:
                print("Offset resulted in unsupported geometry type.")
                self.offset_boundary_path = None
                return

            # Plot the offset path
            x, y = zip(*self.offset_boundary_path)
            self.offset_line, = self.ax.plot(x, y, 'g-', label='Offset Path')
            # Update the legend without duplicates
            handles, labels = self.ax.get_legend_handles_labels()
            unique = dict(zip(labels, handles))
            self.ax.legend(unique.values(), unique.keys())
            self.fig.canvas.draw()
        except Exception as e:
            print(f"Error in calculating offset path: {e}")
            self.offset_boundary_path = None

    def show(self):
        plt.axis('on')
        plt.grid(False)  # Turn off default grid
        plt.show()

# Function to animate the final path traversal
def animate_final_path(traversal_path, obstacles, title="Final Path Traversal Animation"):
    # Resample the traversal path for consistent speed
    spacing = 0.75  # Set to the same as offset distance
    resampled_traversal_path = resample_path(traversal_path, spacing=spacing)

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot obstacles
    for obs in obstacles:
        if len(obs) < 2:
            continue  # Skip invalid obstacles
        ox, oy = zip(*obs)
        ax.plot(ox + (ox[0],), oy + (oy[0],), 'r-', label='Obstacle')

    # Plot traversal path
    if resampled_traversal_path:
        x, y = zip(*resampled_traversal_path)
        ax.plot(x, y, 'b-', label='Traversal Path')

    # Set up the plot limits
    all_x = [p[0] for p in resampled_traversal_path]
    all_y = [p[1] for p in resampled_traversal_path]
    ax.set_xlim(min(all_x) - 10, max(all_x) + 10)
    ax.set_ylim(min(all_y) - 10, max(all_y) + 10)
    ax.set_aspect('equal', adjustable='box')

    # Initialize the machine marker and traversed path line
    machine_marker, = ax.plot([], [], 'bo', markersize=8, label='Machine')
    traversed_path_line, = ax.plot([], [], 'c-', linewidth=2, label='Traversed Path')

    # Animation function
    def update(frame):
        if frame < len(resampled_traversal_path):
            x, y = resampled_traversal_path[frame]
            machine_marker.set_data([x], [y])  # Pass as lists

            # Update traversed path
            traversed_x = [p[0] for p in resampled_traversal_path[:frame + 1]]
            traversed_y = [p[1] for p in resampled_traversal_path[:frame + 1]]
            traversed_path_line.set_data(traversed_x, traversed_y)
        return machine_marker, traversed_path_line

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=len(resampled_traversal_path), interval=50, blit=True, repeat=False)

    # Add legend
    handles, labels = ax.get_legend_handles_labels()
    unique = dict(zip(labels, handles))
    ax.legend(unique.values(), unique.keys())

    plt.title(title)
    plt.show()

# Main block
if __name__ == '__main__':
    drawer = PolygonDrawer()
    drawer.show()

    boundary_points = drawer.boundary
    obstacle_points_list = drawer.obstacles
    infill_lines = drawer.infill_lines

    if len(boundary_points) < 3:
        print("Boundary must have at least 3 points.")
        exit()

    # Use the offset boundary path calculated during drawing
    offset_boundary_path = drawer.offset_boundary_path
    if offset_boundary_path is None and infill_lines:
        print("Offset boundary path was not generated, but infill lines are present.")
    elif offset_boundary_path is None and not infill_lines:
        print("Offset boundary path was not generated, and no infill lines are present.")
    elif offset_boundary_path is not None:
        pass  # Offset path exists

    # Print number of infill lines
    print(f"\nNumber of infill lines: {len(infill_lines)}")

    # Prompt user for traversal option
    print("\nSelect Traversal Mode:")
    print("1. Traverse only the Boundary Path")
    print("2. Traverse only the Offset Path and Infill Lines")
    print("3. Traverse Boundary Path, Offset Path, and Infill Lines")
    choice = input("Enter 1, 2 or 3: ")

    if choice == '1':
        traversal_path = boundary_points
        title = "Final Path Traversal Animation - Boundary Path"
    elif choice == '2':
        if offset_boundary_path is None and not infill_lines:
            print("No offset path or infill lines to traverse.")
            exit()
        traversal_path = []
        if offset_boundary_path is not None:
            traversal_path.extend(offset_boundary_path)
        for line in infill_lines:
            traversal_path.extend(list(line.coords))
        title = "Final Path Traversal Animation - Offset Path and Infill Lines"
    elif choice == '3':
        if not boundary_points:
            print("No boundary path to traverse.")
            exit()
        traversal_path = list(boundary_points)  # Start with boundary path
        if offset_boundary_path is not None:
            traversal_path.extend(offset_boundary_path)
        for line in infill_lines:
            traversal_path.extend(list(line.coords))
        title = "Final Path Traversal Animation - Boundary, Offset Path, and Infill Lines"
    else:
        print("Invalid choice. Defaulting to traverse only the Boundary Path.")
        traversal_path = boundary_points
        title = "Final Path Traversal Animation - Boundary Path"

    # Check if traversal_path is not empty
    if not traversal_path:
        print("No valid traversal path selected.")
        exit()

    # Animate the final path traversal
    animate_final_path(traversal_path, obstacle_points_list, title=title)
