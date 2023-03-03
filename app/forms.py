#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class DepartmentForm(FlaskForm):
    name = StringField('Department Name')
    submit = SubmitField('Save')
    