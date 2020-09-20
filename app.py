from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_pyfile('config.py')

from routes import stocks

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
