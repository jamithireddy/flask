import yfinance as yf

stocks = ['AAPL', 'TSLA', 'MSFT']
price_data = yf.download(stocks, start='2021-04-01', end='2022-03-31')
price_data = price_data.loc[:, 'Adj Close']
price_data.columns = stocks
stock_returns = price_data[stocks].pct_change().dropna()

stock_returns
