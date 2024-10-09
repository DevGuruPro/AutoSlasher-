import math
import os

from pyproj import Transformer
import numpy as np
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
import networkx as nx

from settings import CALIBRATION, MAGNETIC_DECLINATION, DATABASE_PATH, MACHINE_WIDTH
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
    x = np.arange(min_x, max_x + grid_size, grid_size)
    y = np.arange(min_y, max_y + grid_size, grid_size)
    grid_points = []

    for i in x:
        for j in y:
            point = (i, j)
            if boundary.contains(Point(point)) and all(not obs.contains(Point(point)) for obs in obstacles):
                grid_points.append(point)

    return grid_points


def is_visible(point1, point2, obstacles, boundary):
    line = LineString([point1, point2])

    if not boundary.contains(line):
        return False

    for obs in obstacles:
        if line.crosses(obs) or line.within(obs):
            return False

    return True


def create_visibility_graph(grid_points, obstacles, boundary):
    gg = nx.Graph()
    for p1 in grid_points:
        for p2 in grid_points:
            if p1 != p2 and is_visible(p1, p2, obstacles, boundary):
                gg.add_edge(p1, p2, weight=np.linalg.norm(np.array(p1) - np.array(p2)))
    return gg


def find_path(graph, start, end):
    try:
        path = nx.shortest_path(graph, source=start, target=end, weight='weight')
        return path
    except nx.NetworkXNoPath:
        return []


def create_coverage_path(grid_points, obstacles, boundary, gg=None):
    if gg is None:
        gg = create_visibility_graph(grid_points, obstacles, boundary)
    path = []
    visited = set()

    # Sort grid points for coverage path planning
    sorted_points = sorted(grid_points, key=lambda pp: (pp[0], pp[1]))
    columns = {}
    for p in sorted_points:
        columns.setdefault(p[0], []).append(p)

    columns = dict(sorted(columns.items()))
    column_keys = list(columns.keys())

    for idx, x in enumerate(column_keys):
        column_points = columns[x]
        column_points.sort(key=lambda pp: pp[1], reverse=idx % 2 == 1)
        for point in column_points:
            if point not in visited:
                if path:
                    part_path = find_path(gg, path[-1], point)
                    if part_path:
                        path.extend(part_path[1:])
                    else:
                        path.append(point)
                else:
                    path.append(point)
                visited.add(point)

    return path


def generate_offset_paths(boundary_polygon, obstacles_polygons, num_offsets, grid_size):
    offset_paths = []

    for i in range(1, num_offsets + 1):
        offset_distance = -i * grid_size
        offset_polygon = boundary_polygon.buffer(offset_distance)

        if not offset_polygon.is_empty and isinstance(offset_polygon, (Polygon, MultiPolygon)):
            if isinstance(offset_polygon, MultiPolygon):
                offset_polygon = max(offset_polygon.geoms, key=lambda p: p.area)

            for obs in obstacles_polygons:
                offset_polygon = offset_polygon.difference(obs)

            if isinstance(offset_polygon, Polygon):
                offset_coords = list(offset_polygon.exterior.coords)
                offset_paths.append(offset_coords)
            elif isinstance(offset_polygon, MultiPolygon):
                for poly in offset_polygon.geoms:
                    offset_coords = list(poly.exterior.coords)
                    offset_paths.append(offset_coords)
        else:
            print(f"Offset {i} is invalid or empty.")

    return offset_paths


def generate_path(field_data, ma_width, offset_path):
    boundary_polygon = Polygon(field_data[0])
    obstacles_polygons = [Polygon(coords) for coords in field_data[1:]]

    grid_size = int(15 * ma_width / MACHINE_WIDTH)  # Adjust as needed

    coverage_segments = []
    all_points = set()

    # Generate offset paths
    if offset_path > 0:
        offset_paths = generate_offset_paths(boundary_polygon, obstacles_polygons, offset_path, grid_size)
        for offset_coords in offset_paths:
            coverage_segments.append(offset_coords)
            all_points.update(offset_coords)

    # Step 3: Create grid within original boundary
    grid_points = create_grid(boundary_polygon, obstacles_polygons, grid_size)
    all_points.update(grid_points)

    # Now, create visibility graph over all_points
    all_points = list(all_points)  # Convert to list
    gg = create_visibility_graph(all_points, obstacles_polygons, boundary_polygon)

    # Step 4: Create coverage path
    grid_coverage_path = create_coverage_path(grid_points, obstacles_polygons, boundary_polygon, gg)
    coverage_segments.append(grid_coverage_path)

    # Now, build the final coverage path by connecting segments
    coverage_path = []

    for i in range(len(coverage_segments)):
        segment = coverage_segments[i]
        if i == 0:
            coverage_path.extend(segment)
        else:
            # Find path from last point of previous segment to first point of current segment
            start_point = coverage_path[-1]
            end_point = segment[0]
            if start_point != end_point:
                transition_path = find_path(gg, start_point, end_point)
                if transition_path:
                    coverage_path.extend(transition_path[1:])  # Exclude the first point
                else:
                    print(f"No path found between segment {i - 1} and segment {i}. Adding direct connection.")
                    coverage_path.append(end_point)
            coverage_path.extend(segment)
    return coverage_path


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
