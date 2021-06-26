from resources.audit import AuditConsent
from resources.consent import ConsentCreate, Revoke, BrokenConsent
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
import os

from flask import Flask
from flask_restful import Api
from resources.Test import Test
from resources.query import QueryConsentIDByConsentProviderID, QueryAllConsentID
# contract resources
from core.contract.resources.contracts import Contracts
from core.contract.resources.contract_by_requester import GetContractByRequester
from core.contract.resources.contract_by_provider import GetContractByProvider
from core.contract.resources.contract_create import ContractCreate
from core.contract.resources.contract_update import ContractUpdateByContractId
from core.contract.resources.contract_by_id import GetContractById
from core.contract.resources.generate_token import GenerateToken
app = Flask(__name__)


api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Automatic Contracting API Specification',
        version='v01',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    # 'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

api.add_resource(ConsentCreate, "/consent/create/")
docs.register(ConsentCreate)
api.add_resource(Revoke, "/consent/revoke/<string:consent_id>")
docs.register(Revoke)
api.add_resource(BrokenConsent, "/consent/broken_chain/")
docs.register(BrokenConsent)
api.add_resource(QueryAllConsentID, "/query/bulk_consent_id/")
docs.register(QueryAllConsentID)
api.add_resource(QueryConsentIDByConsentProviderID,
                 "/query/consentid/<string:consentprovider_id>/")
docs.register(QueryConsentIDByConsentProviderID)
api.add_resource(AuditConsent, "/audit/<string:consent_id>")
docs.register(AuditConsent)
api.add_resource(Test, "/")
# api.add_resource(ClassName, "/compliance_verify/<string:name>")

# contract endpoint url
# generate token
api.add_resource(GenerateToken, '/token/')
# contract api end points with swagger documentation

api.add_resource(Contracts, '/contract/')
docs.register(Contracts)
api.add_resource(GetContractByRequester,
                 '/contract/contract_by_requester/<string:requester>/')
docs.register(GetContractByRequester)
api.add_resource(GetContractById, '/contract/contract_by_id/<string:id>/')
docs.register(GetContractById)
# api.add_resource(ContractRevokeByContractId,
#                  '/contract/contract_revoke_by_id/<string:id>/')
# docs.register(ContractRevokeByContractId)
api.add_resource(GetContractByProvider,
                 '/contract/contract_by_provider/<string:provider>/')
docs.register(GetContractByProvider)
api.add_resource(ContractCreate, "/contract/create/")
docs.register(ContractCreate)


if __name__ == '__main__':
    app.run(debug=True)
