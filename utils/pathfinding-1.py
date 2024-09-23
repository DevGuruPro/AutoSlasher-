import matplotlib.pyplot as plt  
import numpy as np
from shapely.geometry import Polygon, Point, LineString, box
import networkx as nx
from shapely.affinity import scale
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
    Shrinks a given polygon by moving its vertices inward towards the centroid.  

    :param polygon_coords: List of tuples representing the coordinates of the polygon vertices.  
    :param distance: Distance by which to shrink the polygon.  
    :return: A new Polygon object that is smaller by the specified distance.  
    """  
    # Create a polygon  
    polygon = Polygon(polygon_coords)  
    
    # Compute the centroid of the polygon  
    centroid = polygon.centroid  
    cx, cy = centroid.x, centroid.y  
    
    # Create list for new coordinates  
    new_coords = []  

    for x, y in polygon.exterior.coords[:-1]:  # Skip the closing coordinate which is a repeat of the first  
        # Calculate the direction vector from the centroid to the vertex  
        direction_vector = np.array([x - cx, y - cy])  
        # Normalize the direction vector  
        length = np.linalg.norm(direction_vector)  
        if length != 0:  
            normalized_vector = direction_vector / length  
        else:  
            normalized_vector = direction_vector  # Avoid division by zero  
        
        # Move the vertex towards the centroid by the specified distance  
        new_x = x - distance * normalized_vector[0]  
        new_y = y - distance * normalized_vector[1]  
        
        new_coords.append((new_x, new_y))  

    # Close the polygon by adding the first coordinate to the end  
    new_coords.append(new_coords[0])  

    # Create a new polygon with the new coordinates  
    smaller_polygon = Polygon(new_coords)  
    
    return smaller_polygon

import numpy as np  
import networkx as nx  
from shapely.geometry import Point, LineString, box  

# Inflate obstacles to ensure a safety margin around them  
def inflate_obstacles(obstacles, inflation_distance):  
    return [obs.buffer(inflation_distance) for obs in obstacles]  

# Create the grid points based on boundary and grid size, avoiding obstacles  
def create_grid(boundary, obstacles, grid_size):  
    min_x, min_y, max_x, max_y = boundary.bounds  
    x = np.arange(min_x, max_x, grid_size)  
    y = np.arange(min_y, max_y, grid_size)  
    grid_points = []  

    for i in x:  
        for j in y:  
            point = Point(i + grid_size / 2, j + grid_size / 2)  
            cell = box(i, j, i + grid_size, j + grid_size)  
            if boundary.contains(cell) and all(not cell.intersects(obs) for obs in obstacles):  
                grid_points.append(point)  

    return grid_points  

# Check if the direct line between two points is visible (unobstructed by obstacles) and fully inside the boundary  
def is_visible(point1, point2, obstacles, boundary):  
    line = LineString([point1, point2])  
    if not boundary.contains(line):  
        return False  
    for obstacle in obstacles:  
        if line.intersects(obstacle):  
            return False  
    return True  

# Create a visibility graph (only if points can be connected directly without obstacles)  
def create_visibility_graph(grid_points, obstacles, boundary):  
    G = nx.Graph()  
    for i, p1 in enumerate(grid_points):  
        for p2 in grid_points[i+1:]:  
            if is_visible(p1, p2, obstacles, boundary):  
                G.add_edge(p1, p2, weight=np.linalg.norm(np.array(p1.coords[0]) - np.array(p2.coords[0])))  
    return G  

# Find the shortest path in the visibility graph, if exists  
def find_path(graph, start, end):  
    try:  
        return nx.shortest_path(graph, source=start, target=end, weight='weight')  
    except nx.NetworkXNoPath:  
        return []  

# Implement the main function to cover the grid  
def create_coverage_path(grid_points, obstacles, boundary, grid_size):  
    def validate_line(line):  
        return boundary.contains(line) and not line.crosses(boundary.exterior) and all(not line.intersects(obs) for obs in obstacles)  

    def validate_path(temp_path):  
        for p1, p2 in zip(temp_path[:-1], temp_path[1:]):  
            if not validate_line(LineString([p1, p2])):  
                return False  
        return True  

    # Create visibility graph  
    G = create_visibility_graph(grid_points, obstacles, boundary)  
    
    path = []  
    visited = set()  

    # Choose the initial point  
    current_point = min(grid_points, key=lambda p: (p.x, p.y))  
    visited.add(current_point)  
    path.append(current_point.coords[0])  
    
    while len(visited) < len(grid_points):  
        neighbors = sorted(  
            [p for p in grid_points if p not in visited],  
            key=lambda p: np.linalg.norm(np.array(current_point.coords[0]) - np.array(p.coords[0])))  

        found_next = False  
        for neighbor in neighbors:  
            temp_path = find_path(G, current_point, neighbor)  
            if temp_path and validate_path(temp_path):  
                for pt in temp_path:  
                    if pt not in visited:  
                        path.append(pt.coords[0])  
                        visited.add(pt)  
                        current_point = pt  
                    else:  
                        path.append(pt.coords[0])  # Allow revisits  
                found_next = True  
                break  
        
        if not found_next:  
            break  # If no valid path to unvisited neighbors is found  
    
    return path

def plot_boundary_obstacles_path(boundary, sm_boundary, obstacles, covering_path):

    fig, ax = plt.subplots()  

    # Plot boundary  
    boundary_patch = plt.Polygon(boundary.exterior.coords, fill=None, edgecolor='blue')  
    ax.add_patch(boundary_patch)

    sm_boundary_patch = plt.Polygon(sm_boundary.exterior.coords, fill=None, edgecolor='brown')  
    ax.add_patch(sm_boundary_patch)

    # Plot obstacles  
    for obs in obstacles:  
        obs_patch = plt.Polygon(obs.exterior.coords, fill=None, edgecolor='red')  
        ax.add_patch(obs_patch)  

    # Plot covering path as a line connecting points  
    if covering_path:  
        path_x, path_y = zip(*covering_path)  
        ax.plot(path_x, path_y, color='orange', linewidth=1, label='Covering Path')
        ax.plot(path_x, path_y, 'ro')  

    # Labels and legend  
    ax.set_xlim(boundary.bounds[0] - 1, boundary.bounds[2] + 1)  
    ax.set_ylim(boundary.bounds[1] - 1, boundary.bounds[3] + 1)  
    ax.set_aspect('equal', adjustable='box')  
    ax.legend()  

    plt.show()

if __name__ == '__main__':  
    drawer = PolygonDrawer()  
    drawer.show()

    boundary_points = drawer.boundary
    obstacle_points_list = drawer.obstacles

    desired_reduction = 20 
    origin_boundary = Polygon(boundary_points) 
    boundary = shrink_polygon_uniform(origin_boundary, desired_reduction)
    origin_obstacles = [Polygon(pts) for pts in obstacle_points_list]
    obstacles = [Polygon(pts).buffer(desired_reduction) for pts in obstacle_points_list]  

    grid_size = 30  # Adjust grid size as appropriate  
    grid_points = create_grid(boundary, obstacles, grid_size)  

    # Create coverage path  
    covering_path = create_coverage_path(grid_points, obstacles, boundary, grid_size)  

    # Plot the results
    plot_boundary_obstacles_path(origin_boundary, boundary, origin_obstacles, covering_path)