import tkinter as tk
from tkinter import messagebox
import threading
import requests
from twilio.rest import Client

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "X Corp"
STOCK_API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWSAPI_API_KEY"
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

# Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def send_alert():
    def fetch_stock_data():
        stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK_NAME,
            "apikey": STOCK_API_KEY,
        }
        response = requests.get(STOCK_ENDPOINT, params=stock_params)
        data = response.json()["Time Series (Daily)"]
        data_list = [value for (key, value) in data.items()]
        yesterday_data = data_list[0]
        yesterday_closing_price = yesterday_data["4. close"]
        day_before_yesterday_data = data_list[1]
        day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
        difference_percentage = ((float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) / float(yesterday_closing_price)) * 100
        return round(difference_percentage, 2)

    def fetch_news_articles():
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        three_articles = articles[:3]
        return three_articles

    def send_sms_alert(message):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        try:
            message = client.messages.create(
                body=message,
                from_="YOUR_TWILIO_PHONE_NUMBER",
                to="RECIPIENT_PHONE_NUMBER"
            )
            print("Alert sent successfully:", message.sid)
        except Exception as e:
            print("Error sending alert:", str(e))

    stock_percentage = fetch_stock_data()
    if stock_percentage > -6:
        news_articles = fetch_news_articles()
        formatted_articles = [f"{STOCK_NAME}{'🔺' if stock_percentage > 0 else '🔻'}{stock_percentage}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in news_articles]
        
        for article in formatted_articles:
            send_sms_alert(article)

        messagebox.showinfo("Alert Sent", "Stock alerts have been sent!")

# Create the main GUI window
root = tk.Tk()
root.title("Stock Alert System")

# Create and place GUI elements (buttons, labels, etc.)
send_button = tk.Button(root, text="Send Alerts", command=send_alert)
send_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
