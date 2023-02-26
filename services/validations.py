#!/usr/bin/python3

"""This modules contains all functions required to validate user's input
"""

import re


class ValidationError(Exception):
    """ValidationError raised if some values does not conform to a specification.
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def validate_email(email: str) -> str:
    """Validate an email
    Email is valid if it is of the format<abc123@email.com>
    Throws:
        ValidateError: if email is not Valid
    Returns:
        email: string: if email is Valid
    """
    format = re.compile(r'^[A-Za-z0-9]+@[a-z]+\.[a-z]{2,4}$')
    r_email = format.match(email)
    if r_email is None:
        raise ValidationError('Email is not in valid format')
    return r_email


def validate_password(password: str) -> str:
    """Validate a password
    Password must be 8 character long
    Contains at least 1 uppercase, 1 digit and a special character
    Throws:
        ValidateError: if password is not Valid
    Returns:
        password: string: if password is Valid
    """
    pass
