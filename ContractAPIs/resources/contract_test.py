
import unittest
import requests
from resources import contract_by_requester 

class ContractApiTest(unittest.TestCase):


    def setUp(self):
        self.requester=contract_by_requester.GetContractByRequester()
    # base url
    CONTRACT_URL="http://127.0.0.1:5000/"
    # get all contracts
    def test_get_all_contracts(self):
        r=requests.get(ContractApiTest.CONTRACT_URL)
        self.assertEqual(r.status_code,200)
    # get contract by requester
    def test_get_contract_by_requester(self):
        # from_contract_requester=self.requester
        # print(from_contract_requester)
        # # pass
        requester='CompanyABC'
        r=requests.get(ContractApiTest.CONTRACT_URL+"query/contractbyrequester/{}/".format(requester))
        self.assertEqual(r.status_code,200)
    # get provider by provider
    def test_get_contract_by_provider(self):
        provider='Brade'
        r=requests.get(ContractApiTest.CONTRACT_URL+"query/contractbyrequester/{}/".format(provider))
        self.assertEqual(r.status_code,200)
    # get contract by contract id
    def test_get_contract_by_id(self):
        id='kg244565'
        r=requests.get(ContractApiTest.CONTRACT_URL+"query/contractbyrequester/{}/".format(id))
        self.assertEqual(r.status_code,200)
    # new contract
    def test_new_contract(self):
        data= {
                "Amendment": "abccc",
                "ConfidentialityObligation": "string",
                "ContractId": "kg121213",
                "ContractProvider": "string",
                "ContractRequester": "string",
                "ContractType": "string",
                "DataController": "string",
                "DataProtection": "string",
                "EffectiveDate": "2021-06-06",
                "ExecutionDate": "2021-06-06",
                "ExpireDate": "2022-06-06",
                "LimitationOnUse": "string",
                "Medium": "string",
                "MethodOfNotice": "string",
                "NoThirdPartyBeneficiaries": "string",
                "PermittedDisclosure": "string",
                "Purpose": "string",
                "ReceiptOfNotice": "string",
                "Severability": "string",
                "StartDate": "2021-06-06",
                "TerminationForInsolvency": "string",
                "TerminationForMaterialBreach": "string",
                "TerminationOnNotice": "string",
                "Waiver": "string"
        }
        r=requests.post(ContractApiTest.CONTRACT_URL+"/contract/create/",json=data)
        self.assertEqual(r.status_code,200)
    # # update contract
    # def test_update_contract(self):
    #     update_data= {
    #             "Amendment": "abccc",
    #             "ConfidentialityObligation": "string",
    #             "ContractId": "kg121213",
    #             "ContractProvider": "Abdul",
    #             "ContractRequester": "string",
    #             "ContractType": "string",
    #             "DataController": "string",
    #             "DataProtection": "string",
    #             "EffectiveDate": "2021-06-06",
    #             "ExecutionDate": "2021-06-06",
    #             "ExpireDate": "2022-06-06",
    #             "LimitationOnUse": "string",
    #             "Medium": "string",
    #             "MethodOfNotice": "string",
    #             "NoThirdPartyBeneficiaries": "string",
    #             "PermittedDisclosure": "string",
    #             "Purpose": "string",
    #             "ReceiptOfNotice": "string",
    #             "Severability": "string",
    #             "StartDate": "2021-06-06",
    #             "TerminationForInsolvency": "string",
    #             "TerminationForMaterialBreach": "string",
    #             "TerminationOnNotice": "string",
    #             "Waiver": "string"
    #     }
    #     r=requests.post(ContractApiTest.CONTRACT_URL+"/contract/update/",json=update_data)
    #     self.assertEqual(r.status_code,200)