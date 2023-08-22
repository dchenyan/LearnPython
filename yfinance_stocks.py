#use yfinace to get stock data
import yfinance.py as yf
import numpy as np
#import matplotlib.pyplot as plt
#iport pandas as pd
#import datetime as dt

#List of a few stock symbols (tickers)
stocks=['AAPL', 'GOOG', 'TSLA']

#This function gets the stock prices for the past week; gives closing stock price in the 7 days
#def defines a function
def get_weekly_data(stock_symbol):
    data= yf.Ticker(stock_symbol)
    return data.history(period="14d")''Close'}.tolist()

def rsi(prices, n=14):
    ***Calclulates the relative strength index (RSI) for a given set of prices.

    Args:
        prices: A list of prices
        n: The number of peridos to use.

    Returns:
        The RSI for the given prices
    ***
''



return 


def volatility()

#For each stoc, we'll get its weekly data and print average, max, and min prices
for stock in stocks:
    prices = get_weekly_data(stock)

    rsi = rsi(prices)
    volatility = volatility(prices)

    # Calculating and displaying the data
    average_price = sum(prices) / len(prices)
    max_price=max(prices)
    min_price = min(prices)

    print(f"For {stocks}:")
    print(f" - Average price over the past week: ${average_price:.2f}")
    print(f" - Highest price over the past week: ${max_price:.2f}")
    print(f" - Lowest  price over the past week: ${min_price:.2f}")
    print(f" - RSI over the past week: ${rsi:.2f}")
    print(f" - Volatility over the past week: ${volatility:.2f}")