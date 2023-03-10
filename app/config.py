#!/usr/bin/env python3

"""Configuration module
"""

from dotenv import load_dotenv

load_dotenv()


class Config():
    """
    Configuration class
    """
    from os import getenv

    user = getenv('AM_MYSQL_USER')
    pwd = getenv('AM_MYSQL_PWD')
    host = getenv('AM_MYSQL_HOST', 'localhost')
    db = getenv('AM_MYSQL_DB')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{pwd}@{host}/{db}'
    SECRET_KEY = 'my-token-key'
