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
import json


class ConsentRequests(Schema):
    PersonaldataId = fields.String(required=True,
                                   description="Unique personal identifier")
    applicationMappings = fields.Dict(required=False, keys=fields.Str(), values=fields.Str())
    GrantedAtTime = fields.DateTime(required=True, description="Date when consent was provided")
    GivenAtLocation = fields.String(required=True, description="Location from where consent was given")
    ExpirationDate = fields.DateTime(required=True, description="Consent expiry date")
    Resource = fields.Dict(required=True, keys=fields.Str(), values=fields.List(fields.Str()))
    dataUsage = fields.List(fields.String(),required=True,
                            description='["GPS","speed","milleage","personalData","trafficJamLocation"]')
    Medium = fields.String(required=True, description="How consent was given? Eg. Online, MobileApp")
    Agents = fields.List(fields.String(),required=True,
                         description='["60a55c53d79bc757698041e9","60a55c9dd79bc757698041ea"]')
    Purpose = fields.String(required=True, description="For what purpose")
    DataProcessing = fields.List(fields.String(),required=True,
                                 description='["Analysis, collection, storage"]')


class ConsentCreate(MethodResource, Resource):
    @doc(description='create consent.', tags=['Create Consent'])
    @use_kwargs(ConsentRequests)
    @marshal_with(ConsentRequests)
    def post(self, **kwargs):
        print(kwargs["PersonaldataId"])
        # query = QueryEngine()
        # parser = reqparse.RequestParser()
        # parser.add_argument('ConsentIDInput', required=True,  location="json")
        # parser.add_argument('DataControllerInput', required=True, location="json")
        # parser.add_argument('DataInput', required=True,location="json")
        # parser.add_argument('DataProcessingInput', required=True, location="json")
        # parser.add_argument('DataRequesterInput', required=True, location="json")
        # parser.add_argument('DurationInput', required=True, location="json")
        # parser.add_argument('GrantedAtTimeInput', required=True,location="json")
        # parser.add_argument('MediumInput', required=True,  location="json")
        # parser.add_argument('NameInput', required=True,location="json")
        # parser.add_argument('PurposeInput', required=True, location="json")
        # # data = request.get_json(force=True)
        # args = parser.parse_args()
        # response = query.post_data(ConsentIDInput = args["ConsentIDInput"],
        #                            DataControllerInput = args["DataControllerInput"] ,
        #                            DataInput = args["DataInput"] ,
        #                            DataProcessingInput = args["DataProcessingInput"] ,
        #                            DataRequesterInput = args["DataRequesterInput"],
        #                            DurationInput = args["DurationInput"],
        #                            GrantedAtTimeInput = args["GrantedAtTimeInput"] ,
        #                            MediumInput = args["MediumInput"],
        #                            NameInput = args["NameInput"],
        #                            PurposeInput = args["PurposeInput"])


        return kwargs

class QueryAllConsentID(MethodResource, Resource):
    @doc(description='Get all consent ID.', tags=['All ConsentID'])
    def get(self):
        query = QueryEngine()
        return json.loads(query.select_query_gdb(consentProvidedBy=None, purpose=None, dataProcessing=None,
                                                 dataController=None, dataRequester=None, additionalData="bconsentID"))



