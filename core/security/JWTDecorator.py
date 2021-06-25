# -*- coding: utf-8 -*-
# @Time    : 25.06.21 11:48
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : JWTDecorator.py
# @Software: PyCharm

from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from flask import jsonify
from functools import wraps



def luh_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_authorised_for_endpoint"] == 2040:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Unauthorized"), 403

        return decorator

    return wrapper

def spm_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_authorised_for_endpoint"] == 2020:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Unauthorized"), 403

        return decorator

    return wrapper


def ccc_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_authorised_for_endpoint"] == 3030:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Unauthorized"), 403

        return decorator

    return wrapper
