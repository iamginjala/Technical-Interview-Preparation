import requests
from twilio.rest import Client

# OpenWeatherMap API endpoint for fetching weather data
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Replace with your OpenWeatherMap API key
api_key = "__YOUR_OWM_API_KEY__"

# Replace with your Twilio account SID and auth token
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

# Parameters for the weather API request
weather_params = {
    "lat": YOUR OWN LAT,  # Latitude for the location (e.g., Bern, Switzerland)
    "lon": YOUR OWN LONG,   # Longitude for the location
    "appid": api_key,  # API key for authentication
    "cnt": 4,          # Number of forecast blocks (each block represents 3 hours)
}

# Send a request to the OpenWeatherMap API
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()  # Raise an error if the request fails
weather_data = response.json()  # Parse the response as JSON

# Variable to check if rain is expected
will_rain = False

# Iterate through each forecast block in the weather data
for hour_data in weather_data["list"]:
    # Extract the weather condition code
    condition_code = hour_data["weather"][0]["id"]

    # Check if the condition code indicates rain (codes below 700)
    if int(condition_code) < 700:
        will_rain = True

# If rain is expected, send an SMS alert using Twilio
if will_rain:
    # Initialize the Twilio Client
    client = Client(account_sid, auth_token)

    # Create and send the SMS message
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",  # Message content
        from_="YOUR TWILIO VIRTUAL NUMBER",  # Twilio virtual number
        to="YOUR TWILIO VERIFIED REAL NUMBER"  # Your verified phone number
    )

    # Print the status of the message (e.g., 'queued', 'sent', etc.)
    print(message.status)
