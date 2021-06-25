# -*- coding: utf-8 -*-
# @Time    : 25.06.21 10:54
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : models.py
# @Software: PyCharm
from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(300), nullable = False)
    role = db.Column(db.Integer, nullable = False)
    status = db.Column(db.Integer, nullable = False)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()