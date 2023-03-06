#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class DepartmentForm(FlaskForm):
    name = StringField('Department Name')
    submit = SubmitField('Save')


class MemberForm(FlaskForm):
    name = StringField('Member Name')
    email = StringField('Email')
    submit = SubmitField('Add')


class MeetingForm(FlaskForm):
    name = StringField('Meeting name')
    desc = TextAreaField('Description')
    submit = SubmitField('Add Meeting')


class AttendanceForm(FlaskForm):
    code = StringField(
        'Member Code', description='Enter unique code for member')
    submit = SubmitField('Mark Attendance')
