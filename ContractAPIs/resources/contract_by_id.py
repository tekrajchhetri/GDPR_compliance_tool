from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from sparql.queries import SPARQL

class GetContractById(MethodResource,Resource):
    @doc(description='Get contract by contract id.', tags=['Contract By Contract Id'])
    def get(self, id):
        query = SPARQL()
        result = query.get_contract_by_id(id)
        return result