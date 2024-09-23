import matplotlib.pyplot as plt  
import numpy as np
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
import networkx as nx
import matplotlib.animation as animation

class PolygonDrawer:
    def __init__(self):  
        self.fig, self.ax = plt.subplots(figsize=(5, 5), dpi=100)  # 5x5 inches at 100 dpi is 500x500 pixels  
        self.ax.set_xlim(0, 500)  # Set x-axis limit  
        self.ax.set_ylim(0, 500)  # Set y-axis limit  
        self.ax.set_aspect('equal')  # Ensure aspect ratio is equal  

        self.is_drawing_boundary = True  
        self.boundary = []  
        self.obstacles = []  
        self.current_polygon = []  

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.temp_line = None  

    def onclick(self, event):  
        if event.inaxes != self.ax:  
            return  
        if event.dblclick:  
            self.finish_polygon()  
        else:  
            self.add_point(event)  

    def add_point(self, event):  
        ix, iy = event.xdata, event.ydata  
        print(f'Point clicked: ({ix}, {iy})')  

        if self.current_polygon:  
            # Remove the previous temporary line if it exists  
            if self.temp_line:  
                self.temp_line.remove()  
                self.temp_line = None  
            
            x0, y0 = self.current_polygon[-1]  
            line_color = 'b-' if self.is_drawing_boundary else 'g-'  
            self.ax.plot([x0, ix], [y0, iy], line_color)  

            x1, y1 = self.current_polygon[0]  
            self.temp_line, = self.ax.plot([ix, x1], [iy, y1], 'r--')  # Use dashed line for temporary closure line  

        self.current_polygon.append((ix, iy))  
        self.ax.plot(ix, iy, 'ro')  # Mark the vertex  
        self.fig.canvas.draw()  

    def finish_polygon(self):  
        if self.current_polygon:  
            if self.temp_line:  
                self.temp_line.remove()  
                self.temp_line = None  

            x0, y0 = self.current_polygon[-1]  
            x1, y1 = self.current_polygon[0]  
            line_color = 'b-' if self.is_drawing_boundary else 'g-'  
            self.ax.plot([x0, x1], [y0, y1], line_color)  

            if self.is_drawing_boundary:  
                self.boundary = self.current_polygon  
                self.is_drawing_boundary = False  
                print("Boundary finalized. Now drawing obstacles.")  
            else:  
                self.obstacles.append(self.current_polygon)  
                print("Obstacle added.")  

            self.current_polygon = []  
            self.fig.canvas.draw()  

    def show(self):  
        plt.axis('on')  # Keep the axes visible  
        plt.grid(True)  # Optional: Show grid  
        plt.show()

def shrink_polygon_uniform(polygon_coords, distance):  
    """
    Shrinks a given polygon by a specified distance using the buffer method.

    :param polygon_coords: List of tuples representing the coordinates of the polygon vertices.  
    :param distance: Positive distance by which to shrink the polygon.  
    :return: A new Polygon object that is smaller by the specified distance.  
    """
    # Create a polygon from the given coordinates
    polygon = Polygon(polygon_coords)
    
    # Use buffer with a negative distance to shrink the polygon inward
    smaller_polygon = polygon.buffer(-distance)
    
    # Handle the case where the buffer operation results in a MultiPolygon
    if isinstance(smaller_polygon, Polygon):
        return smaller_polygon
    elif isinstance(smaller_polygon, MultiPolygon):
        # If multiple polygons result, you may choose to take the largest one
        largest_polygon = max(smaller_polygon, key=lambda p: p.area)
        return largest_polygon
    else:
        print("The shrinking operation resulted in an invalid or empty geometry.")
        return None

def create_grid(boundary, obstacles, grid_size):  
    min_x, min_y, max_x, max_y = boundary.bounds  
    x = np.arange(min_x, max_x, grid_size)  
    y = np.arange(min_y, max_y, grid_size)  
    grid_points = []  

    for i in x:  
        for j in y:  
            cell = Polygon([  
                (i, j),  
                (i + grid_size, j),  
                (i + grid_size, j + grid_size),  
                (i, j + grid_size)  
            ])  
            if boundary.contains(cell) and all(not cell.intersects(obs) for obs in obstacles):  
                grid_points.append((i + grid_size / 2, j + grid_size / 2))  
    
    return grid_points  

def is_visible(point1, point2, obstacles, boundary):  
    line = LineString([point1, point2])  
    
    if not boundary.contains(line):  
        return False  
    
    for obs in obstacles:  
        if line.intersects(obs):  
            return False  

    return True  

def create_visibility_graph(grid_points, obstacles, boundary):  
    G = nx.Graph()  
    for p1 in grid_points:  
        for p2 in grid_points:  
            if p1 != p2 and is_visible(p1, p2, obstacles, boundary):  
                G.add_edge(p1, p2, weight=np.linalg.norm(np.array(p1) - np.array(p2)))  
    return G  

def find_path(graph, start, end):  
    try:  
        path = nx.shortest_path(graph, source=start, target=end, weight='weight')  
        return path  
    except nx.NetworkXNoPath:  
        return []  

def create_coverage_path(grid_points, obstacles, boundary, grid_size):  
    G = create_visibility_graph(grid_points, obstacles, boundary)  
    path = []  
    visited = set()  
    
    num_columns = int((max(grid_points, key=lambda x: x[0])[0] - min(grid_points, key=lambda x: x[0])[0]) / grid_size) + 1  

    for i in range(num_columns):  
        column_x = min(grid_points, key=lambda x: x[0])[0] + i * grid_size
        column_points = [p for p in grid_points if abs(p[0] - column_x) < grid_size / 2]  
        column_points = sorted(column_points, key=lambda x: x[1])  
        
        if i % 2 == 1:  
            column_points.reverse()  
        
        for j in range(len(column_points)):  
            if column_points[j] not in visited:  
                if path:  
                    part_path = find_path(G, path[-1], column_points[j])  
                    path.extend(part_path[1:] if part_path else [])  
                else:  
                    path.append(column_points[j])  
                visited.add(column_points[j])  
    
    return path

def plot_boundary_obstacles_path(boundary, sm_boundary, obstacles, covering_path):
    fig, ax = plt.subplots()
    
    # Plot original boundary
    x_orig, y_orig = boundary.exterior.xy
    ax.plot(x_orig, y_orig, 'b-', label='Original Boundary')

    # Plot smaller boundary
    if sm_boundary:
        x_sm, y_sm = sm_boundary.exterior.xy
        ax.plot(x_sm, y_sm, 'r--', label='Offset Boundary')

    # Plot obstacles
    for obs in obstacles:
        x_obs, y_obs = obs.exterior.xy
        ax.plot(x_obs, y_obs, 'k-', label='Obstacle')

    # Plot covering path
    if covering_path:
        path_x, path_y = zip(*covering_path)
        ax.plot(path_x, path_y, 'g-', label='Coverage Path')

    ax.set_aspect('equal')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    # Step 1: Use PolygonDrawer to get boundary and obstacles
    drawer = PolygonDrawer()
    print("Draw the boundary by clicking on the plot. Double-click to finish.")
    print("Then, draw obstacles. Double-click to finish each obstacle.")
    drawer.show()

    # Get boundary and obstacles from drawer
    boundary_coords = drawer.boundary
    obstacles_coords = drawer.obstacles

    # Convert to Shapely polygons
    boundary_polygon = Polygon(boundary_coords)
    obstacles_polygons = [Polygon(coords) for coords in obstacles_coords]

    # Step 2: Shrink boundary
    offset_distance = 10  # Adjust as needed
    sm_boundary_polygon = shrink_polygon_uniform(boundary_coords, offset_distance)

    if sm_boundary_polygon:
        # Step 3: Create grid
        grid_size = 10  # Adjust as needed
        grid_points = create_grid(sm_boundary_polygon, obstacles_polygons, grid_size)

        # Step 4: Create coverage path
        covering_path = create_coverage_path(grid_points, obstacles_polygons, sm_boundary_polygon, grid_size)

        # Step 5: Plot everything
        plot_boundary_obstacles_path(boundary_polygon, sm_boundary_polygon, obstacles_polygons, covering_path)
    else:
        print("Failed to create a valid smaller boundary.")
