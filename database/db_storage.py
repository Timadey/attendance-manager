#!/usr/bin/python3

"""DB storage module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

from models.base_model import BaseModel, Base
from models.user import User
from models.organisation import Organisation
from models.department import Department
from models.member import Member


class DBStorage():
    """
    Database Engine

    Make a connection with the mysql database. The folowing must be set \
        as environment variables
    * AM_MYSQL_USER: Mysql user with the right privilege to database
    * AM_MYSQL_PWD: Mysql password of the user
    * AM_MYSQL_HOST: The host of the database, default is localhost
    * AM_MYSQL_DB: The name of the database
    """
    __engine = None
    __session = None
    models = {
        'Organisation': Organisation,
        'Department': Department,
        'Member': Member,
    }

    @property
    def session(self):
        return self.__session

    def __init__(self) -> None:
        """
        Initiate engine
        """
        user = getenv('AM_MYSQL_USER')
        pwd = getenv('AM_MYSQL_PWD')
        host = getenv('AM_MYSQL_HOST', 'localhost')
        db = getenv('AM_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

    def boot(self):
        """Create all tables and start a new database session
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    # def all(self, models: list = []):
    #     """Get one or all models
    #     """
    #     obj = {}
    #     if len(models) > 0:
    #         for model in models:
    #             model_obj = self.models.get(model)
    #             obj[model] +=
