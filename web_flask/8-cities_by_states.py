#!/usr/bin/python3
'''Flask web app'''
from flask import Flask, render_template

from models import storage
from models.state import State


app = Flask(__name__)
'''app instance'''
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    '''cities_by_states'''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)

    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('8-cities_by_states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''request context end event listener'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
