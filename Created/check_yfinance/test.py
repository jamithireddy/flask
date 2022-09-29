import yfinance as yf
import riskfolio as rp
import pandas as pd


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
my_portfolio = rp.Portfolio(returns=xyz)
my_portfolio.assets_stats(method_mu='hist', method_cov='hist', d=0.94)
stock_weights = my_portfolio.optimization(
    model='Classic', rm='MV', obj='Sharpe', hist=True)*100
stock_weights.reset_index(inplace=True)
stock_weights.weights.astype(str)
stock_weights.columns = ['Stock', 'Weights(%)']
stock_weights = stock_weights.round(2)
stock_weights = pd.DataFrame(stock_weights)
heade
print(stock_weights)
