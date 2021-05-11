# -*- coding: utf-8 -*-
# @Time    : 11.05.21 16:10
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : query_resources.py
# @Software: PyCharm



from flask_restful import Resource
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs
from core.QueryEngine import QueryEngine
import json

# class ResponseSchema(Schema):
#     message = fields.Str(default="Success")
#
# class RequestSchema(Schema):
#     api_type = fields.String(required=True, description="Input Query String")

class QueryConsentIDName(MethodResource, Resource):
    @doc(description='Get consent ID by name.', tags=['ConsentID By Name'])
    def get(self, name):
        query = QueryEngine()
        return json.loads(query.select_query_gdb(consentProvidedBy=name,purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None, additionalData="consentID"))

class QueryAllConsentID(MethodResource, Resource):
    @doc(description='Get all consent ID.', tags=['All ConsentID'])
    def get(self):
        query = QueryEngine()
        return json.loads(query.select_query_gdb(consentProvidedBy=None,purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None, additionalData="bconsentID"))

