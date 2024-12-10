"""
Retrieve seven day weather, make it into a pretty dict, then send back to the app 
for processing
"""

import os
import requests
import datetime as dt

from reptile_utilities import is_local, get_lat_lon, round_temp_to_nearest_int
from error_codes import HTTPError,create_custom_third_party_api_error, CITY_NOT_FOUND_ERROR

if is_local():
    api_key = os.getenv("LOCAL_USE_API_KEY")
    weather_api_base_url = os.getenv("OPEN_WEATHER_BASE_API_URL")
   
else:
    api_key = None
    weather_api_base_url = None

def city_daily_max_min_temp(city:str, state_code:str, date:dt=dt.datetime.now())->dict:
    """
        Use city name, 2 char state code, and date to return high/low temps for the day.

        If no date is specified, we use today as default.
    """
    (lat,lon) = get_lat_lon(city, state_code)
    if not lat:
        raise CITY_NOT_FOUND_ERROR
    date = date.strftime("%Y-%m-%d")
    complete_url = f"{weather_api_base_url}/onecall/day_summary?lat={lat}&lon={lon}&date={date}&appid={api_key}&units=imperial"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()

        temp_data = data["temperature"]
        min_temperature = round_temp_to_nearest_int(temp_data['min'])
        max_temperature = round_temp_to_nearest_int(temp_data['max'])
        temps = {'min_temp':min_temperature,'max_temp':max_temperature}
        return temps
    else:
        message = create_custom_third_party_api_error(response)
        raise HTTPError(message, 400)
        

def city_seven_day_forcast(city:str, state_code:str, first_day:dt=dt.datetime.now())->dict:
    """
    Retrieve 7 days of high/low temps for a given city
    """
    daily_temps = {'daily_temps':[]}
    
    for delta in range(7):
        current_day = first_day + dt.timedelta(days=delta)
        temps = city_daily_max_min_temp(city,state_code,current_day)
        daily_temps['daily_temps'].append({'date':current_day.strftime("%Y-%m-%d"),'temps':temps})
    seven_day_temps = daily_temps
    return seven_day_temps
    