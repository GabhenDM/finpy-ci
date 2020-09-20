from app import app
from markupsafe import escape
import requests
from flask import jsonify



@app.route('/stocks/price/<ticker>')
def show_stock_price(ticker):
    stock_ticker = escape(ticker)
    string = '{}/quote?symbol={}&token={}'.format(app.config["API_URL"],stock_ticker,app.config['API_KEY'])
    r = requests.get(string)
    if r.status_code == requests.codes.ok:
        return r.json(), 200

@app.route('/stocks/news/<ticker>')
def show_stock_news(ticker):
    stock_ticker = escape(ticker)
    string = '{}company-news?symbol={}&from=2020-04-30&to=2020-05-01&token={}'.format(app.config["API_URL"],stock_ticker,app.config['API_KEY'])
    r = requests.get(string)
    if r.status_code == requests.codes.ok:
        return r.json(), 200

@app.route('/stocks/profile/<ticker>')
def show_profile(ticker):
    stock_ticker = escape(ticker)
    string = '{}stock/profile2?symbol={}&token={}'.format(app.config["API_URL"],stock_ticker,app.config['API_KEY'])
    r = requests.get(string)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return jsonify({'message': 'Unknown error'}), 500
    