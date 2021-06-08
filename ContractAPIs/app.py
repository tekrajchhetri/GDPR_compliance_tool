from resources.contract_by_id import GetContractById
from flask import Flask
from flask_restful import Api
from marshmallow import Schema, fields
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin

from resources.contracts import Contracts
from resources.contract_by_requester import GetContractByRequester
from resources.contract_by_provider import GetContractByProvider
from resources.contract_create import ContractCreate
from resources.contract_revoke import ContractRevokeByContractId
import app

app = Flask(__name__)
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Automatic Contracting API Specification',
        version='v01',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})
docs = FlaskApiSpec(app)

api.add_resource(Contracts, '/contract/')
docs.register(Contracts)

api.add_resource(GetContractByRequester, '/contract/query/contractbyrequester/<string:requester>/')
docs.register(GetContractByRequester)

api.add_resource(GetContractById, '/contract/query/contractbyid/<string:id>/')
docs.register(GetContractById)

api.add_resource(ContractRevokeByContractId, '/contract/query/contractrevokebyid/<string:id>/')
docs.register(ContractRevokeByContractId)

api.add_resource(GetContractByProvider, '/contract/query/contractbyprovider/<string:provider>/')
docs.register(GetContractByProvider)

api.add_resource(ContractCreate, "/contract/create/")
docs.register(ContractCreate)

if __name__ == '__main__':
    app.run(debug=True)



