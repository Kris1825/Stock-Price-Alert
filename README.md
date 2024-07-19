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

## Setup Instructions

### Clone the Repository

```bash
git clone <https://github.com/Harxhit/Stock-Alert.git>
cd <repository-directory>
