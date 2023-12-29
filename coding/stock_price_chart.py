# filename: stock_price_chart.py

import yfinance as yf
import matplotlib.pyplot as plt

# download stock data
nvda = yf.download('NVDA', period='ytd')['Close']
tsla = yf.download('TSLA', period='ytd')['Close']
googl = yf.download('GOOGL', period='ytd')['Close']

# calculate the change in price
nvda_change = nvda / nvda.iloc[0] - 1
tsla_change = tsla / tsla.iloc[0] - 1
googl_change = googl / googl.iloc[0] - 1

# plot the price change
plt.figure(figsize=(12,6))
plt.plot(nvda_change, label='NVDA')
plt.plot(tsla_change, label='TESLA')
plt.plot(googl_change, label='GOOGL')
plt.legend(loc='upper left')
plt.title('NVDA v/s TESLA v/s GOOGL Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Price Change')
plt.grid(True)
plt.show()