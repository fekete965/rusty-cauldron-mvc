from sqlalchemy import insert
from tables.users import User


class UserService():
    def get_user_by_email(email):
        return User.query.filter(User.email == email).first()

    def create_user(first_name, last_name, email, password, password_hash):
        return insert(User).values(first_name=first_name, last_name=last_name, email=email, password=password, password_hash=password_hash)
