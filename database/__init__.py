#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from app import app
from app.config import Config

app.config_from_object(Config)

db = SQLAlchemy()
db.init_app(app)
