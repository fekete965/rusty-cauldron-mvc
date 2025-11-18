from functools import wraps
from flask import redirect
from flask_login import LoginManager, current_user

from app import App
from constants import ROUTES
from tables.users import User


# Setup login manager
login_manager = LoginManager()
login_manager.init_app(App)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def unauthenticated_route(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if current_user and current_user.is_authenticated:
            return redirect(ROUTES.Home)

        return f(*args, **kwargs)

    return decorated
