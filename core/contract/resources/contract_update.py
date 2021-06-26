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


class ContractUpdateByContractId(MethodResource, Resource):
    @doc(description='Contract update by contract id.', tags=['Contract update By Contract Id'])
    # @UserCredentials.check_for_token
    def put(self, id):
        # query = SPARQL()
        # result = query.contract_revoke_by_id(id)
        return 'update query'
