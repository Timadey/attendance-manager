#!/usr/bin/env python3

from app import app
from app import routes
import flask
import os

if __name__ == "__main__":
    os.environ['FLASK_APP'] = 'web.py'
    flask.run(app)