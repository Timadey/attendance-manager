#!/usr/bin/python3
"""
user module
"""

from base_model import BaseModel, Base, Column, String


class User(BaseModel, Base):
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

    def __init__(self, name, email, password, **kwargs):
        """Initialize an user"""
        super().__init__(**kwargs)
        self.name = name
        self._email = email
        self._password = password

    @property
    def email(self):
        """Return the user email
        """
        return self._email

    @email.setter
    def email(self, email):
        if type(email) != str:
            raise TypeError("Email must be a string")

    @property
    def password(self):
        """Get user password
        """
        return self._password

    @password.setter
    def password(self, password):
        if type(password) != str:
            raise TypeError("Password must be a string")
        self._password = password
