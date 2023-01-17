from flask_sqlalchemy import SQLAlchemy

from app import App
from utils.main import getDatabasePath

# Get the database's path
databasePath = getDatabasePath()

# Bind the necessary SQL Alchemy values to the application
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + databasePath
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Connect to the database
db = SQLAlchemy(App)
