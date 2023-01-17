import os

from constants import ROUTES

def isUrlSafe(url):
    return url in ROUTES

def getDatabasePath():
    return os.path.join(os.getcwd(), "rusty-cauldron.db")
