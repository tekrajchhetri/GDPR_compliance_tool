from flask import json
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from core.query_processor.QueryProcessor import QueryEngine
from marshmallow import Schema, fields


class NestedSchema(Schema):
    Contract = fields.Dict(
        required=True, keys=fields.Str(),
        values=fields.Str()
    )


class BulkResponseQuerySchema(Schema):
    bindings = fields.List(fields.Nested(NestedSchema), required=True)


class GetContractByRequester(MethodResource, Resource):
    @doc(description='Get contract by contract requester.', tags=['Contract By Contract Requester'])
    # @UserCredentials.check_for_token
    def get(self, requester):
        query = QueryEngine()
        response = json.loads(query.select_query_gdb(consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                                                     dataRequester=None, additionalData="contractId", consentID=None, contractId=None,
                                                     contractRequester=requester, contractProvider=None))
        response = response["results"]
        return response, 200
