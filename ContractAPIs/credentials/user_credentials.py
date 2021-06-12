import os
from flask import current_app,request,jsonify
from functools import wraps
import jwt
class UserCredentials:
    
    def get_username(self):
        return os.getenv("user_name")

    def get_password(self):
        return os.getenv("password")

    # check token
    def check_for_token(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            token= request.headers.get('Authorization')
            if not token:
                return jsonify({'message':'Token is missed'})
            try:
                # remove bearer keyword and a space
                token=token[7:]
                data=jwt.decode(token,os.getenv('SECRET_KEY'))
            except:
                return jsonify({'message':'invalid token'})
            return func(*args,**kwargs)
        return wrapped