import requests
from twilio.rest import Client

# Twilio configuration: Replace with your Twilio virtual number and verified phone number
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

# Stock and company details
STOCK_NAME = "TSLA"  # Ticker symbol for the stock (e.g., Tesla Inc.)
COMPANY_NAME = "Tesla Inc"  # Full name of the company

# API endpoints and credentials
STOCK_ENDPOINT = "https://www.alphavantage.co/query"  # Alpha Vantage API endpoint
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"  # News API endpoint
STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"  # Alpha Vantage API key
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"  # News API key
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"  # Twilio SID
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"  # Twilio auth token

# STEP 1: Fetch stock data using Alpha Vantage API
stock_params = {
    "function": "TIME_SERIES_DAILY",  # API function for daily stock data
    "symbol": STOCK_NAME,  # Stock ticker symbol
    "apikey": STOCK_API_KEY,  # Alpha Vantage API key
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]  # Extract daily time series data
data_list = [value for (key, value) in data.items()]  # Convert to a list of daily data

# Extract yesterday's and the day-before-yesterday's closing prices
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Calculate the price difference and determine direction (up/down)
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"

# Calculate the percentage difference in price
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# STEP 2: Fetch news if price change exceeds a threshold
if abs(diff_percent) > 1:  # Threshold for fetching news
    news_params = {
        "apiKey": NEWS_API_KEY,  # News API key
        "qInTitle": COMPANY_NAME,  # Search for news related to the company
        "language": "en",
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]  # Extract articles from the response
    three_articles = articles[:3]  # Get the top 3 articles
    print(three_articles)

    # Format news articles into SMS-ready messages
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]
    print(formatted_articles)

    # STEP 3: Send SMS alerts using Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,  # Message content
            from_=VIRTUAL_TWILIO_NUMBER,  # Twilio virtual number
            to=VERIFIED_NUMBER,  # Verified phone number
        )
        print(message.status)  # Print the message status
