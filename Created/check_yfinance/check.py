from crypt import methods
import pandas as pd
import riskfolio as rp
from flask import Flask, render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import yfinance as yf

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"


class stockinfo(FlaskForm):
    scrips = StringField("Enter the scrips", validators=[DataRequired()])
    stdt = DateField("Enter the Start date")
    eddt = DateField("Enter the End date")
    model = SelectField("Please select Model", choices=[('Classic', 'Classic:  use estimates of expected return vector and covariance matrix that depends on historical data.'), ('BL', 'BL:  use estimates of expected return vector and covariance matrix based on the Black Litterman model.'), (
        'FM', 'FM:  use estimates of expected return vector and covariance matrix based on a Risk Factor model specified by the user.'), ('BLFM', 'BLFM:  use estimates of expected return vector and covariance matrix based on Black Litterman applied to a Risk Factor model specified by the user.')])
    rm = SelectField("Please select Risk measure", choices=[('MV', 'MV:  Standard Deviation.'), ('MAD', 'MAD:  Mean Absolute Deviation.'), ('GMD', 'GMD:  Gini Mean Difference.'), ('MSV', 'MSV:  Semi Standard Deviation.'), ('FLPM', 'FLPM:  First Lower Partial Moment (Omega Ratio).'), ('SLPM', 'SLPM:  Second Lower Partial Moment (Sortino Ratio).'), ('CVaR', 'CVaR:  Conditional Value at Risk.'), ('TG', 'TG:  Tail Gini.'), ('EVaR', 'EVaR:  Entropic Value at Risk.'), ('WR', 'WR:  Worst Realization (Minimax).'), (
        'RG', 'RG:  Range of returns.'), ('CVRG', 'CVRG:  CVaR range of returns.'), ('TGRG', 'TGRG:  Tail Gini range of returns.'), ('MDD', 'MDD:  Maximum Drawdown of uncompounded cumulative returns (Calmar Ratio).'), ('ADD', 'ADD:  Average Drawdown of uncompounded cumulative returns.'), ('CDaR', 'CDaR:  Conditional Drawdown at Risk of uncompounded cumulative returns.'), ('EDaR', 'EDaR:  Entropic Drawdown at Risk of uncompounded cumulative returns.'), ('UCI', 'UCI:  Ulcer Index of uncompounded cumulative returns.')])
    obj = SelectField("Please select Objective Function", choices=[('MinRisk', 'MinRisk:  Minimize the selected risk measure.'), ('Utility', 'Utility:  Maximize the Utility function 𝜇𝑤−𝑙𝜙𝑖(𝑤)μw−lϕi(w).'), (
        'Sharpe', 'Sharpe:  Maximize the risk adjusted return ratio based on the selected risk measure.'), ('MaxRet', 'MaxRet:  Maximize the expected return of the portfolio.')])
    submit = SubmitField('Submit')


def checkfunc(stocks, stdt, eddt):
    price_data = yf.download(stocks, start=stdt, end=eddt)
    price_data = price_data.loc[:, 'Adj Close']
    stock = price_data.columns
    stock_returns = price_data[stock].pct_change().dropna()
    return stock_returns


@app.route('/', methods=['GET', 'POST'])
def index():
    form = stockinfo()
    if form.validate_on_submit():
        session['scrips'] = form.scrips.data
        session['stdt'] = form.stdt.data
        session['eddt'] = form.eddt.data
        session['model'] = form.model.data
        session['rm'] = form.rm.data
        session['obj'] = form.obj.data
        scrip_check = (list(session['scrips'].split(",")))
        stock_table = checkfunc(scrip_check, session['stdt'], session['eddt'])
        my_portfolio = rp.Portfolio(returns=stock_table)
        my_portfolio.assets_stats(method_mu='hist', method_cov='hist', d=0.94)
        stock_weights = my_portfolio.optimization(
            model=session['model'], rm=session['rm'], obj=session['obj'], hist=True)*100
        stock_weights.weights.astype(str)
        stock_weights = stock_weights.round(2)
        stock_weights.reset_index(inplace=True)
        stock_weights.weights.astype(str)
        stock_weights.columns = ['Stock', 'Weights(%)']
        stock_weights = stock_weights.round(2)
        stock_weights = pd.DataFrame(stock_weights)
        header_list = list(stock_weights.columns.values)
        stock_data = stock_weights.values
        return render_template('thankyou.html', header_list=header_list, stock_data=stock_data)
    return render_template('index.html', form=form)


@ app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
