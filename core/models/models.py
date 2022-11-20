# -*- coding: utf-8 -*-
# @Time    : 25.06.21 10:54
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : models.py
# @Software: PyCharm
from db import db


import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    organization = db.Column(db.String(40), nullable=False)
    role = db.Column(db.String(300), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
