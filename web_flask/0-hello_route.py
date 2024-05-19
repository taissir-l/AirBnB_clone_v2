#!/usr/bin/python3
'''Flask web app'''
from flask import Flask


app = Flask(__name__)
'''Flask application'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
