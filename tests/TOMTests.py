# -*- coding: utf-8 -*-
# @Time    : 14.09.21 10:03
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : TOMTests.py
# @Software: PyCharm
import unittest
from core.security.Cryptography import Encrypt, Decrypt
import requests
import re
import json
class TOMTests(unittest.TestCase):
    def setUp(self):
        self.e = Encrypt()
        self.d = Decrypt()
        testText = "A quick brown fox jumps over the lazy dog"
        self.enc =  self.e.encrypt_aes(testText)

        self.JWT_URI_TEST = "http://0.0.0.0:5001/consent/broken-chain"
        self.JWT_LOGIN = "http://0.0.0.0:5001/jwt/login/"

    def test_enc_equal(self):
        testTexts = "A quick brown fox jumps over the lazy dog"
        self.assertEqual(self.e.encrypt_aes(testTexts),self.enc)

    def test_text_decrypt(self):
        long_text = "Conveying or northward offending admitting perfectly my. Colonel gravity get thought fat smiling add but. Wonder twenty hunted and put income set desire expect. Am cottage calling my is mistake cousins talking up. Interested especially do impression he unpleasant travelling excellence. All few our knew time done draw ask."

        long_text_enc = self.e.encrypt_aes(long_text.strip())

        self.assertEqual(str(self.d.decrypt_aes(long_text_enc).decode("utf-8")), long_text.strip())

    def test_access_without_JWT(self):
        dummy_data = {
              "consent_id": "TEST11091113454114545512",
              "reason": "pdf"
            }
        header = {"Content-Type": "application/json"}
        response = requests.post(self.JWT_URI_TEST,
                                 json=dummy_data)
        response = int(re.findall(r'\d+',str(response))[0])
        self.assertEqual(response, 500)

    def test_access_with_valid_JWT(self):
        login = {

            "password": "aa",
            "username": "aside"
        }
        response = requests.post(self.JWT_LOGIN,
                                 json=login)

        responseid = int(re.findall(r'\d+',str(response))[0])
        self.assertEqual(responseid, 200)
        access_token = json.loads(response.text)["access_token"]
        url = "http://0.0.0.0:5001/query/bulk-consent-id"

        result = requests.get(url,
                               headers={'Content-Type': 'application/json',
                                        'Authorization': 'Bearer {}'.format(access_token)})
        result_stat = True if "bindings" in result.text else False
        self.assertTrue(result_stat)

    def test_access_with_valid_token_unauthorised_role(self):
        consent = {
          "Agents": [

            {
              "id": "60a55c9dd79bc75769804113ea",
              "role": "controller"
            }
          ],
          "DataProcessing": [
            "storage",
          ],
          "GrantedAtTime": "2021-06-04T16:28:31.816Z",
          "Medium": "Online",
          "Purpose": "Marketing",
          "Resource": {
            "SensorDataCategory": [
              {
                "data": [
                  "speed"
                ]
              }
            ],
          },
          "city": "Innsbruck",
          "consentid": "TEST110911134541145455121",
          "country": "Austria",
          "dataprovider": "TESTCOMPLIANCEDP0023",
          "expirationTime": "2021-12-04T16:28:31.816Z",
          "state": "Tyrol"
        }

        login = {

            "password": "123das",
            "username": "luhapiaccessid"
        }
        response = requests.post(self.JWT_LOGIN,
                                 json=login)

        responseid = int(re.findall(r'\d+',str(response))[0])
        self.assertEqual(responseid, 200)
        access_token = json.loads(response.text)["access_token"]

        response_CREATE_CS = requests.post("http://127.0.0.1:5001/consent/create",
                                 json=consent,
                                headers={'Content-Type': 'application/json',
                                'Authorization': 'Bearer {}'.format(access_token)})
        responseid = int(re.findall(r'\d+', str(response_CREATE_CS))[0])
        self.assertEqual(responseid, 403)
        

    def test_minimisation_test_fail(self):
        consent = {
            "Phone": "004351250753449",
          "Agents": [

            {
              "id": "60a55c9dd79bc75769804113ea",
              "role": "controller"
            }
          ],
          "DataProcessing": [
            "storage",
          ],
          "GrantedAtTime": "2021-06-04T16:28:31.816Z",
          "Medium": "Online",
          "Purpose": "Marketing",
          "Resource": {
            "SensorDataCategory": [
              {
                "data": [
                  "speed"
                ]
              }
            ],
          },
          "city": "Innsbruck",
          "consentid": "TEST110911134541145455121",
          "country": "Austria",
          "dataprovider": "TESTCOMPLIANCEDP0023",
          "expirationTime": "2021-12-04T16:28:31.816Z",
          "state": "Tyrol"
        }

        login = {
            "password": "aa",
            "username": "aside"
        }
        response = requests.post(self.JWT_LOGIN,
                                 json=login)

        responseid = int(re.findall(r'\d+',str(response))[0])
        self.assertEqual(responseid, 200)
        access_token = json.loads(response.text)["access_token"]

        response_CREATE_CS_fail = requests.post("http://127.0.0.1:5001/consent/create",
                                 json=consent,
                                headers={'Content-Type': 'application/json',
                                'Authorization': 'Bearer {}'.format(access_token)})
        responseid = int(re.findall(r'\d+', str(response_CREATE_CS_fail))[0])
        self.assertEqual(responseid, 422)

    def test_minimisation_test_pass(self):
        import random
        id = random.randint(0,999999)
        consent = {
          "Agents": [

            {
              "id": "60a55c9dd79bc75769804113ea",
              "role": "controller"
            }
          ],
          "DataProcessing": [
            "storage",
          ],
          "GrantedAtTime": "2021-06-04T16:28:31.816Z",
          "Medium": "Online",
          "Purpose": "Marketing",
          "Resource": {
            "SensorDataCategory": [
              {
                "data": [
                  "speed"
                ]
              }
            ],
          },
          "city": "Innsbruck",
          "consentid": "TEST110911134541145455121",
          "country": "Austria",
          "dataprovider": "TESTCOMPLIANCEDP0023{}".format(id),
          "expirationTime": "2021-12-04T16:28:31.816Z",
          "state": "Tyrol"
        }

        login = {
            "password": "aa",
            "username": "aside"
        }
        response = requests.post(self.JWT_LOGIN,
                                 json=login)

        responseid = int(re.findall(r'\d+',str(response))[0])
        self.assertEqual(responseid, 200)
        access_token = json.loads(response.text)["access_token"]

        response_CREATE_CS_pass = requests.post("http://127.0.0.1:5001/consent/create",
                                 json=consent,
                                headers={'Content-Type': 'application/json',
                                'Authorization': 'Bearer {}'.format(access_token)})

        responseid = int(re.findall(r'\d+', str(response_CREATE_CS_pass))[0])
        self.assertEqual(responseid, 200)

        act_response = json.loads(response_CREATE_CS_pass.text)
        eval_true = True if "CONSENT_CREATION_SUCCESS" in act_response["decision"] else False
        self.assertTrue(eval_true)
        self.assertEqual(act_response["act_status_code"],7100)

if __name__ == '__main__':
    unittest.main(verbosity=2)