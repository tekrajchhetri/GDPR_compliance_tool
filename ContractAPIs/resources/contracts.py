from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from sparql.queries import SPARQL
from credentials.user_credentials import UserCredentials

class Contracts(MethodResource,Resource,UserCredentials):
  
    @doc(description='Get all contract ID.', tags=['All ContractId'])
    @UserCredentials.check_for_token
    def get(self):
        query = SPARQL()
        response = query.get_all_contracts()
        return response 
