#!/usr/bin/python3

"""A department
"""

from models.base_model import BaseModel, Column, String
from models.member import Member
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Department(BaseModel, db.Model):
    """A department belongs to an organisation
    Attributes:
        name: string: Name of the department
        members: List[Member]: List of all members in the department
    """
    __tablename__ = 'departments'
    name = Column(String(255), nullable=False, unique=True)
    organisation_id = Column(String(60), ForeignKey(
        'organisations.id'), nullable=False)
    members = relationship(Member, backref='departments',
                           cascade='all, delete-orphan')

    def __init__(self, name, **kwargs):
        """Initialize department"""
        super().__init__(**kwargs)
        self.name = name
