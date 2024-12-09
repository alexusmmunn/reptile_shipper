"""
Error codes used to handle various issues with processing in the backend
"""

class ErrorCode(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(self.message)

    def __repr__(self):
        return f"Error {self.code}: {self.message}"
    
CITY_NOT_FOUND_ERROR = ErrorCode(code=400, message="Specified city not found.")
CITY_NOT_APPLICABLE_ERROR = ErrorCode(code=400, message="Specified city is not supported, or does not contian a FedEx hub")
UNKNOWN_ERROR = ErrorCode(code=500,message="An unexpected error has occured.")


def create_custom_third_party_api_error(api_response):
    if api_response.status_code and api_response.text:
        return ErrorCode(api_response.status_code, api_response.text)
    else:
        return UNKNOWN_ERROR
