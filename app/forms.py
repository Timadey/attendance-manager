#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtfforms import StringField


class DepartmentForm(FlaskForm):
    name = StringField(