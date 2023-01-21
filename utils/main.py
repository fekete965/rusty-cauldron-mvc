import datetime
import os
from string import punctuation

from constants import COOKING_MEASUREMENT, MIN_PASSWORD_LENGTH, ROUTES


def is_url_safe(url: str):
    """Validates the url"""
    return url in ROUTES.list()


def get_database_path():
    """Returns the databse file's path"""
    return os.path.join(os.getcwd(), "rusty-cauldron.db")


def get_timestamp():
    """Return the current time in a friendly format"""
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


def has_upper(string: str):
    """Check if string contains an uppercase character"""
    return any(c.isupper() for c in string)


def has_digit(string: str):
    """Check if string contains a digit"""
    return any(c.isdigit() for c in string)


def has_symbol(string: str):
    """Check if string contains a symbol"""
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
    """Check if the passwors meets every rules"""
    if len(password) < MIN_PASSWORD_LENGTH:
        return f"Password has to be at least {MIN_PASSWORD_LENGTH} long"
    if password != confirmation:
        return "The passwords aren't match"
    if not is_password_applicable(password):
        return "The password has to contain at least 1 uppercase character, a number and a speacial character"

    return None


def validateIngredients(ingredient_list: list[dict]):
    """If any of them is invalid, return an error message"""

    for ingredient in ingredient_list:
        name = ingredient.get("name")
        amount = ingredient.get("amount")
        measurement = ingredient.get("measurement")
        
        if not name or not amount or not measurement:
            return "Name, amount and measurements are required for any ingredients"
        
        if not measurement in COOKING_MEASUREMENT.list():
            return "Invald measurment type"
        
    return None
