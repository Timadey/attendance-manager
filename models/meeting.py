#!/usr/bin/python3

"""Meeting module
"""

from app import db
from models import BaseModel
from sqlalchemy import Table, DateTime, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime


attendance = Table('attendance', db.metadata,
                   Column('organisation_id', ForeignKey('organisations.id'),
                          nullable=False),
                   Column('member_id', ForeignKey('members.id'),
                          nullable=False, primary_key=True),
                   Column('meeting_id', ForeignKey('meetings.id'),
                          nullable=False, primary_key=True),
                   Column('date_added', DateTime,
                          nullable=False, default=datetime.now())
                   )


class Meeting(BaseModel, db.Model):
    """A meeting model
    Attributes
        name: Name of the meeting
        can_attend: Members that can attend this meeting
        members: Members that have attended this meeting
    """
    __tablename__ = 'meetings'
    organisation_id = Column(String(60), ForeignKey(
        'organisations.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(255), nullable=True)
    members = relationship('Member', secondary='attendance',
                           back_populates='meetings', viewonly=False)
