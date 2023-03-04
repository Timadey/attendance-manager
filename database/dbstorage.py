#!/usr/bin/python3

"""DB storage module
"""

from app import db


class DBStorage():
    """Implement most actions done with db
    """

    def save(self, obj):
        """
        Save the current object to database
        """
        db.session.add(obj)
        db.session.commit()
        # Log success

    def all(self, obj) -> list:
        """Get all `obj` in the database
        """
        return obj.query.all()

    def get(self, obj, id: str):
        """Get the `obj` with `id` from the database
        """
        return db.session.get(obj, id)
