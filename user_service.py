from tables.users import User
from app import db

class UserService():
    def get_user_by_email(email):
        return User.query.filter(User.email == email).first()

    def create_user(first_name, last_name, email, password):
        newUser = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(newUser)
        db.session.commit()

        return newUser
