#!/usr/bin/env python3

from app import app, db
from app.forms import DepartmentForm
from models import Department, Organisation


from flask import redirect, request, flash, url_for, render_template


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/departments', methods=['GET'])
def departments():
    """
    GET all departments
    """
    depts = Department.query.all()
    return {'departments': [dept.to_dict() for dept in depts]}


@app.route('/departments/new', methods=['GET', 'POST'])
def add_department():
    """
    Add new department
    """
    form = DepartmentForm()
    if form.validate_on_submit():
        name = form.name.data
        org_id = '94f3eb84-8e11-456b-8ca9-50060d0aac21'
        dept = Department(name, organisation_id=org_id)
        print(dept.name)
        dept.save()
        flash(f"New Department added: {form.name.data}")
        return redirect(url_for('index'))
    return render_template('department_new.html', title='New Department', form=form)
