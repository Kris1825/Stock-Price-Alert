import os
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Retrieve sensitive information from environment variables
news_api_key = os.getenv('NEWS_API_KEY')
stock_api_key = os.getenv('STOCK_API_KEY')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Threshold for percentage change
percentage_threshold = 5  

# Fetching Stock Data
parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "5min",  # You can use "1min", "5min", "15min", "30min", or "60min"
    "apikey": stock_api_key
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()

# Ensure the 'Time Series (5min)' key is present
if "Time Series (5min)" in stock_data:
    time_series = stock_data["Time Series (5min)"]
    
    # Get and sort timestamps
    timestamps = list(time_series.keys())
    timestamps.sort(reverse=True)  # Sort in descending order to get the latest times first
    
    # Check if there are at least two timestamps
    if len(timestamps) >= 2:
        latest_time = timestamps[0]
        previous_time = timestamps[1]
        
        latest_closing_price = time_series[latest_time]["4. close"]
        previous_closing_price = time_series[previous_time]["4. close"]
        
        print(f"Latest closing price: {latest_closing_price} at {latest_time}")
        print(f"Previous closing price: {previous_closing_price} at {previous_time}")
        
        # Calculate the percentage change
        difference = abs(float(latest_closing_price) - float(previous_closing_price))
        percentage = (difference / float(latest_closing_price)) * 100 
        
        # Check if the percentage change exceeds the threshold value
        if percentage > percentage_threshold * 100:  # Convert percentage_threshold to percentage
            parameters1 = {
                "q": "Tesla",
                "apiKey": news_api_key,
            }
            response = requests.get(NEWS_ENDPOINT, params=parameters1)
            response.raise_for_status()
            news_data = response.json()
            articles = news_data["articles"]

            # Prepare email content
            news_content = "News Articles:\n"
            for article in articles:
                news_content += f"Title: {article['title']}\n"
                news_content += f"Description: {article['description']}\n"
                news_content += f"URL: {article['url']}\n\n"
            
            # Create email content for testing
            msg = MIMEMultipart()
            msg['From'] = EMAIL_SENDER
            msg['To'] = EMAIL_RECEIVER
            msg['Subject'] = f"Stock Price Alert: {STOCK_NAME}"
            
            body = f"Stock price for {COMPANY_NAME} has changed by more than {percentage_threshold * 100}%.\n\n"
            body += f"Latest closing price: {latest_closing_price} at {latest_time}\n"
            body += f"Previous closing price: {previous_closing_price} at {previous_time}\n\n"
            body += news_content
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Print the email content for testing
            print("\n--- Email Content ---")
            print(msg.as_string())
            print("----------------------")
        else:
            print(f"Percentage change is within the acceptable range of {percentage_threshold * 100}%.")
    else:
        print("Not enough data to compare latest and previous closing prices.")
else:
    print("No 'Time Series (5min)' data found.")
# TODO: Implement alert feature
