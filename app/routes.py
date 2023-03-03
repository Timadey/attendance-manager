#!/usr/bin/env python3

from app import app, db
from models import Department

@app.route('/')
def index():
    return 'Hello world'

@app.route('/departments', methods=['GET'])
def departments():
    """
    GET all departments
    """
    depts = Department.query.all()
    return {'departments': [dept.to_dict() for dept in depts]}


