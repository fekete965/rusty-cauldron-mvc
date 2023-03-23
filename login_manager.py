from flask_login import LoginManager

from app import App
from tables.users import User


# Setup login manager
login_manager = LoginManager()
login_manager.init_app(App)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
