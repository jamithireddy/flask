import yfinance as yf
import riskfolio as rp
import pandas as pd


def checkfunc(stocks, stdt, eddt):
    price_data = yf.download(stocks, start=stdt, end=eddt)
    price_data = price_data.loc[:, 'Adj Close']
    price_data.columns = stocks
    stock_returns = price_data[stocks].pct_change().dropna()
    return stock_returns

stocks = ['TCS.NS', 'EASEMYTRIP.NS', 'AAVAS.NS', 'ABBOTINDIA.NS', 'DIXON.NS', 'BHARTIARTL.NS', 'SUNPHARMA.NS', 'WHIRLPOOL.NS', 'UBL.NS', 'INDIGO.NS', 'INDUSINDBK.NS', 'ICICIBANK.NS', 'ABFRL.NS', 'MARUTI.NS', 'EICHERMOT.NS',
          'ITC.NS', 'VGUARD.NS', 'PHOENIXLTD.BO', 'CONCOR.NS', 'ASHOKLEY.NS', 'JUBLFOOD.NS', 'AIAENG.NS', 'CUMMINSIND.NS', 'GODREJCP.NS', 'HDFCBANK.NS', 'TRENT.NS', 'SBIN.NS', 'CUB.NS', 'TVSMOTOR.NS', 'KAJARIACER.NS']
stdt = '2021-04-01'
eddt = '2022-09-28'


xyz = checkfunc(stocks, stdt, eddt)

xyz.to_csv('/Users/rjamithireddy/Desktop/stocks.csv')
 