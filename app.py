import os

from flask import Flask
from flask_restful import Api
from resources.Test import Test
from resources.query import QueryConsentIDByConsentProviderID, QueryAllConsentID
app = Flask(__name__)
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from resources.consent import  ConsentCreate, Revoke, BrokenConsent

from resources.audit import AuditConsent

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

api.add_resource(ConsentCreate,"/consent/create/")
docs.register(ConsentCreate)
api.add_resource(Revoke,"/consent/revoke/<string:consent_id>")
docs.register(Revoke)
api.add_resource(BrokenConsent,"/consent/broken_chain/<string:consent_id>/<string:reason>")
docs.register(BrokenConsent)
api.add_resource(QueryAllConsentID,"/query/bulk_consent_id/")
docs.register(QueryAllConsentID)
api.add_resource(QueryConsentIDByConsentProviderID,"/query/consentid/<string:consentprovider_id>/")
docs.register(QueryConsentIDByConsentProviderID)
api.add_resource(AuditConsent, "/audit/<string:consent_id>")
docs.register(AuditConsent)
api.add_resource(Test,"/")
# api.add_resource(ClassName, "/compliance_verify/<string:name>")


if __name__ == '__main__':
    app.run(debug=True)
