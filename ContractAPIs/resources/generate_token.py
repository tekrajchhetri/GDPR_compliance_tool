import os
from flask_restful import Resource,request
from flask_apispec.views import MethodResource
from flask import jsonify
from functools import wraps
import jwt
import datetime
class GenerateToken(MethodResource,Resource):
    # check username and password
    def check_for_username_password(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            username=os.getenv('user_name')
            password=os.getenv('password')
            secret_key=os.getenv('SECRET_KEY')

          
            if request.authorization and request.authorization.username and request.authorization.password:
                if request.authorization.username==username and request.authorization.password==password:
                    token=jwt.encode({
                        'username':username,
                        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=15)
                    },secret_key)
                    return jsonify({'token' : token.decode('utf-8')})
                else:
                    return 'username or password is not correct'
            elif request.headers.get('username') and request.headers.get('password'):
                if request.headers.get('username')==username and request.headers.get('password')==password:
                    token=jwt.encode({
                        'username':username,
                        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=15)
                    },secret_key)
                    return jsonify({'token' : token.decode('utf-8')})
                else:
                    return 'username or password is not correct'                
            else:
                return 'Basic authentication is required.'    
        return wrapped
    @check_for_username_password    
    def get(self):
        return True
