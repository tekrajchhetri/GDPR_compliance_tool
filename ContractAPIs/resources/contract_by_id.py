from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from sparql.queries import SPARQL
from credentials.user_credentials import UserCredentials

class GetContractById(MethodResource,Resource,UserCredentials):
    @doc(description='Get contract by contract id.', tags=['Contract By Contract Id'])
    @UserCredentials.check_for_token
    def get(self, id):
        query = SPARQL()
        response = query.get_contract_by_id(id)
        return response
