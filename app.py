import os

from flask import Flask
from flask_restful import Api
from resources.Test import Test
from resources.query import QueryConsentIDName, QueryAllConsentID
app = Flask(__name__)
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from resources.consent import  ConsentCreate, Revoke, BrokenConsent

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
api.add_resource(Revoke,"/consent/revoke/<string:consent_id>")
api.add_resource(BrokenConsent,"/consent/brokenconsent/")
docs.register(ConsentCreate)
api.add_resource(QueryAllConsentID,"/query/bconsentid/")
docs.register(QueryAllConsentID)
api.add_resource(QueryConsentIDName,"/query/consentid/<string:name>/")
docs.register(QueryConsentIDName)

api.add_resource(Test,"/")
# api.add_resource(ClassName, "/compliance_verify/<string:name>")


if __name__ == '__main__':
    app.run(debug=True)
