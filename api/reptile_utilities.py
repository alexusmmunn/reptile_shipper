# Used to store a hodge podge of utility functions I use elseware

from dotenv import load_dotenv
import os

enviornment = os.getenv("ENVIRONMENT")

def is_local():
    if enviornment == "development":
        return True
    else:
        return False