import requests
from datetime import datetime
import os

# User personal data for calculating calories burned
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 26

# Nutritionix API credentials (set via environment variables for security)
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

# Nutritionix API endpoint for exercise analysis
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Input from the user describing the exercises
exercise_text = input("Tell me which exercises you did: ")

# Headers for Nutritionix API authentication
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Parameters for the API call, including exercise details and user stats
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Sending a POST request to Nutritionix and fetching exercise data
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Adding current date and time to the exercise log
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety API setup for updating Google Sheets
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

# Iterating through each exercise in the Nutritionix response
for exercise in result["exercises"]:
    # Structuring data for the Sheety API request
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sending data to Sheety using Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )
