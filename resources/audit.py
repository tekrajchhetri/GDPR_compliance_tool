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
from core.audit.Audit import  Audit
import json

class ReturnSchemaaudit(Schema):
    act_status_code = fields.Integer(required=True)
    decision = fields.String(required=True)
    decision_token = fields.String(required=True)
    message = fields.String(optional=True)
    timestamp = fields.String(required=True)

class AuditConsent(MethodResource, Resource):
    @doc(description='AuditConsent.', tags=['Audit'])
    @marshal_with(ReturnSchemaaudit)
    def get(self, consent_id, level_of_details):
        auditInstance = Audit()
        response = auditInstance.audit__consent(consent_id=consent_id,
                                                         level_of_details=level_of_details
                                                         )

        return response


class  AuditDataProvider(MethodResource, Resource):
    @doc(description="Audit consent by data provider",tags=['Audit'])
    @marshal_with(ReturnSchemaaudit)
    def get(self, data_provider_id, level_of_details):
        auditInstance = Audit()
        response = auditInstance.audit_all_consent_by_dp(data_provider_id=data_provider_id,
                                                         level_of_details=level_of_details
                                                         )

        return response




