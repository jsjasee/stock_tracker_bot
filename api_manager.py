import os

import requests
from dotenv import load_dotenv # if there are errors importing, click on the red-bulb in pycharm and click on install python-dotenv pkg, not the dotenv pkg

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

class ApiManager:
    def __init__(self):
        self.stock_params = {
            "apikey": STOCK_API_KEY,
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
        }

        self.news_params = {
            "apiKey": NEWS_API_KEY,
            "q": COMPANY_NAME,
        }

        self.stock_data = self.get_stock_data()
        self.stock_change = 0
        self.news_data = {}

    def get_stock_data(self):
        response = requests.get(url="https://www.alphavantage.co/query", params=self.stock_params)
        response.raise_for_status()
        return response.json()

    def get_news_data(self):
        ## STEP 2: Use https://newsapi.org
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
        response = requests.get(url="https://newsapi.org/v2/everything", params=self.news_params)
        response.raise_for_status()
        return response.json()

    def is_change_signif(self):
        try:
            all_days_dict = self.stock_data['Time Series (Daily)']
        except KeyError:
            print("Maximum API rate limit reached. Try again tomorrow.")
            return False
        else:
            count = 0
            yesterday_and_day_before = []
            for (day, price_dict) in all_days_dict.items():
                if count < 2:
                    count += 1
                    yesterday_and_day_before.append(price_dict)
            raw_percentage_change = ((float(yesterday_and_day_before[0]["4. close"]) - float(yesterday_and_day_before[1]["4. close"])) / float(yesterday_and_day_before[1]["4. close"])) * 100
            formatted_percentage_change = round(raw_percentage_change, 2)
            self.stock_change = formatted_percentage_change
            if abs(formatted_percentage_change) > 5:
                self.news_data = self.get_news_data()
                return True
            else:
                return False

    def get_top_3_news_data(self):
        articles = self.news_data["articles"]
        top_3_news = [articles[index] for index in range(3)] # alternatively, use python slicing. eg. top_3_news = articles[:3], the number 3 is the stop index
        return top_3_news