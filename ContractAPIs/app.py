from flask import Flask
from flask_restful import Api
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_cors import CORS
# contract resources
from resources.contracts import Contracts
from resources.contract_by_requester import GetContractByRequester
from resources.contract_by_provider import GetContractByProvider
from resources.contract_create import ContractCreate
from resources.contract_revoke import ContractRevokeByContractId
from resources.contract_by_id import GetContractById
# flask app
app = Flask(__name__)
# cors enable for swagger-editor
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)
# swagger configuration
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Automatic Contracting API Specification',
        version='v01',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/',
})
# contract api end points with swagger documentation
docs = FlaskApiSpec(app)
api.add_resource(Contracts, '/api/contract/')
docs.register(Contracts)
api.add_resource(GetContractByRequester, '/api/contract/contract_by_requester/<string:requester>/')
docs.register(GetContractByRequester)
api.add_resource(GetContractById, '/api/contract/contract_by_id/<string:id>/')
docs.register(GetContractById)
api.add_resource(ContractRevokeByContractId, '/api/contract/contract_revoke_by_id/<string:id>/')
docs.register(ContractRevokeByContractId)
api.add_resource(GetContractByProvider, '/api/contract/contract_by_provider/<string:provider>/')
docs.register(GetContractByProvider)
api.add_resource(ContractCreate, "/api/contract/create/")
docs.register(ContractCreate)

if __name__ == '__main__':
    app.run(debug=True)
