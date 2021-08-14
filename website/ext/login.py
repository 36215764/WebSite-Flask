from flask_login import LoginManager
from flask import Flask
from website.models import User

login_manager = LoginManager()

def init_app(app: Flask):
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))