from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import requests

from reptile_utilities import is_local, get_lat_lon
# Create a Flask application instance
app = Flask(__name__)

if is_local():
    api_key = os.getenv("LOCAL_USE_API_KEY")
    weather_api_base_url = os.getenv("OPEN_WEATHER_BASE_API_URL")
   
else:
    api_key = None
    weather_api_base_url = None

# Define a simple endpoint
@app.route('/weather/<city>', methods=['GET'])
def single_city_forecast(city):
    (lat,lon) = get_lat_lon(city)
    complete_url = f"{weather_api_base_url}/onecall?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()

        temp_data = data['daily'][0]['temp']
        min_temperature = temp_data['min']
        max_temperature = temp_data['max']
        body = {'city':'sacramento','min temp':min_temperature,'max temp':max_temperature}
    else:
        body = {'message': "Request failed","satus_code":response.status_code}
    return jsonify(body)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)