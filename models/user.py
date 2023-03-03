#!/usr/bin/python3
"""
user module
"""

from models.base_model import BaseModel, Column, String


class User(BaseModel):
    """
    An User of the system. Either an organisation or a member of an organisation
    Attributes:
        name: string: Name of the user
        email: string: Email of the user
        password: string: Password of user
    """
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    def __init__(self, name, email, **kwargs):
        """Initialize department"""
        super().__init__(**kwargs)
        self.name = name
