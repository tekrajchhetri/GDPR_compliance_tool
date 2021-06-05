# -*- coding: utf-8 -*-
# @Time    : 11.05.21 16:10
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : query.py
# @Software: PyCharm



from flask_restful import Resource
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs
from core.QueryEngine import QueryEngine
import json


class NestedSchema(Schema):
    ConsentID =  fields.Dict(
        required=True, keys=fields.Str(),
        values=fields.Str()
    )

class BulkResponseQuerySchema(Schema):
    bindings = fields.List(fields.Nested(NestedSchema),required=True)





class QueryConsentIDByConsentProviderID(MethodResource, Resource):
    @doc(description='Get consent ID by consent provider.', tags=['ConsentID by consentprovider ID'])
    @marshal_with(BulkResponseQuerySchema)
    def get(self, consentprovider_id):
        query = QueryEngine()
        resp =  json.loads(query.select_query_gdb(consentProvidedBy=consentprovider_id,purpose=None, dataProcessing=None,
                                                 dataController=None, dataRequester=None, additionalData="consentID"))
        to_response = resp["results"]
        return to_response, 200

class QueryAllConsentID(MethodResource, Resource):
    @doc(description='Get all consent ID.', tags=['All ConsentID'])
    @marshal_with(BulkResponseQuerySchema)
    def get(self):
        query = QueryEngine()
        response =  json.loads(query.select_query_gdb(consentProvidedBy=None,purpose=None, dataProcessing=None,
                                                 dataController=None,dataRequester=None, additionalData="bconsentID"))
        response = response["results"]
        return response, 200



