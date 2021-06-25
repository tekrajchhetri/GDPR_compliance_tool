# -*- coding: utf-8 -*-
# @Time    : 25.06.21 10:54
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : models.py
# @Software: PyCharm
from passlib.hash import pbkdf2_sha256 as sha256
from app import db
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    role = db.Column(db.String(120), nullable = False)
    status = db.Column(db.Integer, nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()