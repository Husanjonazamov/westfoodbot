
from math import radians, sin, cos, sqrt, atan2




def calculate_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Koordinatalarni radianlarga aylantirish
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


# Restoran lokatsiyasi va maksimal yetkazib berish masofasi (kilometrda)
RESTAURANT_LOCATION = {
    'latitude': 41.297337,  # Restoranning kengligi
    'longitude': 69.268648  # Restoranning uzunligi
}
MAX_DELIVERY_DISTANCE_KM = 75  # Maksimal yetkazib berish masofasi (kilometrda)
