import math
import os

from pyproj import Transformer
import numpy as np
from shapely.geometry import Polygon, LineString, MultiPolygon
import networkx as nx

from settings import CALIBRATION, MAGNETIC_DECLINATION, DATABASE_PATH
from utils.logger import logger


def convert_to_decimal(coord, direction, is_latitude):
    try:
        # Determine sign based on direction
        sign = -1 if direction in ['S', 'W'] else 1

        if is_latitude:
            # Expect 2-digit degrees for latitude
            if len(coord) < 4:
                raise ValueError("Invalid latitude coordinate format")
            degrees = int(coord[:2])
            minutes = float(coord[2:])
        else:
            # Expect 3-digit degrees for longitude
            if len(coord) < 5:
                raise ValueError("Invalid longitude coordinate format")
            degrees = int(coord[:3])
            minutes = float(coord[3:])

        # Convert to decimal
        decimal_coord = sign * (degrees + minutes / 60)
        return decimal_coord
    except ValueError as e:
        logger.error(f"Error converting coordinate: {e}")
        return None


def extract_from_gps(gps_data):
    try:
        # Extract and convert latitude and longitude
        latitude = convert_to_decimal(gps_data['lat'], gps_data['lat_dir'], is_latitude=True)
        longitude = convert_to_decimal(gps_data['lon'], gps_data['lon_dir'], is_latitude=False)

        # Check if conversion was successful
        if latitude is None or longitude is None:
            raise ValueError("Failed to convert GPS data to decimal coordinates")

        logger.info(f"Latitude: {latitude}, Longitude: {longitude}")

        # Transform coordinates
        transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857")
        x, y = transformer.transform(latitude, longitude)
        return x, y
    except KeyError as e:
        logger.error(f"Missing key in GPS data: {e}")
        return None, None
    except ValueError as e:
        logger.error(f"Error: {e}")
        return None, None


def shrink_polygon_uniform(polygon, distance):
    smaller_polygon = polygon.buffer(-distance)
    # Handle the case where the buffer operation results in a MultiPolygon
    if isinstance(smaller_polygon, Polygon):
        return smaller_polygon
    elif isinstance(smaller_polygon, MultiPolygon):
        largest_polygon = max(smaller_polygon.geoms, key=lambda p: p.area)
        return largest_polygon
    else:
        logger.error("The shrinking operation resulted in an invalid or empty geometry.")
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
    graph = nx.Graph()
    for p1 in grid_points:
        for p2 in grid_points:
            if p1 != p2 and is_visible(p1, p2, obstacles, boundary):
                graph.add_edge(p1, p2, weight=np.linalg.norm(np.array(p1) - np.array(p2)))
    return graph


def find_path(graph, start, end):
    try:
        path = nx.shortest_path(graph, source=start, target=end, weight='weight')
        return path
    except nx.NetworkXNoPath:
        return []


def create_coverage_path(grid_points, obstacles, boundary, grid_size):
    graph = create_visibility_graph(grid_points, obstacles, boundary)
    path = []
    visited = set()

    num_columns = int(
        (max(grid_points, key=lambda x: x[0])[0] - min(grid_points, key=lambda x: x[0])[0]) / grid_size) + 1

    for i in range(num_columns):
        column_x = min(grid_points, key=lambda x: x[0])[0] + i * grid_size
        column_points = [p for p in grid_points if abs(p[0] - column_x) < grid_size / 2]
        column_points = sorted(column_points, key=lambda x: x[1])

        if i % 2 == 1:
            column_points.reverse()

        for j in range(len(column_points)):
            if column_points[j] not in visited:
                if path:
                    part_path = find_path(graph, path[-1], column_points[j])
                    path.extend(part_path[1:] if part_path else [])
                else:
                    path.append(column_points[j])
                visited.add(column_points[j])

    return path


def generate_path(field_data):
    boundary_polygon = Polygon(field_data[0])
    obstacles_polygons = [Polygon(coords) for coords in field_data[1:]]

    offset_distance = 10
    sm_boundary_polygon = shrink_polygon_uniform(boundary_polygon, offset_distance)

    if sm_boundary_polygon:
        # Step 3: Create grid
        grid_size = 10  # Adjust as needed
        grid_points = create_grid(sm_boundary_polygon, obstacles_polygons, grid_size)

        # Step 4: Create coverage path
        covering_path = create_coverage_path(grid_points, obstacles_polygons, sm_boundary_polygon, grid_size)
        return covering_path

        # Step 5: Plot everything
        # plot_boundary_obstacles_path(boundary_polygon, sm_boundary_polygon, obstacles_polygons, covering_path)
    else:
        logger.error("Failed to create a valid smaller boundary.")
        return None


def apply_calibration(x, y, z):
    # Apply calibration to raw data
    x_calibrated = _normalize(x, CALIBRATION['MIN_X'], CALIBRATION['MAX_X'])
    y_calibrated = _normalize(y, CALIBRATION['MIN_Y'], CALIBRATION['MAX_Y'])
    z_calibrated = _normalize(z, CALIBRATION['MIN_Z'], CALIBRATION['MAX_Z'])
    return x_calibrated, y_calibrated, z_calibrated


def _normalize(value, min_val, max_val):
    return (2 * (value - min_val) / (max_val - min_val)) - 1


def calculate_heading(x, y):
    # Calculate the heading in radians
    heading_radians = math.atan2(y, x)
    # Convert the heading to degrees
    heading_degrees = math.degrees(heading_radians)
    # Normalize the heading to be in the range of 0 to 360 degrees
    if heading_degrees < 0:
        heading_degrees += 360
    # Apply magnetic declination
    heading_degrees += MAGNETIC_DECLINATION
    # Normalize again to ensure it's within 0-360 degrees
    if heading_degrees >= 360:
        heading_degrees -= 360
    return heading_degrees


def calculate_heading_to_waypoint(point1, point2):
    # Calculate the direction from point1 to point2
    dy = point2[1] - point1[1]
    dx = point2[0] - point1[0]
    # atan2 returns the angle in radians; convert it to degrees
    angle = math.atan2(dy, dx) * (180 / math.pi)
    return angle % 360


def distance_to_waypoint(current_position, waypoint):
    return math.sqrt(
        (waypoint[0] - current_position[0]) ** 2 +
        (waypoint[1] - current_position[1]) ** 2
    )


def clip_speed(value):
    """ Clip the speed within the boundaries of -MAX_SPEED to MAX_SPEED. """
    return max(min(value, 1.0), -1.0)


def find_as_files():
    as_files = []
    # List all files in the given directory
    for file in os.listdir(os.getcwd()+'/'+DATABASE_PATH):
        # Check if the file extension is .as
        if file.endswith('.as'):
            as_files.append(file)
    return as_files
