#!/usr/bin/python3
"""
This module contains the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    The BaseModel class consist of methods that are similar to all models that inherits it
    Attributes:
        id: a uniquely generated id
        dateadded: the date this model was created
        datemodified: the date this model was modified
    """
    def __init__(self, **kwargs):
        """Initializes the model
        """
        if not kwargs:
            self.id = str(uuid4())
            self.dateadded = datetime.now()
            self.datemodified = self.dateadded
        else:
            if "id" not in kwargs.keys():
                setattr(self, 'id', str(uuid4()))

            for key, value in kwargs.items():
                if key == 'dateadded' or key == 'datemodified':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
    
    def __str__(self):
        """Return a string representation of the model
        """
        return f"[{type(self).__name__}] ({self.id}) {self.to_dict()}"
    
    def __repr__(self):
        """Return official representation of model"""
        return  f"{type(self).__name__}(**{self.to_dict()})"
    
    def to_dict(self):
        """Return dictionary representation of the model
        """
        model_dict = self.__dict__.copy()
        model_dict['dateadded'] = model_dict['dateadded'].isoformat()
        model_dict['datemodified'] = model_dict['datemodified'].isoformat()
        model_dict['__class__'] = type(self).__name__
        return model_dict