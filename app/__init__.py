from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.resources.home import Home


from instance.config import app_config
db = SQLAlchemy()


def create_app(config_name):

    from app.models import User
    from app.auth.routes import RegistrationView, LoginView

    app = Flask(__name__)

    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    api = Api(app)

    api.add_resource(Home, '/')
    api.add_resource(RegistrationView, '/auth/register')
    api.add_resource(LoginView, '/auth/login')
    return app
