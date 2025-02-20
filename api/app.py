from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

from seven_day_weather import city_seven_day_forcast
from reptile_utilities import is_local
from error_codes import HTTPError

API_KEY = os.getenv("AUTHENTICATION_KEY")



# Create a Flask application instance
app = Flask(__name__)

# Handle rate limiting
if is_local():
    RATE_LIMIT = "5 per minute"
else:
    RATE_LIMIT = "100 per hour"
# Initialize Limiter
limiter = Limiter(
    get_remote_address,  # Uses client's IP for rate limiting
    app=app,
    default_limits=[RATE_LIMIT]
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