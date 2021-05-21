# -*- coding: utf-8 -*-
# @Time    : 12.05.21 14:32
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : consent_creaateresources.py
# @Software: PyCharm


from flask_restful import Resource, reqparse, request
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs
from core.QueryEngine import QueryEngine
import datetime
import json


class ForNestedSchema(Schema):
    data = fields.List(fields.String())
    name = fields.Str()

class AgentsSchema(Schema):
    id = fields.Str()
    role = fields.Str()

class ConsentRequests(Schema):
    PersonaldataId = fields.String(required=True,
                                   default_value= "AX13RCSD442",
                                   )
    GrantedAtTime = fields.DateTime(required=True,
                                    description="Date when consent was provided")
    GivenAtLocation = fields.String(required=True, description="Location from where consent was given")
    ExpirationDate = fields.DateTime(required=True,
                                     description="Consent expiry date")
    Resource = fields.Dict(
        required=True, keys=fields.Str(),
        values=fields.List(fields.Nested(ForNestedSchema))
    )
    dataUsage = fields.List(fields.Str(),
                            required=True,
                            description='["GPS","speed","milleage","personalData","trafficJamLocation"]')
    Medium = fields.String(required=True, description="How consent was given? Eg. Online, MobileApp")
    Agents = fields.List(fields.Nested(AgentsSchema),required=True)
    Purpose = fields.String(required=True, description="For what purpose")
    DataProcessing = fields.List(fields.String(),required=True,
                                 description='["Analysis, collection, storage"]')


class ConsentCreate(MethodResource, Resource):
    @doc(description='create consent.', tags=['Create Consent'])
    @use_kwargs(ConsentRequests)
    def post(self, **kwargs):
        schema = ConsentRequests()
        data = request.get_json(force=True)
        validated_data = schema.load(data)
        return validated_data

class QueryAllConsentID(MethodResource, Resource):
    @doc(description='Get all consent ID.', tags=['All ConsentID'])
    def get(self):
        query = QueryEngine()
        return json.loads(query.select_query_gdb(consentProvidedBy=None, purpose=None, dataProcessing=None,
                                                 dataController=None, dataRequester=None, additionalData="bconsentID"))



