# -*- coding: utf-8 -*-
# @Time    : 11.06.21 10:48
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : audit.py
# @Software: PyCharm
from flask_restful import Resource
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs

class AuditConsent(MethodResource, Resource):
    @doc(description='All consent information.', tags=['Audit'])
    def get(self, consent_id):
        pass
