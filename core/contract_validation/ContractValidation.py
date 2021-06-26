from core.helper.date_helper import DateHelper
from core.query_processor.QueryProcessor import QueryEngine


class ContractValidation(QueryEngine):

    def __init__(self):
        super().__init__()

    def post_data(self, validated_data):
        ContractId = validated_data["ContractId"]
        ContractType = validated_data["ContractType"]
        Purpose = validated_data["Purpose"]
        ContractRequester = validated_data["ContractRequester"]
        ContractProvider = validated_data["ContractProvider"]
        DataController = validated_data["DataController"]
        StartDate = validated_data["StartDate"]
        ExecutionDate = validated_data["ExecutionDate"]
        ExpireDate = validated_data["ExpireDate"]
        EffectiveDate = validated_data["EffectiveDate"]
        Medium = validated_data["Medium"]
        Waiver = validated_data["Waiver"]
        Amendment = validated_data["Amendment"]
        ConfidentialityObligation = validated_data["ConfidentialityObligation"]
        DataProtection = validated_data["DataProtection"]
        LimitationOnUse = validated_data["LimitationOnUse"]
        MethodOfNotice = validated_data["MethodOfNotice"]
        NoThirdPartyBeneficiaries = validated_data["NoThirdPartyBeneficiaries"]
        PermittedDisclosure = validated_data["PermittedDisclosure"]
        ReceiptOfNotice = validated_data["ReceiptOfNotice"]
        Severability = validated_data["Severability"]
        TerminationForInsolvency = validated_data["TerminationForInsolvency"]
        TerminationForMaterialBreach = validated_data["TerminationForMaterialBreach"]
        TerminationOnNotice = validated_data["TerminationOnNotice"]
        ContractStatus = validated_data["ContractStatus"]

        respone = self.post_sparql(self.get_username(), self.get_password(),
                                   self.insert_query(ContractId=ContractId,
                                                     ContractType=ContractType,
                                                     Purpose=Purpose,
                                                     ContractRequester=ContractRequester,
                                                     ContractProvider=ContractProvider,
                                                     DataController=DataController,
                                                     StartDate=StartDate,
                                                     ExecutionDate=ExecutionDate,
                                                     EffectiveDate=EffectiveDate,
                                                     ExpireDate=ExpireDate,
                                                     Medium=Medium,
                                                     Waiver=Waiver,
                                                     Amendment=Amendment,
                                                     ConfidentialityObligation=ConfidentialityObligation,
                                                     DataProtection=DataProtection,
                                                     LimitationOnUse=LimitationOnUse,
                                                     MethodOfNotice=MethodOfNotice,
                                                     NoThirdPartyBeneficiaries=NoThirdPartyBeneficiaries,
                                                     PermittedDisclosure=PermittedDisclosure,
                                                     ReceiptOfNotice=ReceiptOfNotice,
                                                     Severability=Severability,
                                                     TerminationForInsolvency=TerminationForInsolvency,
                                                     TerminationForMaterialBreach=TerminationForMaterialBreach,
                                                     TerminationOnNotice=TerminationOnNotice,
                                                     ContractStatus=ContractStatus
                                                     )
                                   )
        return respone
