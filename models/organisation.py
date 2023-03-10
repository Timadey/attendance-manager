#!/usr/bin/python3
"""
Organisation module
"""
from app import db
from models.user import User
from sqlalchemy.orm import relationship


class Organisation(User, db.Model):
    """
    An organisations consist of maany departments and members
    Attributes:
        name: string: Name of the organisation
        email: string: Email of the organisation
        password: string: Password of organisation
        departments: List[Department]: List of departments in the organisation
        members: List[Member]: List of all members in the organisation
    """
    __tablename__ = 'organisations'
    members = relationship('Member', backref='organisation',
                           cascade='all, delete-orphan')
    departments = relationship('Department', cascade='all, delete-orphan')
    meetings = relationship('Meeting', cascade='all, delete-orphan')
