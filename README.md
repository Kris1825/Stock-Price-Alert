[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![API](https://img.shields.io/badge/API-Active-blue?style=for-the-badge&logo=api&logoColor=white)](https://example.com)
[![API Developer](https://img.shields.io/badge/API%20Developer-Active-blue?style=for-the-badge&logo=api&logoColor=white)](https://example.com)



# Stock Price Alert System

## Description

The **Stock Price Alert System** is a Python application that monitors the stock price of a specified company and sends an email alert if the percentage change in the stock price exceeds a defined threshold. The program fetches real-time stock price data and recent news articles related to the company, then sends an email containing the stock price change information and news updates.

## Features

- Monitors stock price changes at a specified interval.
- Fetches recent news articles related to the company if significant price changes are detected.
- Sends an email alert with the stock price information and news articles if the price change exceeds the defined threshold.

## Technologies Used

- **Python**: Programming language used for the application.
- **Requests**: For making HTTP requests to fetch stock and news data.
- **Email**: For sending email alerts.
- **Alpha Vantage API**: Provides real-time stock price data.
- **News API**: Provides recent news articles related to the company.

## How It Works
- **Fetch Stock Data**: The program retrieves real-time stock price data from Alpha Vantage for a specified stock symbol.
- **Calculate Price Change**: It calculates the percentage change in the stock price between the latest and previous timestamps.
- **Check Threshold**: If the percentage change exceeds the defined threshold, the program fetches recent news articles related to the company.
- **Send Email Alert**: An email is composed and sent with the stock price information and news articles if the threshold is exceeded.
- **Output**t: The program prints the email content for testing purposes and notifies if the percentage change is within the acceptable range.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, please contact:

[![Gmail](https://img.shields.io/badge/Gmail-harsxit04@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:harsxit04@gmail.com)



## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/Harxhit/Stock-Alert.git

# Install Dependencies
Ensure you have requests and other necessary libraries installed. You can install them using pip:

pip install pip install request

# Set Up Environment Variables
# Create a .env file in the root directory of the project with the following content:

NEWS_API_KEY=your_news_api_key
STOCK_API_KEY=your_stock_api_key
EMAIL_SENDER=your_email@example.com
EMAIL_RECEIVER=receiver_email@example.com
EMAIL_PASSWORD=your_email_password

# Replace your_news_api_key, your_stock_api_key, your_email@example.com, receiver_email@example.com, and your_email_password with your actual API keys and email credentials.

# Run the Program

#Execute the Python script to start monitoring stock prices and sending alerts:

python stock_price_alert.py

### Modified by Kris1825
