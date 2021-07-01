# -*- coding: utf-8 -*-
# @Time    : 25.06.21 13:36
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : JWTUser.py
# @Software: PyCharm

from core.helper.JWTHelper import JWTHelper
from core.smashHitmessages import  smashHitmessages
from werkzeug.security import generate_password_hash, check_password_hash
from core.models.models import User
from flask_jwt_extended import create_access_token
import json

class JWTUser(JWTHelper, smashHitmessages):
    def __init__(self):
        super().__init__()

    def register_user(self, username, password, organization):
        organizationCheck = self.organisation_map(organization)
        if organizationCheck > 0:
            user = User.query.filter_by(username=username).first()
            if user:
                msg =  self.processing_fail_message()
                msg["message"] = "Username exists"
                return msg
            newuser = User(username=username, password=generate_password_hash(password, method='sha256'),
                           role=organizationCheck, status=1)
            newuser.save_to_db()
            newmsg = self.insert_success()
            newmsg["decision"]="USER_REGISTERED"
            return newmsg


        else:
            return self.processing_fail_message()

    def login_user(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            additional_claims = {"is_authorised_for_endpoint":user.role}
            access_token = create_access_token(username, additional_claims=additional_claims, fresh=True)
            raccess_token = {"access_token":access_token}
            return raccess_token
        else:
           return  {"access_token": "Invalid Credentials"}, 401