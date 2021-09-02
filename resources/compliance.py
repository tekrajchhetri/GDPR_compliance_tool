# -*- coding: utf-8 -*-
# @Time    : 23.08.21 17:45
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : compliance.py
# @Software: PyCharm


# -*- coding: utf-8 -*-
# @Time    : 12.05.21 14:32
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : consent.py
# @Software: PyCharm


from flask_restful import Resource, request
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields,ValidationError
from flask_apispec import marshal_with, doc, use_kwargs
from core.compliance.ComplianceEngine import  ComplianceEngine
from  core.security.JWTDecorator import ccc_required


class ComplianceReturnSchema(Schema):
    act_status_code = fields.Integer(required=True)
    decision = fields.String(required=True)
    decision_token = fields.String(required=True)
    message = fields.String(optional=True)
    timestamp = fields.String(required=True)



"""
Compliance rest endpoints
"""
class CompliancebyConsent(MethodResource, Resource):
    """Checks compliance for a single consent based on consent ID
    """
    # @ccc_required(fresh=True)
    @doc(description='Check compliance', tags=['Compliance'])
    @marshal_with(ComplianceReturnSchema)
    def get(self, consent_id):
        ce = ComplianceEngine()
        response = ce.compliance_check_act(level="consent", consentID=consent_id)
        return response

class CompliancebyDataProvider(MethodResource, Resource):
    """Checks compliance for all the active consent particular to data provider
    """
    # @ccc_required(fresh=True)
    @doc(description='Check compliance', tags=['Compliance'])
    @marshal_with(ComplianceReturnSchema)
    def get(self, data_provider_id):
        ce = ComplianceEngine()
        print(data_provider_id)
        response = ce.compliance_check_act(level="dataprovider", consentProvidedBy=data_provider_id)
        return response






