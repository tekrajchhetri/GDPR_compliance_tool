import unittest
import requests
class ContractApiTest(unittest.TestCase):
    # base url
    CONTRACT_URL="http://127.0.0.1:5000/"
    DATA= {
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

    # get all contracts
    def test_get_all_contracts(self):
        r=requests.get(ContractApiTest.CONTRACT_URL)
        self.assertEqual(r.status_code,200)
    # get contract by requester
    def test_get_contract_by_requester(self):
        requester='CompanyABC'
        r=requests.get(ContractApiTest.CONTRACT_URL+"query/contractbyrequester/{}/".format(requester))
        self.assertEqual(r.status_code,200)
    # get contract by provider
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
        r=requests.post(ContractApiTest.CONTRACT_URL+"/contract/create/",json=ContractApiTest.DATA)
        self.assertEqual(r.status_code,200)
