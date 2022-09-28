import yfinance as yf


def checkfunc(stocks, stdt, eddt):
    price_data = yf.download(stocks, start=stdt, end=eddt)
    price_data = price_data.loc[:, 'Adj Close']
    price_data.columns = stocks
    stock_returns = price_data[stocks].pct_change().dropna()
    return stock_returns


stocks = ['AAPL', 'TSLA', 'MSFT']
stdt = '2021-04-01'
eddt = '2022-03-31'


xyz = checkfunc(stocks, stdt, eddt)
xyz.shape
