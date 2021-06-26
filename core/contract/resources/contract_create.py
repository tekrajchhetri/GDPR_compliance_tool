from flask.json import jsonify
from core.contract_validation.ContractValidation import ContractValidation
from flask_restful import Resource, reqparse, request
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs
from core.contract.sparql.queries import SPARQL
from marshmallow import Schema, fields


class ForNestedSchema(Schema):
    data = fields.List(fields.String())


class ContractRequestSchema(Schema):
    ContractId = fields.String(required=True, description="Contract ID")
    ContractType = fields.String(required=True,
                                 description="Contract Type")
    Purpose = fields.String(required=True, description="For What Purpose")
    ContractRequester = fields.String(required=True,
                                      description="Contract Requester")
    ContractProvider = fields.String(required=True,
                                     description="Contract Provider")
    DataController = fields.String(required=True,
                                   description="Data Controller")
    StartDate = fields.Date(required=False,
                            description="Start Date")
    ExecutionDate = fields.Date(required=False,
                                description="Execution Date")
    EffectiveDate = fields.Date(required=False,
                                description="Effective Date")
    ExpireDate = fields.Date(required=False,
                             description="Expire Date")
    Medium = fields.String(required=False, description="Medium")
    Waiver = fields.String(required=False, description="Waiver")
    Amendment = fields.String(required=False, description="Amendment")
    ConfidentialityObligation = fields.String(
        required=False, description="Confidentiality Obligation")
    DataProtection = fields.String(
        required=False, description="Data Protection")
    LimitationOnUse = fields.String(
        required=False, description="Limitation On Use")
    MethodOfNotice = fields.String(
        required=False, description="Method Of Notice")
    NoThirdPartyBeneficiaries = fields.String(
        required=False, description="No Third Party Beneficiaries")
    PermittedDisclosure = fields.String(
        required=False, description="Permitted Disclosure")
    ReceiptOfNotice = fields.String(
        required=False, description="Receipt Of Notice")
    Severability = fields.String(required=False, description="Severability")
    TerminationForInsolvency = fields.String(
        required=False, description="Termination For Insolvency")
    TerminationForMaterialBreach = fields.String(
        required=False, description="Termination For Material Breach")
    TerminationOnNotice = fields.String(
        required=False, description="Termination On Notice")
    ContractStatus = fields.String(
        required=False, description="Contract Status")


class ContractCreate(MethodResource, Resource):
    @doc(description='create contract.', tags=['Create Contract'])
    # @UserCredentials.check_for_token
    @use_kwargs(ContractRequestSchema)
    def post(self, **kwargs):
        schema_serializer = ContractRequestSchema()
        data = request.get_json(force=True)
        validated_data = schema_serializer.load(data)
        cv = ContractValidation()
        response = cv.post_data(validated_data)
        if(response):
            return jsonify({'Success': "Record inserted successfully."})
        else:
            return jsonify({'Error': "Record not inserted due to some errors."})
