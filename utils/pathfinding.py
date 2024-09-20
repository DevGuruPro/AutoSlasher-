import matplotlib.pyplot as plt  
import numpy as np
from shapely.geometry import Polygon, Point, LineString
import networkx as nx
from rtree import index
from collections import deque
from shapely.strtree import STRtree
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

def compute_scaling_factor(polygon, reduction):  
    centroid = polygon.centroid  
    point_on_boundary = polygon.exterior.coords[0]  
    original_distance = centroid.distance(Point(point_on_boundary))  
    scaled_distance = original_distance - reduction  
    
    # The scale factor to reduce the distance by a fixed amount  
    scaling_factor = scaled_distance / original_distance  
    return scaling_factor

def animate_polygon_lines(polygon_points):  
    # Create a polygon using the provided points  
    polygon = Polygon(polygon_points)  

    # Get the x and y coordinates of the polygon's exterior  
    x, y = polygon.exterior.xy  

    fig, ax = plt.subplots()  

    # Set up the plot  
    ax.set_xlim(min(x) - 10, max(x) + 10)  
    ax.set_ylim(min(y) - 10, max(y) + 10)  
    ax.set_aspect('equal')  

    line, = ax.plot([], [], color='blue', linewidth=2)  

    def init():  
        line.set_data([], [])  
        return line,  

    def update(frame):  
        current_x = list(x[:frame + 1])  
        current_y = list(y[:frame + 1])  
        line.set_data(current_x, current_y)  
        return line,  

    num_frames = len(x)  

    ani = animation.FuncAnimation(  
        fig, update, frames=num_frames, init_func=init, blit=True, repeat=False, interval=500  
    )  

    plt.show()

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

def is_visible(point1, point2, obstacles):  
    line = LineString([point1, point2])  
    for obs in obstacles:  
        if line.intersects(obs):  
            return False  
    return True  

def create_visibility_graph(grid_points, obstacles):  
    G = nx.Graph()  
    for p1 in grid_points:  
        for p2 in grid_points:  
            if p1 != p2 and is_visible(p1, p2, obstacles):  
                G.add_edge(p1, p2, weight=np.linalg.norm(np.array(p1) - np.array(p2)))  
    return G  

def find_path(graph, start, end):  
    try:  
        path = nx.shortest_path(graph, source=start, target=end, weight='weight')  
        return path  
    except nx.NetworkXNoPath:  
        return []  

def create_coverage_path(grid_points, obstacles, grid_size):  
    G = create_visibility_graph(grid_points, obstacles)  
    path = []  
    visited = set()  
    
    num_columns = int((max(grid_points, key=lambda x: x[0])[0] - min(grid_points, key=lambda x: x[0])[0]) / grid_size) + 1  

    for i in range(num_columns):  
        column_points = [p for p in grid_points if abs(p[0] - (min(grid_points, key=lambda x: x[0])[0] + i * grid_size)) < grid_size / 2]  
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
    # Convert points to shapely Polygons
    origin_boundary = Polygon(boundary_points) 
    scaling_factor = compute_scaling_factor(origin_boundary, desired_reduction)  
    boundary = scale(origin_boundary, xfact=scaling_factor, yfact=scaling_factor, origin='centroid')
    origin_obstacles = [Polygon(pts) for pts in obstacle_points_list]
    obstacles = [Polygon(pts).buffer(desired_reduction) for pts in obstacle_points_list]  

    grid_size = 20  # Adjust grid size as appropriate  
    grid_points = create_grid(boundary, obstacles, grid_size)  

    # Create coverage path  
    covering_path = create_coverage_path(grid_points, obstacles, grid_size)  

    # Plot the results
    plot_boundary_obstacles_path(origin_boundary, boundary, origin_obstacles, covering_path)