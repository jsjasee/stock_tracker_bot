# Stock Tracker Bot
A bot that monitors fluctuations in stock prices and alerts users with relevant news when price changes are significant.

## Table of contents
- Features
- Technologies used
- Usage

## Features
- Stock Price Monitoring: Tracks stock price changes between yesterday and the day before in real-time.
- Significant Change Alerts: Sends alerts when price changes cross a predefined threshold.
- News Integration: Fetches and delivers relevant news articles about the stock.
- Customizable Thresholds: Allows users to set thresholds for price change alerts.

## Technologies Used
- Programming language: Python
- APIs: Alpha Vantage for stock prices, NewsAPI for news
- Messaging: Telebot

## Usage
1. Clone the repository
2. Install dependencies
3. Set up env variables by creating a .env file in the root directory, and add api keys and credentials, including your telegram bot chatid
4. Change constants, STOCK and COMPANY_NAME to track the desired stock.# stock_tracker_bot
