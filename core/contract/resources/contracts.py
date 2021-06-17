from ssl import RAND_status
from flask import Response, json
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from core.contract.sparql.queries import SPARQL
from core.Credentials import Credentials


class Contracts(MethodResource, Resource):

    @doc(description='Get all contract ID.', tags=['All ContractId'])
    # @UserCredentials.check_for_token
    def get(self):
        query = SPARQL()
        result = query.get_all_contracts()
        return result
