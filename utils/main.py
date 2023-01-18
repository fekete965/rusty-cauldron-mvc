import datetime
import os
from string import punctuation

from constants import MIN_PASSWORD_LENGTH, ROUTES


def is_url_safe(url: str):
    return url in ROUTES


def get_database_path():
    return os.path.join(os.getcwd(), "rusty-cauldron.db")


def get_timestamp():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


def has_upper(string: str):
    return any(c.isupper() for c in string)


def has_digit(string: str):
    return any(c.isdigit() for c in string)


def has_symbol(string: str):
    punctuations = set(punctuation)
    return any(c in punctuations for c in string)


def is_password_applicable(password: str):
    """Password has to contain:
        - at least 1 uppercase character
        - at least 1 digit
        - at least 1 special character
    """

    return has_upper(password) and has_digit(password) and has_symbol(password)


def validate_password(password: str, confirmation: str):
    if not password:
        return "Password field is required"
    if len(password) < MIN_PASSWORD_LENGTH:
        return f"Password has to be at least {MIN_PASSWORD_LENGTH} long"
    if password != confirmation:
        return "The passwords aren't match"
    if not is_password_applicable(password):
        return "The password has to contain at least 1 uppercase character, a number and a speacial character"

    return None
