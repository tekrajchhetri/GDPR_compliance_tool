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
import datetime

from flask_restful import Resource, request
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields,ValidationError
from flask_apispec import marshal_with, doc, use_kwargs
from core.compliance.ComplianceEngine import  ComplianceEngine
from core.compliance.ComplianceEngine import  ComplianceObligationNotification
from  core.security.JWTDecorator import ccc_required


class ComplianceReturnSchema(Schema):
    act_status_code = fields.Integer(required=True)
    decision = fields.String(required=True)
    decision_token = fields.String(required=True)
    message = fields.String(optional=True)
    timestamp = fields.String(required=True)


class ComplianceObligationSchema(Schema):
    """ JSON Schema for compliance obligation
    This JSON Schema  has to be followed by the data controller or processor to inform the ACT that they have
    fulfilled the necessary requested compliance action.

    Example:
            The data provider requested for the deletion of the data. Once the controller receives data deletion
            request, controller or processor has to delete data. And once they delete they can notify ACT following the
            JSON Schema specified below.
    """
    consent_id = fields.String(required=True)
    compliance_action_request = fields.String(required=True)
    compliance_obligation_status = fields.String(required=True)
    decision_token = fields.String(required=True)
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
        response = ce.compliance_check_act(level="dataprovider", consentProvidedBy=data_provider_id)
        return response

class ComplianceObligation(MethodResource, Resource):
    @doc(description="Data erase compliance obligation", tags=["Compliance"])
    @use_kwargs(ComplianceObligationSchema)
    @marshal_with(ComplianceReturnSchema)
    def post(self, **kwargs):
        schema_serializer = ComplianceObligationSchema()
        data = request.get_json(force=True)
        try:
            validated_compliance_obligation_data = schema_serializer.load(data)
        except ValidationError as e:
            return {"error": str(e)}, 400
        compliance_notification_inst = ComplianceObligationNotification()

        store_notification = compliance_notification_inst.store_compliance_obligation_notification_status(
            validated_compliance_obligation_data
        )
        return store_notification





