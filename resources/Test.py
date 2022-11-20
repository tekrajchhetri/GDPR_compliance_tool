# -*- coding: utf-8 -*-
# @Time    : 10.05.21 21:02
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : Test.py
# @Software: PyCharm


from flask_restful import Resource


class Test(Resource):
    def get(self):
        return {"status": "SUCCESS", "admin": "tekraj.chhetri@sti2.at"}
