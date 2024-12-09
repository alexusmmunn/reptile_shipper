from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import requests

from reptile_utilities import is_local
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
    sacramento = (38.5781,121.4944)
    complete_url = f"{weather_api_base_url}/onecall?lat={sacramento[0]}&lon={sacramento[1]}&appid={api_key}"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()

        weather_data = data['weather'][0]
        temperature = data['main']['temp']
        body = {'city':city,'weather':weather_data,'temperature':temperature}
    else:
        body = {'message': "Request failed","satus_code":response.status_code}
    return jsonify(body)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)