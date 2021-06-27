import os

from flask import Flask
from flask_restful import Api
from resources.Test import Test
from resources.query import QueryConsentIDByConsentProviderID, QueryAllConsentID
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)
jwt = JWTManager(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280b1245'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=70)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///act_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from resources.consent import  ConsentCreate
from resources.consent import  Revoke
from resources.consent import  BrokenConsent
from resources.audit import AuditConsent
from resources.user import JWTUserRegister
from resources.user import JWTUserLogin

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
#Consent
api.add_resource(ConsentCreate,"/consent/create/")
docs.register(ConsentCreate)
api.add_resource(Revoke,"/consent/revoke/<string:consent_id>")
docs.register(Revoke)

#Compliance
api.add_resource(BrokenConsent,"/consent/broken_chain/")
docs.register(BrokenConsent)
#LUH Interaction
api.add_resource(QueryAllConsentID,"/query/bulk_consent_id/")
docs.register(QueryAllConsentID)
api.add_resource(QueryConsentIDByConsentProviderID,"/query/consentid/<string:consentprovider_id>/")
docs.register(QueryConsentIDByConsentProviderID)
#Tracing
api.add_resource(AuditConsent, "/audit/<string:consent_id>")
docs.register(AuditConsent)

#JWTLogin
api.add_resource(JWTUserLogin, "/jwt/login/")
docs.register(JWTUserLogin)

#register
api.add_resource(JWTUserRegister, "/jwt/register/")
docs.register(JWTUserRegister)

#default
api.add_resource(Test,"/")







if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
