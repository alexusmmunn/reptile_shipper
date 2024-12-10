from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import requests

from seven_day_weather import city_seven_day_forcast
from error_codes import HTTPError
# Create a Flask application instance
app = Flask(__name__)

# Define a simple endpoint
@app.route('/weather/<state>/<city>', methods=['GET'])
def seven_day_temps(city,state):
    try:
        temps = city_seven_day_forcast(city,state)
    except HTTPError as e:
        return {'status_code':e.status_code,'text':e.message}
    body = {'city':city, 'state': state, 'temps':temps}
    return jsonify(body)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)