from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from server.resources.home import Home
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if os.environ["environment"] == "development":
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.Config')
db = SQLAlchemy(app)
api = Api(app)

# Routes
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True)