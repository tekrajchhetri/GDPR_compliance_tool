from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from sparql.queries import SPARQL
from core.Credentials import Credentials


class GetContractByProvider(MethodResource, Resource, Credentials):
    @doc(description='Get contract by contract provider.', tags=['Contract By Contract Provider'])
    # @UserCredentials.check_for_token
    def get(self, provider):
        query = SPARQL()
        response = query.get_contract_by_provider(provider)
        return response
