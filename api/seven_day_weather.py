"""
Retrieve seven day weather, make it into a pretty dict, then send back to the app 
for processing
"""

import os
import requests

from reptile_utilities import is_local, get_lat_lon, round_temp_to_nearest_int
from error_codes import HTTPError,create_custom_third_party_api_error, CITY_NOT_FOUND_ERROR
from dotenv import load_dotenv

# load variables from .env since sometimes Flask doesn't do this automatically
load_dotenv()

# TODO: eventually these will perhaps be different, for now they are the same
if is_local():
    api_key = os.getenv("LOCAL_USE_API_KEY")
    weather_api_base_url = os.getenv("OPEN_WEATHER_BASE_API_URL")
else:
    api_key = os.getenv("LOCAL_USE_API_KEY")
    weather_api_base_url = os.getenv("OPEN_WEATHER_BASE_API_URL")


def city_seven_day_forcast(city:str, state_code:str)->dict:
    """
    Retrieve 7 days of high/low temps for a given city
    """
    (lat,lon) = get_lat_lon(city, state_code)
    if not lat:
        raise CITY_NOT_FOUND_ERROR
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_min,temperature_2m_max&timezone=auto&forecast_days=7&temperature_unit=fahrenheit"
    response = requests.get(url)
    data = response.json()

    # Extract relevant data
    dates = data["daily"]["time"]
    min_temps = data["daily"]["temperature_2m_min"]
    max_temps = data["daily"]["temperature_2m_max"]

    # Format into desired dict structure
    weather_dict = {
        date: (min_temps[i], max_temps[i]) for i, date in enumerate(dates)
    }
    print(weather_dict)

    return weather_dict
    