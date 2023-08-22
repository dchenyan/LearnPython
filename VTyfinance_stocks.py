#https://pypi.org/project/yfinance/
# We'll use yfinance to get stock data
#The two most common stock calculations are the relative strength index (RSI) and the relative strength (RS) ratio.
#RSI is a momentum oscillator that measures the magnitude of recent price changes to evaluate overbought or oversold #conditions in a security. The RSI is calculated by averaging the gains and losses over a certain number of periods (usually #14). A reading of 70 or above indicates that the security is overbought and may be due for a selloff, while a reading of 30 #or below indicates that the security is oversold and may be due for a rally.
#RS is a ratio of the average of a security's up closes to the average of its down closes over a certain number of periods ###(usually 14). A reading of 1 or above indicates that the security is outperforming the market, while a reading of below 1 #indicates that the security is underperforming the market.
#Both RSI and RS are useful tools for technical analysis, but they have different strengths and weaknesses. RSI is better at identifying overbought and oversold conditions, while RS is better at identifying relative strength or weakness against the market.
#In general, RSI is a more popular indicator than RS, but both can be used to inform your trading decisions.
#https://numpy.org/devdocs/
#https://pandas.pydata.org/docs/

import yfinance as yf
import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
#import datetime as dt


# List of a few stock symbols (tickers)
stocks = ['AAPL', 'GOOG', 'TSLA']

# This function gets the stock prices for the past week
def get_weekly_data(stock_symbol):
    data = yf.Ticker(stock_symbol)
    return data.history(period="14d")['Close'].tolist()


def rsi(prices, n=14):
    """Calculates the relative strength index (RSI) for a given set of prices.

    Args:
        prices: A list of prices.
        n: The number of periods to use.

    Returns:
        The RSI for the given prices.
    """

    gains = []
    losses = []

    for i in range(len(prices) - 1):
        close_1 = prices[i]
        close_2 = prices[i + 1]

        gain = close_2 - close_1 if close_2 > close_1 else 0
        loss = close_1 - close_2 if close_1 > close_2 else 0

        gains.append(gain)
        losses.append(loss)

    avg_gain = sum(gains) / len(gains)
    avg_loss = sum(losses) / len(losses)

    if avg_loss == 0:
        return 100

    rsi = 100 - 100 / (1 + (sum(gains) / sum(losses)))

    return rsi


def volatility(prices):
    """Calculates the volatility for the last 14 days of prices.

    Args:
        prices: A list of prices.

    Returns:
        The volatility for the last 14 days of prices.
    """

    close_prices = [prices[-i] for i in range(14)]

    daily_returns = [
        (close_prices[i] - close_prices[i - 1]) / close_prices[i - 1]
        for i in range(1, len(close_prices))
    ]

    variance = sum([d ** 2 for d in daily_returns]) / len(daily_returns)

    volatility = np.sqrt(variance)

    return volatility
  
# For each stock, we'll get its weekly data and print average, max, and min prices
for stock in stocks:
    prices = get_weekly_data(stock)

    rsi = rsi(prices)
    volatility = volatility(prices)
    # Calculating and displaying the data
    average_price = sum(prices) / len(prices)
    max_price = max(prices)
    min_price = min(prices)
    
    print(f"For {stock}:")

    print(f"  - Average price over the past week: ${average_price:.2f}")
    print(f"  - Highest price over the past week: ${max_price:.2f}")
    print(f"  - Lowest price over the past week: ${min_price:.2f}\n")
    print(f"  - Rsi over the past week: ${rsi:.2f}")
    print(f"  -  Volatility over the past week: ${volatility:.2f}")




