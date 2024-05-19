#!/usr/bin/python3
'''Flask web app'''
from flask import Flask


app = Flask(__name__)
'''app instance'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''home'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''c page'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''python page'''
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
