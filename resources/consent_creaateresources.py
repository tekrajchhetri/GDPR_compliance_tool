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


class ConsentRequest(Schema):
    ConsentIDInput = fields.String(required=True, description="Consent ID")
    DataControllerInput = fields.String(required=True, description="Data Controller")
    DataInput = fields.String(required=True, description="What data? EG. GPS")
    DataProcessingInput = fields.String(required=True, description="What Purpose? EG. Analysis")
    DataRequesterInput = fields.String(required=True, description="Who want data? EG. LexisNexis")
    DurationInput = fields.String(required=True, description="How many days? EG. 10days")
    GrantedAtTimeInput = fields.DateTime(required=True, description="Time consent given")
    MediumInput = fields.String(required=True, description="What medium consent is provided by?")
    NameInput = fields.String(required=True, description="Data subject")
    PurposeInput = fields.String(required=True, description="For what purpose")

class ConsentCreate(MethodResource, Resource):
    @doc(description='create consent.', tags=['Create Consent'])
    @use_kwargs(ConsentRequest)
    def post(self, **kwargs):
        query = QueryEngine()
        parser = reqparse.RequestParser()
        parser.add_argument('ConsentIDInput', required=True,  location="json")
        parser.add_argument('DataControllerInput', required=True, location="json")
        parser.add_argument('DataInput', required=True,location="json")
        parser.add_argument('DataProcessingInput', required=True, location="json")
        parser.add_argument('DataRequesterInput', required=True, location="json")
        parser.add_argument('DurationInput', required=True, location="json")
        parser.add_argument('GrantedAtTimeInput', required=True,location="json")
        parser.add_argument('MediumInput', required=True,  location="json")
        parser.add_argument('NameInput', required=True,location="json")
        parser.add_argument('PurposeInput', required=True, location="json")
        # data = request.get_json(force=True)
        args = parser.parse_args()
        response = query.post_data(ConsentIDInput = args["ConsentIDInput"],
                                   DataControllerInput = args["DataControllerInput"] ,
                                   DataInput = args["DataInput"] ,
                                   DataProcessingInput = args["DataProcessingInput"] ,
                                   DataRequesterInput = args["DataRequesterInput"],
                                   DurationInput = args["DurationInput"],
                                   GrantedAtTimeInput = args["GrantedAtTimeInput"] ,
                                   MediumInput = args["MediumInput"],
                                   NameInput = args["NameInput"],
                                   PurposeInput = args["PurposeInput"])


        return response


class QueryAllConsentID(MethodResource, Resource):
    @doc(description='Get all consent ID.', tags=['All ConsentID'])
    def get(self):
        query = QueryEngine()
        return json.loads(query.select_query_gdb(consentProvidedBy=None, purpose=None, dataProcessing=None,
                                                 dataController=None, dataRequester=None, additionalData="bconsentID"))



