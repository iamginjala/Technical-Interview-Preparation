# Stock Alert and News Notification App

This Python application tracks stock price fluctuations for a specified company and sends SMS notifications if significant price changes occur. The app also retrieves the latest news articles about the company and sends them as SMS messages using Twilio.

---

## Features
- Monitors stock price changes using the Alpha Vantage API.
- Fetches the latest news about the company using the News API.
- Sends SMS alerts with stock price changes and related news headlines via Twilio.

---

## Requirements
- Python 3.x
- API keys for:
  - [Alpha Vantage](https://www.alphavantage.co/)
  - [News API](https://newsapi.org/)
  - [Twilio](https://www.twilio.com/)
- A Twilio account with a verified phone number.

---

## Installation
    ```
1. Install the required Python libraries:
    ```bash
    pip install requests twilio
    ```

---

## Configuration
1. **API Keys and Credentials**:
   - Replace the placeholders in the script with your actual API keys and credentials:
     ```python
     STOCK_API_KEY = "YOUR ALPHA VANTAGE API KEY"
     NEWS_API_KEY = "YOUR NEWSAPI API KEY"
     TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
     TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
     VIRTUAL_TWILIO_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
     VERIFIED_NUMBER = "YOUR VERIFIED PHONE NUMBER"
     ```

2. **Stock and Company Details**:
   - Update the `STOCK_NAME` and `COMPANY_NAME` variables:
     ```python
     STOCK_NAME = "TSLA"  # Stock ticker symbol
     COMPANY_NAME = "Tesla Inc"  # Full company name
     ```

---

## How It Works
1. **Stock Price Monitoring**:
   - Fetches the stock's closing prices for the last two days using the Alpha Vantage API.
   - Calculates the percentage change between the two closing prices.
   - Triggers a notification if the price change exceeds a set threshold (default: 5%).

2. **News Fetching**:
   - Retrieves the latest news articles about the company from the News API.
   - Extracts the first three articles with headlines and descriptions.

3. **SMS Notification**:
   - Formats the stock price change and news into a user-friendly message.
   - Sends each message via Twilio to the specified phone number.

---

## Running the App
1. Save the script as `stock_alert.py`.
2. Run the script:
    ```bash
    python stock_alert.py
    ```
3. If significant stock price changes occur, you will receive SMS alerts with stock updates and related news articles.

---

## Example Output
### Console Output
```plaintext
750.00
740.00
-1.33%
[{'title': 'Tesla releases new update...', 'description': 'Tesla's new software update...'}]
