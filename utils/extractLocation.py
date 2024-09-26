from pyproj import Transformer
from utils.logger import logger

# # Your GPS data
# gps_data = {
#     'timestamp': datetime.time(12, 14, 15, 600000, tzinfo=datetime.timezone.utc),
#     'lat': '3035.4477199',
#     'lat_dir': 'S',
#     'lon': '15248.9818695',
#     'lon_dir': 'E',
#     'gps_qual': 1,
#     'num_sats': '12',
#     'horizontal_dil': '0.48',
#     'altitude': 59.191,
#     'altitude_units': 'M',
#     'geo_sep': '30.373',
#     'geo_sep_units': 'M',
#     'age_gps_data': '',
#     'ref_station_id': ''
# }


def convert_to_decimal(coord, direction, is_latitude):
    # Determine factor for direction
    sign = -1 if direction in ['S', 'W'] else 1

    if is_latitude:
        degrees = int(coord[:2])
        minutes = float(coord[2:])
    else:
        degrees = int(coord[:3])
        minutes = float(coord[3:])

        # Convert to decimal
    decimal_coord = sign * (degrees + minutes / 60)
    return decimal_coord


def extract_from_gps(gps_data):
    # Extract and convert latitude and longitude
    latitude = convert_to_decimal(gps_data['lat'], gps_data['lat_dir'], is_latitude=True)
    longitude = convert_to_decimal(gps_data['lon'], gps_data['lon_dir'], is_latitude=False)

    logger.info(f"Latitude:{latitude}, Longitude:{longitude}")

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857")
    x, y = transformer.transform(latitude, longitude)

    return x, y
