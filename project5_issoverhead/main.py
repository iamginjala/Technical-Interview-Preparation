import requests
from datetime import datetime
import smtplib
import time

# Replace with your email and password
MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"

# Replace with your location's latitude and longitude
MY_LAT = 51.507351  # Example: Latitude for London
MY_LONG = -0.127758  # Example: Longitude for London

def is_iss_overhead():
    """
    Checks if the ISS is currently overhead within ±5 degrees 
    of the specified latitude and longitude.
    """
    # Fetch the current position of the ISS
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()

    # Extract the latitude and longitude of the ISS
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if the ISS is within ±5 degrees of your position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    """
    Determines if it is currently nighttime at the specified location
    using sunrise and sunset times from an API.
    """
    # Parameters for the API request
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # Use 24-hour time format
    }
    # Fetch sunrise and sunset times
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()

    # Extract sunrise and sunset hours
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour
    time_now = datetime.now().hour

    # Return True if it's nighttime
    if time_now >= sunset or time_now <= sunrise:
        return True

# Infinite loop to check conditions every minute
while True:
    time.sleep(60)  # Wait for 60 seconds before checking again

    # If the ISS is overhead and it's nighttime
    if is_iss_overhead() and is_night():
        # Connect to the email server
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)  # Log in to your email account

        # Send an email notification
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
        connection.close()  # Close the connection
