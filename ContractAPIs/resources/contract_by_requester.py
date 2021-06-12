from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from sparql.queries import SPARQL
from credentials.user_credentials import UserCredentials


class GetContractByRequester(MethodResource,Resource,UserCredentials):
    @doc(description='Get contract by contract requester.', tags=['Contract By Contract Requester'])
    @UserCredentials.check_for_token
    def get(self, requester):
        query = SPARQL()
        response = query.get_contract_by_requester(requester)
        return response
