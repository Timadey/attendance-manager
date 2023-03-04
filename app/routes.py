#!/usr/bin/env python3

from app import app, db
from app.forms import DepartmentForm
from models import Department, Organisation
from flask import redirect, request, flash, url_for, render_template

app.app_context().push()
org_id = '94f3eb84-8e11-456b-8ca9-50060d0aac21'
org = Organisation.get('94f3eb84-8e11-456b-8ca9-50060d0aac21')
# dep = Department.get()


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/departments', methods=['GET'])
def departments():
    """
    Get all departments in the organisation
    """
    # depts = Department.query.all()
    depts = org.departments
    departments = [dept.to_dict() for dept in depts]
    return render_template('departments.html', departments=departments)


@app.route('/departments/new', methods=['GET', 'POST'])
def add_department():
    """
    Add new department to the organisation
    """
    form = DepartmentForm()
    if form.validate_on_submit():
        name = form.name.data
        dept = Department(name, organisation_id=org_id)
        dept.save()
        flash(f"New Department added: {dept.name}")
        return redirect(url_for('index'))
    return render_template('department_new.html', title='New Department', form=form)
