import numpy as np  
from stl import mesh  
from scipy.spatial import Delaunay  
import trimesh
import subprocess

def create_3d_mesh_from_2d_points(points, height):
    tri = Delaunay(points)  
    triangles = tri.simplices  

    vertices = []  
    for point in points:  
        vertices.append([point[0], point[1], 0])    # Base  
        vertices.append([point[0], point[1], height])  # Top  

    vertices = np.array(vertices)  

    faces = []  
    num_points = len(points)  
    for simplex in triangles:  
        # Base face  
        faces.append([simplex[0], simplex[1], simplex[2]])  
        # Top face  
        faces.append([simplex[0] + num_points, simplex[1] + num_points, simplex[2] + num_points])  
        # Side faces  
        faces.append([simplex[0], simplex[1], simplex[0] + num_points])  
        faces.append([simplex[1], simplex[1] + num_points, simplex[0] + num_points])  
        faces.append([simplex[1], simplex[2], simplex[1] + num_points])  
        faces.append([simplex[2], simplex[2] + num_points, simplex[1] + num_points])  
        faces.append([simplex[2], simplex[0], simplex[2] + num_points])  
        faces.append([simplex[0], simplex[0] + num_points, simplex[2] + num_points])  

    # Create the STL mesh  
    mesh_data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)  
    for i, face in enumerate(faces):  
        for j in range(3):  
            mesh_data["vectors"][i][j] = vertices[face[j]]  
    
    return mesh.Mesh(mesh_data)  

boundary_points = [  
    (10, 10), (20, 10), (30, 12), (40, 13), (50, 15), (60, 20), (70, 25),  
    (80, 25), (100, 28), (120, 30), (140, 34), (160, 35), (180, 40),
    (480, 50), (490, 62), (490, 75), (470, 80), (480, 93), (475, 470),
    (440, 480), (435, 478), (432, 475), (100, 480), (10, 340) 
]  


# Example data  
obstacle_points_list = [
    [(150, 180), (180, 210), (150, 245), (120, 220), (130, 190)],
    # [(300, 50), (320, 60), (330, 75), (315, 90), (295, 80)],
    [(280, 300), (320, 330), (340, 360), (290, 380), (270, 310)]
]  

boundary_mesh = create_3d_mesh_from_2d_points(boundary_points, 1)  

boundary_trimesh = trimesh.Trimesh(vertices=boundary_mesh.vectors.reshape(-1, 3),  
                                   faces=np.arange(len(boundary_mesh.vectors) * 3).reshape(-1, 3))  

obstacle_meshes = []  
for obstacle_points in obstacle_points_list:  
    obstacle_mesh = create_3d_mesh_from_2d_points(obstacle_points, 1)  
    obstacle_trimesh = trimesh.Trimesh(vertices=obstacle_mesh.vectors.reshape(-1, 3),  
                                       faces=np.arange(len(obstacle_mesh.vectors) * 3).reshape(-1, 3))  
    obstacle_meshes.append(obstacle_trimesh)  

combined_mesh = trimesh.util.concatenate([boundary_trimesh] + obstacle_meshes)  

mesh_file = 'combined.stl'

combined_mesh.export(mesh_file)


gcode_file = 'combined.gcode'


subprocess.run(['Slic3r-console.exe', mesh_file, '--output', gcode_file])

path = []  
current_position = [0.0, 0.0, 0.0]

with open(file_path, 'r') as file:  
    for line in file:  
        line = line.strip()  
        if line.startswith('G0') or line.startswith('G1'):  
            # Parse movement command  
            x_match = re.search(r'X([\d\.\-]+)', line)  
            y_match = re.search(r'Y([\d\.\-]+)', line)  
            z_match = re.search(r'Z([\d\.\-]+)', line)  
            
            if x_match: current_position[0] = float(x_match.group(1))  
            if y_match: current_position[1] = float(y_match.group(1))  
            if z_match: current_position[2] = float(z_match.group(1))  

            # Append copy of current_position to path list  
            path.append(current_position.copy())

for point in path:  
    print(point)
