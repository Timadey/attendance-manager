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
    hash_password = Column(String(128), nullable=False, default='password')

    def __init__(self, name, email, password, **kwargs):
        """Initialize department"""
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.hash_password = password

    # @property
    # def hash_password(self):
    #     """User password is hashed before setting the attribute.
    #     Only the hashed password is visible
    #     """
    #     return self.hash_password

    # @hash_password.setter
    # def hash_password(self, pwd):
    #     # hash user password later
    #     self.hash_password = pwd
