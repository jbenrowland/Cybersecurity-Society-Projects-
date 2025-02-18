import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    print("Error: API key not found. Check your .env file.")

BASE_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip(ip_address):
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90
    }
    
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 401:
        print("Authentication failed. Check your API key.")
    return response.json()

# Test with a known IP
if __name__ == "__main__":
    print(check_ip("8.8.8.8"))
