# Exercise Tracker

The **Exercise Tracker** is a Python script that helps you log exercises and their calorie data into a Google Sheet. It uses the Nutritionix API to analyze your exercise details and the Sheety API to update the Google Sheet with the collected data.

---

## Features
1. **Nutritionix API Integration**:
   - Enter your exercise details in natural language (e.g., "ran 5 km and cycled for 30 minutes").
   - Fetches exercise duration and calories burned.

2. **Sheety API Integration**:
   - Logs exercise details (date, time, type of exercise, duration, and calories) into a Google Sheet.

---

## Setup and Installation

### Prerequisites
- Python 3.x installed on your system.
- Required Python libraries: `requests`, `os`.
- Nutritionix account for API credentials.
- Sheety project linked to your Google Sheet.

### Environment Variables
Set the following environment variables for the script to run:
- **ENV_NIX_APP_ID**: Your Nutritionix API Application ID.
- **ENV_NIX_API_KEY**: Your Nutritionix API Key.
- **ENV_SHEETY_ENDPOINT**: The endpoint for your Sheety project.
- **ENV_SHEETY_USERNAME**: (Optional) Username for Sheety Basic Authentication.
- **ENV_SHEETY_PASSWORD**: (Optional) Password for Sheety Basic Authentication.

### Install Dependencies
```bash
pip install requests
