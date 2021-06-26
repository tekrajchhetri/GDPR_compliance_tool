from flask import json
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc
from core.query_processor.QueryProcessor import QueryEngine
from marshmallow import Schema, fields


class NestedSchema(Schema):
    Contract = fields.Dict(
        required=True, keys=fields.Str(),
        values=fields.Str()
    )


class BulkResponseQuerySchema(Schema):
    bindings = fields.List(fields.Nested(NestedSchema), required=True)


class Contracts(MethodResource, Resource):

    @doc(description='Get all contract ID.', tags=['All ContractId'])
    @marshal_with(BulkResponseQuerySchema)
    # @UserCredentials.check_for_token
    def get(self):
        query = QueryEngine()
        response = json.loads(query.select_query_gdb(consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                                                     dataRequester=None, additionalData="bcontractId", consentID=None, contractId=None,
                                                     contractRequester=None, contractProvider=None,))
        response = response["results"]
        return response, 200
