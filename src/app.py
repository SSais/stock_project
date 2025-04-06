import requests
import json  # Need to check if this is required
import os

from dotenv import load_dotenv
from requests.exceptions import RequestException, Timeout

# Set up environment file
load_dotenv()

api_key = os.environ.get('API_KEY')

# Add API Key to url
url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=NVDA&apikey={api_key}'


# function to GET API
def get_request(url: str):
    try:
        response = requests.get(url)
        print(response.status_code)  # gives back 200
        return response.json()
    except Timeout:
        raise RequestException('The request timed out - Request failed for URL')
    except RequestException:
        raise RequestException('Invalid URL - Request failed for URL')
    except Exception:
        raise RequestException('An error occurred - Unexpected error for URL')

# Save the API request in a variable
# data = get_request(url)

# Test to handle and check status
