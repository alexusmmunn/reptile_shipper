# Used to store a hodge podge of utility functions I use elseware

import os
# https://www.geonames.org/servlet/geonames?
# requires free account activated here
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError

enviornment = os.getenv("ENVIRONMENT")

geolocator = Nominatim(user_agent="reptile_shipper")
   
def is_local()-> bool:
    """
    If enviornment is local, return true
    """
    if enviornment == "development":
        return True
    else:
        return False
    
def get_lat_lon(city:str,state_code:str)-> tuple: 
    """
    Retrieve latitude and longitude for a given city name string and 2 char state
    """
    try:
        # returns (lat,lon) as first element in a list
        coordinates = geolocator.geocode(f'{city}, {state_code}')
    except GeopyError:
        return (None,None)
    if not coordinates:
        return (None,None)
    return coordinates[1]

def round_temp_to_nearest_int(decimal_temp:float)->int:
    """
    Just converts decimal temp values to more commonly human-read ints
    """
    return int(round(decimal_temp,0))
