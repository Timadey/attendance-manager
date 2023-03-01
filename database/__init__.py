#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from app import app
from os import getenv

user = getenv('AM_MYSQL_USER')
pwd = getenv('AM_MYSQL_PWD')
host = getenv('AM_MYSQL_HOST', 'localhost')
db = getenv('AM_MYSQL_DB')

app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+mysqldb://{user}:{pwd}@{host}/{db}'
db = SQLAlchemy()
db.init_app(app)
