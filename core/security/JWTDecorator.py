# -*- coding: utf-8 -*-
# @Time    : 25.06.21 11:48
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : JWTDecorator.py
# @Software: PyCharm

from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from functools import wraps
from core.smashHitmessages import smashHitmessages
from core.storage.JWTUser import JWTUser

sm = smashHitmessages()
jwtuser = JWTUser()
def luh_required(optional=False, fresh=False, refresh=False, locations=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(optional, fresh, refresh, locations)
                claims = get_jwt()
                isValid = jwtuser.get_hex_data(claims["is_authorised_for_endpoint"])
                if isValid != 0 and isValid["organisation"] == "LUH":
                    return fn(*args, **kwargs)
                else:
                    return sm.jwt_invalid_message(), 403
            except:
                return sm.token_expired(), 403

        return decorator

    return wrapper
# internal act
def spm_required(optional=False, fresh=False, refresh=False, locations=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:

                verify_jwt_in_request(optional, fresh, refresh, locations)
                claims = get_jwt()
                isValid = jwtuser.get_hex_data(claims["is_authorised_for_endpoint"])
                if isValid != 0 and isValid["organisation"] == "SPC":
                    return fn(*args, **kwargs)
                else:
                    return sm.jwt_invalid_message(), 403
            except:
                return sm.token_expired(), 403

        return decorator

    return wrapper

# this is for ATOS
def ccc_required(optional=False, fresh=False, refresh=False, locations=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(optional, fresh, refresh, locations)
                claims = get_jwt()
                isValid = jwtuser.get_hex_data(claims["is_authorised_for_endpoint"])
                if isValid != 0 and isValid["organisation"] == "CCC":
                    return fn(*args, **kwargs)
                else:
                    return sm.jwt_invalid_message(), 403
            except:
                return sm.token_expired(), 403

        return decorator

    return wrapper


def access_to_all(optional=False, fresh=False, refresh=False, locations=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(optional, fresh, refresh, locations)
                claims = get_jwt()
                isValid = jwtuser.get_hex_data(claims["is_authorised_for_endpoint"])
                if isValid != 0:
                    return fn(*args, **kwargs)
                else:
                    return sm.jwt_invalid_message(), 403
            except:
                return sm.token_expired(), 403

        return decorator

    return wrapper
