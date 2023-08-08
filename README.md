# Stock Analysis and News Alert

This Python script fetches daily stock data for a given stock symbol using the Alpha Vantage API and provides analysis on the stock's performance over the last two days. It also fetches news articles related to a given company using the News API and sends alerts via SMS using the Twilio API.

## Prerequisites

Before running the script, you need to have the following:

- Python 3.x installed
- Required libraries: `requests`, `twilio` (install using `pip install requests twilio`)
## Functionality
Fetches the closing prices of the stock for the last two days and calculates the price difference and percentage change.
Determines whether the stock price increased or decreased and assigns corresponding emoji.
If the price change is within -6%, fetches news articles related to the specified company.
Formats and sends news alerts via SMS using Twilio to the specified phone number.
## Example Output
Yesterday's Closing Price: $XYZ
Day Before Yesterday's Closing Price: $ABC
Price Difference: $PQR (X.XX%)
🔺 or 🔻: Indicates increase or decrease
News Alerts:
- Headline: Article 1 Title
  Brief: Article 1 Description
- Headline: Article 2 Title
  Brief: Article 2 Description
- Headline: Article 3 Title
  Brief: Article 3 Description

## Setup

1. Replace the placeholder values in the script with your actual API keys, stock/company information, and Twilio credentials.

```python
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"


