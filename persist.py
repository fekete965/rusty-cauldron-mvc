from flask_sqlalchemy import SQLAlchemy

from app import App

dbName = './database/rusty-cauldron.db'
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbName
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(App)
