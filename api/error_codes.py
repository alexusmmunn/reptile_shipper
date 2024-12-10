"""
Error codes used to handle various issues with processing in the backend
"""

#XXX: Need to rework this to be a bit more sensical. Different errors handled differently diff places...
class HTTPError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

CITY_NOT_FOUND_ERROR = HTTPError("Specified city not found.",400)
CITY_NOT_APPLICABLE_ERROR =HTTPError("Specified city is not supported, or does not contian a FedEx hub",400)
UNKNOWN_ERROR = HTTPError("An unknown error occured",500)


def create_custom_third_party_api_error(api_response):
    if api_response.status_code and api_response.text:
        return f"Status code: {api_response.status_code} from 3rd party api. Details: {api_response.text}"
    else:
        return UNKNOWN_ERROR
