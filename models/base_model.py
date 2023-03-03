#!/usr/bin/python3
"""
This module contains the BaseModel class
"""

from uuid import uuid4
from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

# Base = declarative_base()


class BaseModel():
    """
    The BaseModel class consist of methods that are similar to all models that inherits it
    Attributes:
        id: a uniquely generated id
        dateadded: the date this model was created
        datemodified: the date this model was modified
    """
    id = Column(String(60), nullable=False, unique=True, primary_key=True)
    date_added = Column(DateTime, nullable=False, default=datetime.now())
    date_modified = Column(DateTime, nullable=False, default=date_added)

    def __init__(self, **kwargs):
        """Initializes the model
        """
        if not kwargs:
            self.id = str(uuid4())
            self.date_added = datetime.now()
            self.date_modified = self.date_added
        else:
            if "id" not in kwargs.keys():
                setattr(self, 'id', str(uuid4()))

            for key, value in kwargs.items():
                if key == 'date_added' or key == 'date_modified':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the model
        """
        return f"[{type(self).__name__}] ({self.id}) {self.to_dict()}"

    def __repr__(self):
        """Return official representation of model"""
        return f"{type(self).__name__}(**{self.to_dict()})"

    def to_dict(self):
        """Return dictionary representation of the model
        """
        model_dict = self.__dict__.copy()
        model_dict['date_added'] = model_dict['date_added'].isoformat()
        model_dict['date_modified'] = model_dict['date_modified'].isoformat()
        model_dict['__class__'] = type(self).__name__
        if '_sa_instance_state' in model_dict.keys():
            model_dict.pop('_sa_instance_state', None)
        return model_dict
