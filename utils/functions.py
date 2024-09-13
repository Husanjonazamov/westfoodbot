
import math
from geopy.geocoders import Nominatim

def get_location_name(lat, lon):
    geolocator = Nominatim(user_agent="location_finder")
    location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True)
    
    if location:
        address = location.raw['address']
        
        # Extracting relevant parts of the address
        village = address.get('village', '')
        hamlet = address.get('hamlet', '')
        town = address.get('town', '')
        county = address.get('county', '')
        state = address.get('state', '')
        
        # Building the location name in desired order
        location_name = ", ".join(filter(None, [state, county, town, village, hamlet]))
        
        return location_name if location_name else None
    else:
        return None

def captionToCount(caption):
    """
    get product count in:
        🍟 Food title
        Nx
        N X N So'm = Total N so'm
    """
    try:
        count = int(caption.split('\n')[1].replace("x", ""))
        return count

    except:
        count = 1


def calculate_distance(lat1, lon1, lat2, lon2):
    # Radius of the earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance


def calc_delivered_time(dis, speed):
    # Vaqtni soatlar va minutlarga aylantiramiz
    vaqt_soat = dis / speed

    # Vaqtni soatlar va minutlarga aylantiramiz
    soat = int(vaqt_soat)
    minut = int((vaqt_soat - soat) * 60)

    return f"{soat} soat, {minut} minut"


def create_google_maps_link(latitude, longitude, zoom=12, map_service="yandex"):
    """
    Given latitude and longitude, this function returns a URL link to either Google Maps or Yandex Maps.

    Parameters:
    latitude (float): Latitude of the location.
    longitude (float): Longitude of the location.
    map_service (str): Map service to use ('google' or 'yandex'). Default is 'google'.

    Returns:
    str: URL link to the map service showing the specified location.
    """
    if map_service == 'google':
        return f"https://www.google.com/maps?q={latitude},{longitude}"
    elif map_service == 'yandex':
        return f"https://yandex.com/maps/?pt={longitude},{latitude}&z=14&l=map"
    else:
        return "Invalid map service specified. Use 'google' or 'yandex'."
