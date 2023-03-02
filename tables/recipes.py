from persist import db


class Recipe(db.Model):
    __tablename__= "recipes"

    _id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column("title", db.String(100), nullable=False)
    prep_time = db.Column("prep_time", db.Integer, nullable=True)
    cooking_time = db.Column("cooking_time", db.Integer, nullable=False)
    description = db.Column("description", db.String(255), nullable=False)
    deleted = db.Column("deleted", db.Boolean, nullable=False)
    created_at = db.Column("created_at", db.String(100), nullable=False)
    updated_at = db.Column("updated_at", db.String(100), nullable=False)

    def __init__(self, user_id, title, prep_time, cooking_time, description, deleted, created_at, updated_at):
        self.user_id = user_id
        self.title = title
        self.prep_time = prep_time
        self.cooking_time = cooking_time
        self.description = description
        self.deleted = deleted
        self.created_at = created_at
        self.updated_at = updated_at
