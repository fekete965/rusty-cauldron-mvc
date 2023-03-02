from persist import db


class User(db.Model):
    __tablename__ = 'users'

    _id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100), nullable=False)
    last_name = db.Column("last_name", db.String(100), nullable=True)
    email = db.Column("email", db.String(255), unique=True)
    password = db.Column("password", db.String(255), nullable=False)
    deleted = db.Column("deleted", db.Boolean, nullable=False)
    created_at = db.Column("created_at", db.DateTime, nullable=False)
    updated_at = db.Column("updated_at", db.DateTime, nullable=False)

    def __init__(self, first_name, last_name, email, password, deleted, created_at, updated_at):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.deleted = deleted
        self.created_at = created_at
        self.updated_at = updated_at
