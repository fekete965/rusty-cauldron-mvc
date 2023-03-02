from flask_sqlalchemy import SQLAlchemy

from app import App
from utils.main import get_database_path


# Get the database's path
database_path = get_database_path()

# Bind the necessary SQL Alchemy values to the application
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Connect to the database
db = SQLAlchemy(App)
