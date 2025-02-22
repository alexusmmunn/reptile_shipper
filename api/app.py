from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv

from seven_day_weather import city_seven_day_forcast
from reptile_utilities import is_local
from error_codes import HTTPError

# load variables from .env since sometimes Flask doesn't do this automatically
load_dotenv()

API_KEY = os.getenv("AUTHENTICATION_KEY")
REDIS_URL = os.getenv("REDIS_URL")

# Create a Flask application instance
app = Flask(__name__)


# Allow calls from local front end for dev purposes
CORS(app, origins=["http://localhost:3000"])

# You might think it's weird to use Redis for local rate limiting - and you're right.
# I'm currently using the free tier of Geopy, I don't want to go over the daily limit 
# between local and production. Track both with one rate limiting value.
# XXX: Actually, this may not matter since in all likelihood requests are coming from two different IPs...
RATE_LIMIT = "999 per day"
limiter = Limiter(
    get_remote_address,  # Uses client's IP for rate limiting
    app=app,
    default_limits=[RATE_LIMIT],
    storage_uri=REDIS_URL
)


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