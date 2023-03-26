from sqlalchemy import func
from app import db


class Ingredient(db.Model):
    __tablename__= "ingredients"

    _id = db.Column("id", db.Integer, primary_key=True)
    recipe_id = db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    name = db.Column("name", db.String(100), nullable=False)
    amount = db.Column("amount", db.Float, nullable=False)
    measurement = db.Column("measurement", db.String(50), nullable=False)
    created_at = db.Column("created_at", db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column("updated_at", db.DateTime, nullable=False, default=func.now())

    def __init__(self, recipe_id, name, amount, measurement, created_at=func.now(), updated_at=func.now()):
        self.recipe_id = recipe_id
        self.name = name
        self.amount = amount
        self.measurement = measurement
        self.created_at = created_at
        self.updated_at = updated_at
