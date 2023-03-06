#!/usr/bin/python3

"""Members of an organisation
"""
from models.user import User, Column, String
from sqlalchemy import Integer, ForeignKey

from sqlalchemy.orm import relationship
from app import db
from models.meeting import attendance
from datetime import datetime


class Member(User, db.Model):
    """Members of an organisation
    Attributes:
        meetings: Meetings that this member have attended
    """
    __tablename__ = 'members'
    organisation_id = Column(String(60), ForeignKey(
        'organisations.id'), nullable=False)
    department_id = Column(String(60), ForeignKey(
        'departments.id'), nullable=False)
    code = Column(String(128), nullable=False, unique=True)
    meetings = relationship('Meeting', secondary=attendance,
                            back_populates='members', viewonly=False)
