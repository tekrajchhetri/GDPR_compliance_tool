from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from sparql.queries import SPARQL

class ContractRevokeByContractId(MethodResource,Resource):
    @doc(description='Contract revoke by contract id.', tags=['Contract revoke By Contract Id'])
    def put(self, id):
        query = SPARQL()
        result = query.contract_revoke_by_id(id)
        response={
            'STATUS':'Success',
            'Message':result,
        }
        return response