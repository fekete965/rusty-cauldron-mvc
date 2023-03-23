import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from constants import RUSTY_CAULDRON_KEY
from utils.main import get_database_path

# Init the application
App = Flask(__name__)

# Check for RUSTY_CAULDRON_KEY
if not os.environ[RUSTY_CAULDRON_KEY]:
	raise Exception(f"{RUSTY_CAULDRON_KEY} must be defined in your environment!")

# Set our secret key
App.secret_key = os.environ[RUSTY_CAULDRON_KEY]

# Get the database's path
database_path = get_database_path()

# Bind the necessary SQL Alchemy values to the application
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Connect to the database
db = SQLAlchemy(App)

import routes
