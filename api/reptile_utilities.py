# Used to store a hodge podge of utility functions I use elseware

from dotenv import load_dotenv
import os
# https://www.geonames.org/servlet/geonames?
# requires free account activated here
from geopy import geocoders

enviornment = os.getenv("ENVIRONMENT")
geonames_username = os.getenv("GEONAMES_USERNAME")
geo = geocoders.GeoNames(username=geonames_username)

def is_local():
    if enviornment == "development":
        return True
    else:
        return False
    
def get_lat_lon(city):
    # TODO: Modify so this takes any name of a city and returns lat lon
    # Right now geonames isn't working... I'm getting 401s
    if city == 'sacramento':
        return (38.5781,121.4944)
    return None
