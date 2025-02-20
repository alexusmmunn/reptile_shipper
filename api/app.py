from flask import Flask, jsonify, request
from flask_cors import CORS
import os

from seven_day_weather import city_seven_day_forcast
from error_codes import HTTPError

API_KEY = os.getenv("AUTHENTICATION_KEY")

# Create a Flask application instance
app = Flask(__name__)

# Allow calls from local front end for dev purposes
CORS(app, origins=["http://localhost:3000"])

# Authenticator for requests
def authenticate(request):
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        raise HTTPError("Unauthorized", 401)
    
# Define a simple endpoint
@app.route('/weather/<state>/<city>', methods=['GET'])
def seven_day_temps(city,state):
    try:
        authenticate(request)
        temps = city_seven_day_forcast(city,state)
    except HTTPError as e:
        return {'status_code':e.status_code,'text':e.message}
    body = {'city':city, 'state': state, 'temps':temps}
    return jsonify(body)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)