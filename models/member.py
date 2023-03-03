#!/usr/bin/python3

"""Members of an organisation
"""
from models.user import User, Column, String
from app import db

from sqlalchemy import ForeignKey


class Member(User, db.Model):
    """Members of an organisation
    """
    __tablename__ = 'members'
    organisation_id = Column(String(60), ForeignKey(
        'organisations.id'), nullable=False)
    department_id = Column(String(60), ForeignKey(
        'departments.id'), nullable=False)
