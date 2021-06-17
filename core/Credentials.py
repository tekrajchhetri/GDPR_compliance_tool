# -*- coding: utf-8 -*-
# @Time    : 12.05.21 15:24
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : Credentials.py
# @Software: PyCharm
import os
from flask import request, jsonify
from functools import wraps
import jwt


class Credentials:
    def get_username(self):
        return os.environ.get("USERNAME")

    def get_password(self):
        return os.environ.get("PASSWORD")
    # check token

    def check_for_token(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missed'})
            try:
                # remove bearer keyword and a space
                token = token[7:]
                data = jwt.decode(token, os.getenv('SECRET_KEY'))
            except:
                return jsonify({'message': 'invalid token'})
            return func(*args, **kwargs)
        return wrapped
