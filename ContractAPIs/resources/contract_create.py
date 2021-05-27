from flask_restful import Resource,reqparse
from flask_apispec.views import MethodResource
from flask_apispec import doc,use_kwargs
from sparql.queries import SPARQL
from marshmallow import Schema, fields


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
    ConfidentialityObligation = fields.String(required=False, description="Confidentiality Obligation")
    DataProtection = fields.String(required=False, description="Data Protection")
    LimitationOnUse = fields.String(required=False, description="Limitation On Use")
    MethodOfNotice = fields.String(required=False, description="Method Of Notice")
    NoThirdPartyBeneficiaries = fields.String(required=False, description="No Third Party Beneficiaries")
    PermittedDisclosure = fields.String(required=False, description="Permitted Disclosure")
    ReceiptOfNotice = fields.String(required=False, description="Receipt Of Notice")
    Severability = fields.String(required=False, description="Severability")
    TerminationForInsolvency = fields.String(required=False, description="Termination For Insolvency")
    TerminationForMaterialBreach = fields.String(required=False, description="Termination For Material Breach")
    TerminationOnNotice = fields.String(required=False, description="Termination On Notice")


class ContractCreate(MethodResource,Resource):
    @doc(description='create contract.', tags=['Create Contract'])
    @use_kwargs(ContractRequestSchema)
    
    def post(self, **kwargs):
        query = SPARQL()
        parser = reqparse.RequestParser()
        parser.add_argument('ContractId', required=True, location="json")
        parser.add_argument('ContractType', required=True, location="json")
        parser.add_argument('Purpose', required=True, location="json")
        parser.add_argument('ContractRequester', required=True, location="json")
        parser.add_argument('ContractProvider', required=True, location="json")
        parser.add_argument('DataController', required=True, location="json")
        parser.add_argument('StartDate', required=False, location="json")
        parser.add_argument('ExecutionDate', required=False, location="json")
        parser.add_argument('EffectiveDate', required=False, location="json")
        parser.add_argument('ExpireDate', required=True, location="json")                                                                                                        
        parser.add_argument('Medium', required=False, location="json")
        parser.add_argument('Waiver', required=False, location="json")
        parser.add_argument('Amendment', required=True, location="json")                                                                                                        
        parser.add_argument('ConfidentialityObligation', required=False, location="json")
        parser.add_argument('DataProtection', required=False, location="json")
        parser.add_argument('LimitationOnUse', required=True, location="json")                                                                                                        
        parser.add_argument('MethodOfNotice', required=False, location="json")
        parser.add_argument('NoThirdPartyBeneficiaries', required=False, location="json")
        parser.add_argument('PermittedDisclosure', required=True, location="json")                                                                                                        
        parser.add_argument('ReceiptOfNotice', required=False, location="json")
        parser.add_argument('Severability', required=False, location="json")
        parser.add_argument('TerminationForInsolvency', required=True, location="json")                                                                                                        
        parser.add_argument('TerminationForMaterialBreach', required=False, location="json")
        parser.add_argument('TerminationOnNotice', required=False, location="json")        

        args = parser.parse_args()
        response = query.post_data(
            ContractId=args["ContractId"],
            ContractType=args["ContractType"],
            Purpose=args["Purpose"],
            ContractRequester=args["ContractRequester"],
            ContractProvider=args["ContractProvider"],
            DataController=args["DataController"],
            StartDate=args["StartDate"],
            ExecutionDate=args["ExecutionDate"],
            EffectiveDate=args["EffectiveDate"],
            ExpireDate=args["ExpireDate"],
            Medium=args["Medium"],
            Waiver=args["Waiver"],
            Amendment=args["Amendment"],
            ConfidentialityObligation=args["ConfidentialityObligation"],
            DataProtection=args["DataProtection"],
            LimitationOnUse=args["LimitationOnUse"],
            MethodOfNotice=args["MethodOfNotice"],
            NoThirdPartyBeneficiaries=args["NoThirdPartyBeneficiaries"],
            PermittedDisclosure=args["PermittedDisclosure"],
            ReceiptOfNotice=args["ReceiptOfNotice"],
            Severability=args["Severability"],
            TerminationForInsolvency=args["TerminationForInsolvency"],
            TerminationForMaterialBreach=args["TerminationForMaterialBreach"],
            TerminationOnNotice=args["TerminationOnNotice"]),

            
        return response