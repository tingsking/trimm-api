
from passlib.hash import pbkdf2_sha256
from tornado.options import define, options
from datetime import datetime, timedelta # TODO research timedelta
import uuid
import json

# Project Imports
from resources.helpers import PageHandler
from resources.categories import default_categories
from models.mysql import Users


class UserRegister(PageHandler):
    '''
        If data is in req body for registration `username, email, password`.
        Check if the email already exits in database.
        If email does not exist, add a new user to the db and return message
        with `auth` cookie.
    '''
    def post(self):
        if self.request.body:
            data = json.loads(self.request.body)
            email_in_db = Users.select_where('user_email', data["email"])
            if not email_in_db:
                hashed_password = pbkdf2_sha256.hash(data['password'])
                user_uuid = str(uuid.uuid4())
                default_currency = '£ - Pound Sterling'
                Users.insert_into(
                    user_uuid=user_uuid,
                    user_name=data['username'], 
                    user_email=data['email'],
                    user_currency=default_currency,
                    user_password=hashed_password)
                
                expires = datetime.utcnow() + timedelta(days=30)
                self.set_cookie('auth', user_uuid, expires=expires)
                self.json_response(
                    {'message': 'new user created and categories', 'currency': default_currency}, 201)
                default_categories(user_uuid)
            else:
                self.json_response({'message': 'this email already exists'}, 400)
        else:
            self.json_error()


class UserLogin(PageHandler):
    # TODO do this next!!!!
    pass
