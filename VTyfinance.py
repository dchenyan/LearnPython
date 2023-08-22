# We'll use yfinance to get stock data
import yfinance as yf

# List of a few stock symbols (tickers)
stocks = ['AAPL', 'GOOG', 'TSLA', 'PDD', 'BABA']

# This function gets the stock prices for the past week
def get_weekly_data(stock_symbol):
    data = yf.Ticker(stock_symbol)
    return data.history(period="7d")['Close'].tolist()

# For each stock, we'll get its weekly data and print average, max, and min prices
for stock in stocks:
    prices = get_weekly_data(stock)
    
    # Calculating and displaying the data
    average_price = sum(prices) / len(prices)
    max_price = max(prices)
    min_price = min(prices)
    
    print(f"For {stock}:")
    print(f"  - Average price over the past week: ${average_price:.2f}")
    print(f"  - Highest price over the past week: ${max_price:.2f}")
    print(f"  - Lowest price over the past week: ${min_price:.2f}\n")
