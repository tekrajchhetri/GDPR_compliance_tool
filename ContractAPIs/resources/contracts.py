from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from sparql.queries import SPARQL

class Contracts(MethodResource,Resource):
    @doc(description='Get all contract ID.', tags=['All ContractId'])
    def get(self):
        query = SPARQL()
        result = query.get_all_contracts()
        return result