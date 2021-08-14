from flask import Flask
import website.views as views
import website.auth as auth
import website.ext.database as database
import website.ext.login as authModule
from os import path

DB_NAME = "databse.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uaea5fsf46s5fsdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.db = database.init_db(app)

    views.init_app(app)
    auth.init_app(app)

    from .models import User, Note
    create_database(app)

    authModule.init_app(app)

    return app


def create_database(app: Flask):
    if not path.exists('website/' + DB_NAME):
        app.db.create_all(app=app)
        print('Created Database!')