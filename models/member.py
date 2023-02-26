#!/usr/bin/python3

"""Members of an organisation
"""

from user import User, Base, Column, String
from sqlalchemy import ForeignKey


class Member(User, Base):
    """Members of an organisation
    """
    __tablename__ = 'members'
    organisation_id = Column(String(60), ForeignKey(
        'organisations.id'), nullable=False)
    department_id = Column(String(60), ForeignKey(
        'departments.id'), nullable=False)
