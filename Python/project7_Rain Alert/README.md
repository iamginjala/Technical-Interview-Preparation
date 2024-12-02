# Weather Alert App

This Python application uses the OpenWeatherMap API to forecast weather conditions and sends an SMS alert via Twilio if rain is expected. It's perfect for staying prepared during unpredictable weather.

---

## Features
- Fetches weather forecasts for the next several hours.
- Sends an SMS alert when rain is predicted.
- Easy configuration for location and phone numbers.

---

## Requirements
- Python 3.x
- Internet connection (to fetch weather data and send SMS)
- Accounts and credentials for:
  - [OpenWeatherMap API](https://openweathermap.org/api)
  - [Twilio SMS Service](https://www.twilio.com/)

---

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/Technical-Interview-Preparation/Python/project7_Rain Alert.git
    ```
2. Install the required Python libraries:
    ```bash
    pip install requests twilio
    ```

---

## Configuration
1. **OpenWeatherMap API**:  
   Sign up at [OpenWeatherMap](https://openweathermap.org/) to get an API key and replace `__YOUR_OWM_API_KEY__` in the script.

2. **Twilio Account**:  
   Sign up at [Twilio](https://www.twilio.com/) to get:
   - `account_sid`: Twilio Account SID
   - `auth_token`: Twilio Auth Token
   - Twilio virtual phone number

3. **Replace the placeholders in the script**:
   ```python
   account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
   auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"
   from_="YOUR TWILIO VIRTUAL NUMBER",
   to="YOUR TWILIO VERIFIED REAL NUMBER"
4.**Location**:
weather_params = {
    "lat": 46.947975,  # Replace with your latitude
    "lon": 7.447447,   # Replace with your longitude
    "appid": api_key,
    "cnt": 4,          # Number of 3-hour blocks to forecast
}


