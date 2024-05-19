#!/usr/bin/python3
'''Flask web app'''
from flask import Flask


app = Flask(__name__)
'''Flask app'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''home'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
