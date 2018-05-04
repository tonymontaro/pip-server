from flask import request
from app.models import User

from flask_restful import Resource


class RegistrationView(Resource):
    """This class-based view registers a new user."""

    def post(self):
        user = User.query.filter_by(email=request.form['email']).first()

        if not user:
            try:
                post_data = request.form
                email = post_data['email']
                password = post_data['password']
                user = User(email=email, password=password)
                user.save()

                response = {
                    'message': 'You registered successfully. Please login.',
                }
                return response, 201

            except Exception as e:
                response = {
                    'message': str(e)
                }
                return response, 401
        else:
            response = {
                'message': 'User already exists. Please login.'
            }

            return response, 202


class LoginView(Resource):
    """This class-based view handles user login and access token generation."""

    def post(self):
        try:
            user = User.query.filter_by(email=request.form['email']).first()

            if user and user.password_is_valid(request.form['password']):
                access_token = user.generate_token(user.id)
                if access_token:
                    response = {
                        'message': 'You logged in successfully.',
                        'access_token': access_token.decode()
                    }
                    return response, 200
            else:
                response = {
                    'message': 'Invalid email or password, Please try again.'
                }
                return response, 401

        except Exception as e:
            response = {
                'message': str(e)
            }
            return response, 500
