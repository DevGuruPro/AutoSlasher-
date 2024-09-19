import matplotlib.pyplot as plt  
import numpy as np
from shapely.geometry import Polygon, Point
import networkx as nx  

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

# Visualize the map  
def plot_environment(boundary, obstacles, path=None):  
    fig, ax = plt.subplots()  
    x, y = boundary.exterior.xy  
    ax.plot(x, y, 'b-')  
    for obs in obstacles:  
        x, y = obs.exterior.xy  
        ax.plot(x, y, 'r-')  
    if path:  
        px, py = zip(*path)  
        ax.plot(px, py, 'g-', linewidth=2)  
    plt.xlim(-1, 500)  
    plt.ylim(-1, 500)  
    plt.gca().set_aspect('equal', adjustable='box')  
    plt.show()

# Create a grid within the boundary  
def create_grid(boundary, grid_size, margin=10):  
    min_x, min_y, max_x, max_y = boundary.bounds  
    x = np.arange(min_x + margin, max_x - margin, grid_size)  
    y = np.arange(min_y + margin, max_y - margin, grid_size)  
    grid_points = []  
    for i in x:  
        for j in y:  
            p = Point(i, j)  
            if (boundary.contains(p) and   
                all(not obs.contains(p) for obs in obstacles) and   
                all(not obs.exterior.distance(p) < margin for obs in obstacles)):  
                grid_points.append((i, j))  
    return grid_points

# Create a graph from the grid points  
def create_graph(grid_points, grid_size):  
    G = nx.Graph()  
    for p in grid_points:  
        G.add_node(p)  
    for p in grid_points:  
        neighbors = [  
            (p[0] + grid_size, p[1]),  
            (p[0] - grid_size, p[1]),  
            (p[0], p[1] + grid_size),  
            (p[0], p[1] - grid_size)  
        ]  
        for n in neighbors:  
            if n in grid_points:  
                G.add_edge(p, n)  
    return G  

# Find path to cover all grid points using DFS or BFS
def find_covering_path(G):  
    start = list(G.nodes())[0]  
    path = list(nx.dfs_edges(G, start))  
    return [start] + [v for u, v in path]

if __name__ == '__main__':  
    drawer = PolygonDrawer()  
    drawer.show()

    boundary_points = drawer.boundary
    obstacle_points_list = drawer.obstacles

    # Convert points to shapely Polygons  
    boundary = Polygon(boundary_points)  
    obstacles = [Polygon(pts) for pts in obstacle_points_list]  

    plot_environment(boundary, obstacles)  

    grid_size = 20
    grid_points = create_grid(boundary, grid_size)  

    G = create_graph(grid_points, grid_size)  

    covering_path = find_covering_path(G)

    # Visualize the result  
    plot_environment(boundary, obstacles, covering_path)