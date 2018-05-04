from app import db
from flask_bcrypt import Bcrypt
from flask import current_app
import jwt
from datetime import datetime, timedelta


class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        """Initialize the user with an email and a password."""
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        """
        Checks the password against it's hash to validates the user's password
        """
        return Bcrypt().check_password_hash(self.password, password)

    def save(self):
        """Save a user to the database.
        This includes creating a new user and editing one.
        """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def generate_token(user_id):
        """Generates the access token to be used as the Authorization header"""

        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            jwt_string = jwt.encode(
                payload,
                current_app.config.get('SECRET'),
                algorithm='HS256'
            )
            return jwt_string

        except Exception as e:
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decode the access token from the Authorization header."""
        try:
            payload = jwt.decode(token, current_app.config.get('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Expired token. Please log in to get a new token"
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"


class PIPModel(db.Model):
    """This class defines the PIP table."""

    __tablename__ = 'pips'

    id = db.Column(db.Integer, primary_key=True)
    fellow = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255))
    fellow_class = db.Column(db.Integer)
    manager = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    people_rep = db.Column(db.String(255))
    status = db.Column(db.String(255))
    start_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def __init__(self, fellow, manager):
        """Initialize the PIP with fellow and his/her manager."""
        self.fellow = fellow
        self.manager = manager

    def save(self):
        """Save a PIP."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_pip(fellow):
        """This method gets all the PIP for a given fellow."""
        return PIPModel.query.filter_by(fellow=fellow)

    @staticmethod
    def all():
        return PIPModel.query.all()

    def delete(self):
        """Deletes a given PIP."""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Return a representation of a PIP instance."""
        return "<Bucketlist: {}>".format(self.name)
