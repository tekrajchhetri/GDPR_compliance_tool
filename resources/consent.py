# -*- coding: utf-8 -*-
# @Time    : 12.05.21 14:32
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : consent.py
# @Software: PyCharm


from flask_restful import Resource, request
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, ValidationError
from flask_apispec import marshal_with, doc, use_kwargs
from core.consent_validation.ConsentValidation import ConsentValidation
from core.compliance.ComplianceEngine import ComplianceEngine
from core.security.JWTDecorator import ccc_required


class ForNestedSchema(Schema):
    data = fields.List(fields.String())


class AgentsSchema(Schema):
    id = fields.Str()
    role = fields.Str()


class ConsentRequests(Schema):
    consentid = fields.String(
        required=True,
        default_value="AX13RCSD442",
    )
    GrantedAtTime = fields.DateTime(required=True)
    expirationTime = fields.DateTime()
    city = fields.String(required=True)
    state = fields.String(required=True)
    country = fields.String(required=True)
    dataprovider = fields.String(required=True)
    Resource = fields.Dict(
        required=True,
        keys=fields.Str(),
        values=fields.List(fields.Nested(ForNestedSchema)),
    )
    Medium = fields.String(
        required=True, description="How consent was given? Eg. Online, MobileApp"
    )
    Agents = fields.List(fields.Nested(AgentsSchema), required=True)
    Purpose = fields.String(required=True, description="For what purpose")
    DataProcessing = fields.List(
        fields.String(), required=True, description='["Analysis, collection, storage"]'
    )


class ReturnSchema(Schema):
    act_status_code = fields.Integer(required=True)
    decision = fields.String(required=True)
    decision_token = fields.String(required=True)
    message = fields.String(optional=True)
    timestamp = fields.String(required=True)


class ConsentCreate(MethodResource, Resource):
    @ccc_required(fresh=True)
    @doc(description="create consent.", tags=["Consent"])
    @use_kwargs(ConsentRequests)
    @marshal_with(ReturnSchema)
    def post(self, **kwargs):
        schema_serializer = ConsentRequests()
        data = request.get_json(force=True)
        try:
            validated_data = schema_serializer.load(data)
        except ValidationError as e:
            return {"error": str(e)}, 400
        cv = ConsentValidation()
        response = cv.post_data(validated_data)
        return response


"""
Compliance rest endpoints
"""


class Revoke(MethodResource, Resource):
    @ccc_required(fresh=True)
    @doc(description="Revoke consent.", tags=["Consent"])
    @marshal_with(ReturnSchema)
    def delete(self, consent_id):
        ce = ComplianceEngine()
        response = ce.revoke_consent(consentID=consent_id)
        return response


class BrokenConsentSchema(Schema):
    consent_id = fields.String(required=True)
    reason = fields.String(required=True)


class BrokenConsent(MethodResource, Resource):
    @ccc_required(fresh=True)
    @doc(description="Broken consent chain.", tags=["Compliance"])
    @marshal_with(ReturnSchema)
    @use_kwargs(BrokenConsentSchema)
    def post(self, **kwarg):
        ce = ComplianceEngine()
        schema_serializer = BrokenConsentSchema()
        data = request.get_json(force=True)
        try:
            validated_data = schema_serializer.load(data)
        except ValidationError as e:
            return {"error": str(e)}, 400
        consent_id = validated_data["consent_id"]
        reason = validated_data["reason"]
        response = ce.broken_consent(consentID=consent_id, reason_for_logging=reason)
        return response
