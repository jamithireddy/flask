from crypt import methods
import pandas as pd
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
    method_mu = RadioField("Please select Method_MU", choices=[('hist', 'hist: Use Historical estimates'), (
        'ewma1', 'Use EWMA with adjust=True'), ('ewma2', 'Use EWMA with adjust=False')])
    method_cov = SelectField("Please select Method_COV", choices=[('hist', 'hist:  Use historical estimates'), ('ewma1', 'ewma1:  Use ewma with adjust=True'), ('ewma2', 'ewma2:  Use ewma with adjust=False'), ('ledoit', 'ledoit:  Use the Ledoit and Wolf Shrinkage method'), ('oas', 'oas:  Use the Oracle Approximation Shrinkage method'), ('shrunk', 'shrunk:  Use the basic Shrunk Covariance method'), (
        'gl', 'gl:  Use the basic Graphical Lasso Covariance method'), ('jlogo', 'jlogo:  Use the j-LoGo Covariance method'), ('fixed', 'fixed:  De-noise using fixed method'), ('spectral', 'spectral:  De-noise using spectral method'), ('shrink', 'shrink:  De-noise using shrink method'), ('gerber1', 'gerber1:  Use the Gerber statistic 1'), ('gerber2', 'gerber2:  Use the Gerber statistic 2')])
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
        session['method_mu'] = form.method_mu.data
        session['method_cov'] = form.method_cov.data
        scrip_check = (list(session['scrips'].split(",")))
        stock_table = checkfunc(scrip_check, session['stdt'], session['eddt'])
        stock_table = stock_table.round(decimals=4)
        stock_table.reset_index(inplace=True)
        stock_table['Date'] = stock_table['Date'].dt.date
        header_list = list(stock_table.columns.values)
        stock_data = stock_table.values
        # return redirect(url_for('thankyou'))
        return render_template('thankyou.html', header_list=header_list, stock_data=stock_data)
    return render_template('index.html', form=form)


@ app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
