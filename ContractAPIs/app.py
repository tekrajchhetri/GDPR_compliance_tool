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

app = Flask(__name__)
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Automatic Contracting API Specification',
        version='v01',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

api.add_resource(Contracts, '/')
docs.register(Contracts)

api.add_resource(GetContractByRequester, '/query/contractbyrequester/<string:requester>/')
docs.register(GetContractByRequester)

api.add_resource(GetContractById, '/query/contractbyid/<string:id>/')
docs.register(GetContractById)

api.add_resource(ContractRevokeByContractId, '/query/contractrevokebyid/<string:id>/')
docs.register(ContractRevokeByContractId)

api.add_resource(GetContractByProvider, '/query/contractbyprovider/<string:provider>/')
docs.register(GetContractByProvider)

api.add_resource(ContractCreate, "/contract/create/")
docs.register(ContractCreate)

if __name__ == '__main__':
    app.run(debug=True)