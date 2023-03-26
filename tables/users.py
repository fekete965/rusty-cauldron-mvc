from flask_login import UserMixin
from app import db
from utils.main import get_timestamp


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    _id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100), nullable=False)
    last_name = db.Column("last_name", db.String(100), nullable=True)
    email = db.Column("email", db.String(255), unique=True, nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    deleted = db.Column("deleted", db.Boolean, nullable=False, default=False)
    created_at = db.Column("created_at", db.DateTime, nullable=False, default=get_timestamp())
    updated_at = db.Column("updated_at", db.DateTime, nullable=False, default=get_timestamp())

    def __init__(self, first_name, last_name, email, password, deleted=False, created_at=get_timestamp(), updated_at=get_timestamp()):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.deleted = deleted
        self.created_at = created_at
        self.updated_at = updated_at

    def get_id(self):
        return self._id
