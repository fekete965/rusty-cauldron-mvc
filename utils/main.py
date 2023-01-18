import datetime
import os
from string import punctuation

from constants import MIN_PASSWORD_LENGTH, ROUTES


def isUrlSafe(url: str):
    return url in ROUTES


def getDatabasePath():
    return os.path.join(os.getcwd(), "rusty-cauldron.db")


def getTimeStamp():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


def hasUpper(string: str):
    return any(c.isupper() for c in string)


def hasDigit(string: str):
    return any(c.isdigit() for c in string)


def hasSymbol(string: str):
    punctuations = set(punctuation)
    return any(c in punctuations for c in string)


def isPasswordApplicable(password: str):
    """Password has to contain:
        - at least 1 uppercase character
        - at least 1 digit
        - at least 1 special character
    """

    return hasUpper(password) and hasDigit(password) and hasSymbol(password)


def validatePassword(password: str, confirmation: str):
    if not password:
        return "Password field is required"
    if len(password) < MIN_PASSWORD_LENGTH:
        return f"Password has to be at least {MIN_PASSWORD_LENGTH} long"
    if password != confirmation:
        return "The passwords aren't match"
    if not isPasswordApplicable(password):
        return "The password has to contain at least 1 uppercase character, a number and a speacial character"

    return None
