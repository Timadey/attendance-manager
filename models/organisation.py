#!/usr/bin/python3
"""
Organisation module
"""

from base_model import BaseModel
from services.validations import validate_email, validate_password

class Organisation(BaseModel):
    """
    An organisations consist of maany departments and members
    Attributes:
        name: string: Name of the organisation
        email: string: Email of the organisation
        password: string: Password of organisation
    Methods:
        departments: List[Department]: List of departments in the organisation
        members: List[Member]: List of all members in the organisation
    """
    
    def __init__(self, name, email, password **kwargs):
        """Initialize an organisation"""
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self._password = password
    
    @email.setter
    def email(self, email):
        try:
            self.email = validate_email(email)
        except ValidationError as err:
            print(err)
            throw

    @password.setter
    def password(self, password):
        try:
            self._password = validate_password(password)
        except ValidationError as err:
            print(err)
            throw
    
