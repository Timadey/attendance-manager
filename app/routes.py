#!/usr/bin/env python3

from app import app, db
from app.forms import DepartmentForm, MemberForm, MeetingForm, AttendanceForm
from models import Department, Organisation, Member, Meeting, attendance
from flask import redirect, request, flash, url_for, render_template
from sqlalchemy import insert, select


app.app_context().push()

org_id = '94f3eb84-8e11-456b-8ca9-50060d0aac21'  # Will be Stored as cookie
meet_id = '5ba4e709-f211-4b0f-be56-9571e7abaf10'  # Will be Stored as cookie
org = Organisation.get('94f3eb84-8e11-456b-8ca9-50060d0aac21')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', form=AttendanceForm())


@app.route('/departments', methods=['GET', 'POST'])
def departments():
    """
    Get all departments in the organisation or ad a new department
    """
    # depts = Department.query.all()
    form = DepartmentForm()
    if form.validate_on_submit():
        name = form.name.data
        dept = Department(name, organisation_id=org_id)
        dept.save()
        flash(f"New Department added: {dept.name}")
        return redirect(url_for('departments'))
    depts = Organisation.get(org_id).departments
    departments = [dept.to_dict() for dept in depts]
    return render_template('departments.html', form=form, departments=departments)


@app.route('/departments/<string:id>', methods=['GET', 'POST'])
def department(id: str):
    """Get a department with the given id
    Post a new member to the department
    """
    dept = db.session.query(Department).filter(
        Department.id == id and Organisation.id == org_id).order_by(Department.date_added).one()
    print(dept.members)
    form = MemberForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        new_member = Member(name, email, 'password', organisation_id=org_id)
        from datetime import datetime
        new_member.code = str(datetime.now())[20:]
        dept.members.append(new_member)
        dept.save()
        flash(f'New member: {new_member.name} added to {dept.name}')
        return redirect(f"{url_for('departments')}/{dept.id}")
    return render_template('department.html', form=form, department=dept.to_dict())


@app.route('/meetings', methods=['GET', 'POST'])
def meetings():
    """Get the meetings in the organisations and add new meetings
    """
    form = MeetingForm()
    if form.validate_on_submit():
        name = form.name.data
        new_meeting = Meeting(name=name, organisation_id=org_id)
        new_meeting.save()
        flash('New meeting added')
        return redirect(url_for('departments'))
    meetings = Organisation.get(org_id).meetings
    return render_template('meetings.html', meetings=[me.to_dict() for me in meetings], form=form)


@app.route('/attendance/mark', methods=['POST'])
@app.route('/attendance/mark/<string:code>', methods=['POST'])
def mark_attendance(code: str = None):
    """Mark attendance for the member with the code `code`
    """
    form = AttendanceForm(code=code)
    if form.validate_on_submit() or code is not None:
        member = Member.query.filter_by(code=code or form.code.data).one()
        if not member:
            flash('Member does not exist!')
            return redirect(url_for('index'))
        att = insert(attendance).values(
            member_id=member.id, meeting_id=meet_id)
        res = db.session.execute(att)
        if res:
            # db.session.add(attendance)
            # db.session.commit()
            flash(f'Attendance marked for: {member.name}')
        else:
            flash(f"Couldn't mark attendance. Internal Error!")
        return redirect(url_for('index'))


@app.route('/attendance', methods=['GET'])
def attendances():
    """All the attendance of every meeting with
    """
    stmt = select('attendance').where(organisation_id=org_id)
    att = db.session.execute(stmt)
    return att

    # @app.route('/departments/new', methods=['GET', 'POST'])
    # def add_department():
    #     """
    #     Add new department to the organisation
    #     """
    #     form = DepartmentForm()
    #     if form.validate_on_submit():
    #         name = form.name.data
    #         dept = Department(name, organisation_id=org_id)
    #         dept.save()
    #         flash(f"New Department added: {dept.name}")
    #         return redirect(url_for('index'))
    #     return render_template('department_new.html', title='New Department', form=form)
