# ISS Overhead Notifier

This Python script notifies you via email whenever the International Space Station (ISS) is overhead and it's nighttime at your location. The script uses APIs to determine the ISS's position and the time of sunrise and sunset.

## Features
- Checks the current position of the ISS.
- Verifies if it's nighttime at your location.
- Sends an email notification when the ISS is visible in the night sky.

---

## Requirements
- Python 3.x
- Internet connection

---

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo-name/iss-overhead-notifier.git
    ```
2. Install the required Python libraries:
    ```bash
    pip install requests
    ```

---

## Configuration
1. Replace the following placeholders in the script with your information:
    ```python
    MY_EMAIL = "___YOUR_EMAIL_HERE____"
    MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
    MY_LAT = 51.507351  # Your latitude
    MY_LONG = -0.127758  # Your longitude
    ```
    - Use your email address and password for email notifications.
    - Use your geographical latitude and longitude.

2. Update the SMTP server address for your email provider:
    ```python
    connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
    ```
    For example:
    - Gmail: `smtp.gmail.com`
    - Yahoo: `smtp.mail.yahoo.com`

---

## How It Works
1. The script fetches the current location of the ISS using the `http://api.open-notify.org/iss-now.json` API.
2. It checks if the ISS is within ±5 degrees of your latitude and longitude.
3. It retrieves sunrise and sunset times using the `https://api.sunrise-sunset.org/json` API and checks if it's nighttime at your location.
4. If both conditions are met, the script sends you an email notification every 60 seconds until the ISS moves out of range.

---

## Running the Script
Run the script with:
```bash
python iss_notifier.py
