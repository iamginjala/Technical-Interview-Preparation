import requests
from datetime import datetime

# User-specific configurations
TOKEN = "--create your own token--"  # Unique token for Pixela API authentication
USERNAME = "--create your own user name--"  # Pixela username
ID = "graph1"  # Graph ID for tracking habits

# Pixela API endpoints
pixela_user_endpoint = "https://pixe.la/v1/users"

# Parameters for creating a new Pixela user
user_parameters = {
    "token": TOKEN,  # Unique token for authentication
    "username": USERNAME,  # Desired username
    "agreeTermsOfService": "yes",  # Agree to Pixela's terms of service
    "notMinor": "yes",  # Confirm age compliance
}

# Uncomment to create a new Pixela user account
# response = requests.post(url=pixela_user_endpoint, json=user_parameters)
# print(response.text)  # Print the API response

# Endpoint and parameters for creating a new graph
graph_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": ID,  # Unique graph ID
    "name": "coding graph",  # Graph name
    "unit": "min",  # Unit of measurement (e.g., minutes)
    "type": "int",  # Data type (integer)
    "color": "momiji",  # Graph color (preset options)
}

# Header for authentication
header = {
    "X-USER-TOKEN": TOKEN,  # API authentication token
}

# Uncomment to create a new graph
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
# print(response.text)  # Print the API response

# Get today's date
today = datetime.now()

# Endpoint for logging activity to the graph
post_pixela_endpoint = f"{graph_endpoint}/{ID}"
post_parameters = {
    "date": today.strftime("%Y%m%d"),  # Format the date as YYYYMMDD
    "quantity": input("How many hours did you spend today? "),  # User input for activity quantity
}

# Uncomment to log activity
# response = requests.post(url=post_pixela_endpoint, json=post_parameters, headers=header)
# print(response.text)  # Print the API response

# Parameters for updating graph properties
update_parameters = {
    "color": "ajisai",  # Update graph color to 'ajisai'
}

# Uncomment to update graph properties
# update_response = requests.put(url=post_pixela_endpoint, json=update_parameters, headers=header)
# print(update_response.text)  # Print the API response

# Endpoint for deleting a specific entry
terminate_endpoint = f"{post_pixela_endpoint}/{today.strftime('%Y%m%d')}"

# Uncomment to delete an entry
# response = requests.delete(url=terminate_endpoint, headers=header)
# print(response.text)  # Print the API response
