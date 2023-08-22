#In the future we will use pandas, numpy and yfinance to build a stock application
# Building the stock dictionary with ten stocks
stocks = {
    'AAPL': 152.00,
  'GOOG': 2750.00,
  'TSLA': 650.50, 
    'MSFT': 280.75,
  'AMZN': 3500.25, 
  'FB': 355.00, 
    'BABA': 210.50,
  'NFLX': 550.00,
  'DIS': 185.00,
  'V': 225.75
}
print("Initial stock: ", stocks)

# Portfolio and its total value
portfolio = {
    'AAPL': 5, 'GOOG': 2, 'TSLA': 10, 'MSFT': 4, 
    'AMZN': 1, 'FB': 8, 'BABA': 7, 'NFLX': 2, 'DIS': 3, 'V': 6
}
portfolio_value = sum(portfolio[stock] * stocks[stock] for stock in portfolio)
print("Total portfolio value: ", portfolio_value)

# Finding the most expensive and least expensive stock
most_expensive_stock = max(stocks, key=stocks.get)
least_expensive_stock = min(stocks, key=stocks.get)
print("The most expensive stock: ", most_expensive_stock)
print("The least expensive stock: ", least_expensive_stock)

# Calculating the average stock price
average_price = sum(stocks.values()) / len(stocks)
print("Average stock price: ", average_price)

# Calculating the total value of all stocks
total_value = sum(stocks[stock] * portfolio[stock] for stock in portfolio)
print("Total value of all stocks: ", total_value)