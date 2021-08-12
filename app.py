# -*- coding: utf-8 -*-
# @Time    : 09.05.21 19:09
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : app.py
# @Software: PyCharm

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
from resources.audit import AuditDataProvider
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
api.add_resource(ConsentCreate,"/consent/create")
docs.register(ConsentCreate)
api.add_resource(Revoke,"/consent/<string:consent_id>/revoke")
docs.register(Revoke)

#Compliance
api.add_resource(BrokenConsent,"/consent/broken-chain")
docs.register(BrokenConsent)
#LUH Interaction
api.add_resource(QueryAllConsentID,"/query/bulk-consent-id")
docs.register(QueryAllConsentID)
api.add_resource(QueryConsentIDByConsentProviderID,"/query/<string:consentprovider_id>/consentid")
docs.register(QueryConsentIDByConsentProviderID)
#audit
api.add_resource(AuditConsent, "/audit/<string:consent_id>/consent")
docs.register(AuditConsent)
api.add_resource(AuditDataProvider, "/audit/<string:data_provider_id>/<string:level_of_details>/data-provider")
docs.register(AuditDataProvider)
#JWTLogin
api.add_resource(JWTUserLogin, "/jwt/login/")
docs.register(JWTUserLogin)

#register
api.add_resource(JWTUserRegister, "/jwt/register/")
docs.register(JWTUserRegister)

#default
api.add_resource(Test,"/")







if __name__ == '__main__':
    # from db import db
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    #     print("Running")
    app.run(port=5000, debug=True)
