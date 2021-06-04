# -*- coding: utf-8 -*-
# @Time    : 12.05.21 14:32
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : consent.py
# @Software: PyCharm


from flask_restful import Resource, reqparse, request
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields,ValidationError
from flask_apispec import marshal_with, doc, use_kwargs
from core.QueryEngine import QueryEngine
import datetime
import json


class ForNestedSchema(Schema):
    data = fields.List(fields.String())
    # name = fields.Str()

class AgentsSchema(Schema):
    id = fields.Str()
    role = fields.Str()

class ConsentRequests(Schema):
    consentid = fields.String(required=True,
                                   default_value= "AX13RCSD442",
                                   )
    GrantedAtTime = fields.DateTime(required=True)
    expirationTime = fields.DateTime()
    city = fields.String(required=True)
    state = fields.String(required=True)
    country = fields.String(required=True)
    dataprovider = fields.String(required=True)
    Resource = fields.Dict(
        required=True, keys=fields.Str(),
        values=fields.List(fields.Nested(ForNestedSchema))
    )
    Medium = fields.String(required=True, description="How consent was given? Eg. Online, MobileApp")
    Agents = fields.List(fields.Nested(AgentsSchema),required=True)
    Purpose = fields.String(required=True, description="For what purpose")
    DataProcessing = fields.List(fields.String(),required=True,
                                 description='["Analysis, collection, storage"]')

class ReturnSchema(Schema):
    act_status_code = fields.Integer(required=True)
    decision = fields.String(required=True)
    decision_token = fields.String(required=True)
    message = fields.String(optional=True)
    timestamp = fields.String(required=True)


class ConsentCreate(MethodResource, Resource):
    @doc(description='create consent.', tags=['Create Consent'])
    @use_kwargs(ConsentRequests)
    @marshal_with(ReturnSchema)
    def post(self, **kwargs):
        schema_serializer = ConsentRequests()
        data = request.get_json(force=True)
        try:
            validated_data = schema_serializer.load(data)
        except ValidationError as e:
            return {"error": str(e)}, 400
        qe = QueryEngine()
        response = qe.post_data(validated_data)
        return response

class QueryAllConsentID(MethodResource, Resource):
    @doc(description='Get all consent ID.', tags=['All ConsentID'])
    def get(self):
        query = QueryEngine()
        return json.loads(query.select_query_gdb(consentProvidedBy=None, purpose=None, dataProcessing=None,
                                                 dataController=None, dataRequester=None, additionalData="bconsentID"))




class Revoke(MethodResource, Resource):
    pass

class BrokenConsent(MethodResource, Resource):
    pass

