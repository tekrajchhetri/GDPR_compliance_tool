# -*- coding: utf-8 -*-
# @Time    : 31.10.22 16:29
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : NGAC.py
# @Software: PyCharm

import json
import time
import asyncio
import requests
import aiohttp
from requests.models import PreparedRequest


class NGAC:

    def addControllerNGAC(self, token, _controller_id, _privacy_policy):
        _URL = "YOURENDPOINT/dplp/add_data_controller"

        payload = {
            "token": token,
            "data_controller": f"dc[{_controller_id}]",
            "privacy_policy": []
        }
        _r = requests.post(_URL, data=payload)
        print("####################addControllerNGAC#############################")
        print(payload, _r.text)
        print("####################addControllerNGAC_END#############################")

        return json.loads(_r.text)['respStatus']

    def addApplicationNGAC(self, token, _controller_id, _processor_id, operations):
        _URL = "YOURENDPOINT/dplp/add_application"

        payload = {
            "token": token,
            "application": f"dp[{_processor_id}][{_controller_id}]_appl",
            "data_processor": f"dp[{_processor_id}][{_controller_id}]",
            "operations": str(operations),
            # "policy":"dplp_min"
        }
        print("####################Application#############################")
        _r = requests.post(_URL, data=payload)
        print("####################Application#############################")
        print(payload, _r.text)
        print("####################addControllerNGAC_END#############################")
        return json.loads(_r.text)['respStatus']

    def addProcessorNGAC(self, token, _processor_id, _data_controller, _privacy_policy):
        _URL = "YOURENDPOINT/dplp/add_data_processor"

        payload = {
            "token": token,
            "data_processor": f"dp[{_processor_id}][{_data_controller}]",
            "data_controller": f"dc[{_data_controller}]",
            "privacy_policy": "[]"
        }
        _r = requests.post(_URL, data=payload)
        print("####################addProcessor#############################")
        print(payload, _r.text)
        print("####################addProcessor_END#############################")

        return json.loads(_r.text)['respStatus']

    def addDataSubjectNGAC(self, token, _data_subject_id, _privacy_preference, _data_items):
        _URL = "YOURENDPOINT/dplp/add_data_subject"

        payload = {
            "token": "admin_token",
            # "policy": "dplp_min",
            "data_subject": f"ds[{_data_subject_id}]",  # 'ds[123BVC112]',
            "data_items": _data_items,  # "['pdi(123BVC112)[123BVC112]':'Birth Date']",
            "privacy_preference": "[]",
        }

        _r = requests.post(_URL, data=payload)
        print("####################addDS#############################")
        print(payload, _r.text)
        print("####################addDS_END#############################")
        return json.loads(_r.text)['respStatus']

    def addConsentNGAC(self, token, consent_id,
                       _processor_id, _data_controller,
                       dataprocessingoperations, purpose,
                       _data_subject_id, _privacy_preference, constraint):
        _URL = "YOURENDPOINT/dplp/add_consent"

        payload = {
            "token": token,
            # "policy": _privacy_preference,
            "consent_id": f"C{consent_id}",
            "data_controller": f'dc[{_data_controller}]',
            "data_processor": f"dp[{_processor_id}][{_data_controller}]",
            "application": f"dp[{_processor_id}][{_data_controller}]_appl",
            "operations": str([f"dp[{_processor_id}][{_data_controller}]_appl"]),
            "purpose": f"{purpose}",
            "data_subject": f"ds[{_data_subject_id}]",
            "data_item": f"pdi({_data_subject_id})[{_data_subject_id}]",  #:\'Birth Date\'",
            "data_category": "Birth Date",
            "constraint": "true"
        }
        print("####################addConsentNGAC#############################")
        print(payload)
        print("####################addConsentNGAC_END#############################")
        _r = requests.post(_URL, data=payload)
        print(f"revocation {_r.text}")
        return json.loads(_r.text)['respStatus']
        # async with session.post(_URL,
        #                 data=payload) as resp:
        #                 data = await resp.text()
        #                 print(data)
        #                 return json.loads(data)['respStatus']

    def updateRevokation(self, token, _privacy_preference, consent_id):
        _URL = "YOURENDPOINT/dplp/delete_consent"

        payload = {
            "token": token,
            "policy": _privacy_preference,
            "consent_id": f"C{consent_id}",
        }
        _r = requests.post(_URL, data=payload)
        print(payload)
        print(f"revocation {_r.text}")
        return json.loads(_r.text)['respStatus']

    def resetpolicy(self, token):
        _URL = "YOURENDPOINT/paapi/reset"

        payload = {
            "token": token,
            "name": "dplp_min",
            "domain": "policy",
        }
        # print(f"############################## RESET POLICY OK ##############################")
        # print(f"{payload}")
        _r = requests.post(_URL, data=payload)
        print(_r)
        return json.loads(_r.text)['respStatus']

    def add_data_item(self, token, _data_subject_id):
        _URL = "YOURENDPOINT/dplp/add_data_item"

        payload = {
            "token": token,
            "data_item": f"pdi({_data_subject_id})[{_data_subject_id}]",
            "data_category": "Birth Date",
            "data_subject": f"ds[{_data_subject_id}]"
        }
        # print(f"############################## ADD data Items ++++++++++ ##############################")
        print(f"{payload}")
        _r = requests.post(_URL, data=payload)
        print(_r.text)
        # print(f"############################## ADD data Items ##############################")
        return json.loads(_r.text)['respStatus']

    def setpolicy(self, token, _privacy_preference):
        _URL = "YOURENDPOINT/paapi/setpol"

        payload = {
            "token": token,
            "policy": _privacy_preference,
        }

        #

        _r = requests.post(_URL, data=payload)
        print(f"############################## SET POLICY OK ##############################")
        print(f"{payload}, {_r.text}")
        print(f"############################## SET POLICY OK ##############################")
        return json.loads(_r.text)['respStatus']

    def add_dplp_policy_base(self, token):
        _URL = "YOURENDPOINT/dplp/add_dplp_policy_base"

        payload = {
            "token": token,
            "policy_class": "pc",
            "policy": "dplp_min",
            "definitions": "smashHitCore202210"
        }

        _r = requests.post(_URL, data=payload)
        print(f"############################## POLICY BASE  ##############################")
        print(f"{payload}, {_r.text}")
        print(f"############################## POLICYend  BASE  ##############################")
        return json.loads(_r.text)['respStatus']

    def check_access_permission(self, purpose, hasDataProcessor, dataprovider, hasDataController, fordataprocessing,
                                token="admin_token"):

        _URLP = f'YOURENDPOINT/paapi/getpol?token={token}'
        _rP = requests.get(_URLP)
        _privacy_preference = json.loads(_rP.text)['respBody'] if len(
            json.loads(_rP.text)['respBody']) > 4 else 'dplp_min'
        results = []
        _URLacess = 'YOURENDPOINT/pqapi/access'
        for x in fordataprocessing:

            payload = {
                "user": f"dp[{hasDataProcessor}][{hasDataController}]",
                "ar": x,
                "purpose": purpose,  # f"p({purpose})",
                # "policy": _privacy_preference,
                "object": f"pdi({dataprovider})[{dataprovider}]"
            }
            _r = requests.get(_URLacess, params=payload)
            # print(_r.text)
            try:
                results.append(json.loads(_r.text)['respMessage'])
            except Exception as ex:
                pass
        print(results)
        if "failure" in results:
            return "deny"
        else:
            return "grant"

    def getpolicy(self, yourtoken):
        _URLP = f'YOURENDPOINT/paapi/getpol?token={yourtoken}'
        _rP = requests.get(_URLP)
        yourprivacypoicy = json.loads(_rP.text)['respBody'] if len(json.loads(_rP.text)['respBody']) > 4 else 'dplp_min'
        return yourprivacypoicy

    def updateNGAC(self, requestedBy, hasDataController, hasDataProcessor, fordataprocessing, GrantedAtTime, inMedium,
                   purpose,
                   isAboutData, city, consentID, country, state, dataprovider, expirationtime):

        yourtoken = "admin_token"
        domain = "policy"
        _URLP = f'YOURENDPOINT/paapi/getpol?token={yourtoken}'
        _rP = requests.get(_URLP)
        yourprivacypoicy = self.getpolicy(
            "admin_token")  # json.loads(_rP.text)['respBody'] if len(json.loads(_rP.text)['respBody'])>4 else 'dplp_min'
        yourprivacy_preference = "[]"
        your_data_items = [f"\'pdi({dataprovider})[{dataprovider}]\':\'Birth Date\'"]
        yourapplication = "[]"
        yourconstraint = "true"

        now = time.time()
        resetp = self.resetpolicy(token=yourtoken)
        setp = self.setpolicy(token=yourtoken, _privacy_preference=yourprivacypoicy)

        adddplp = self.add_dplp_policy_base(token=yourtoken)

        addDS = self.addDataSubjectNGAC(token=yourtoken, _data_subject_id=dataprovider,
                                        _privacy_preference=yourprivacypoicy,
                                        _data_items=your_data_items)

        addCont = self.addControllerNGAC(token=yourtoken, _controller_id=hasDataController,
                                         _privacy_policy=yourprivacypoicy),

        addprocess = self.addProcessorNGAC(token=yourtoken, _processor_id=hasDataProcessor,
                                           _data_controller=hasDataController,
                                           _privacy_policy=yourprivacypoicy)

        addApplication = self.addApplicationNGAC(token=yourtoken, _processor_id=hasDataProcessor,
                                                 _controller_id=hasDataController, operations=fordataprocessing)

        adddataItem = self.add_data_item(token=yourtoken, _data_subject_id=dataprovider)

        print("########--", adddataItem)

        addconsent = self.addConsentNGAC(token=yourtoken,
                                         _privacy_preference=yourprivacypoicy,
                                         consent_id=consentID,
                                         _processor_id=hasDataProcessor,
                                         _data_controller=hasDataController,
                                         _data_subject_id=dataprovider,
                                         dataprocessingoperations=fordataprocessing,
                                         purpose=purpose,
                                         constraint=yourconstraint
                                         )
        print(addconsent, "------------")
        results = [resetp, setp, adddplp, addDS, addCont, addprocess, addApplication, adddataItem, addconsent]
        time_taken = time.time() - now

        if 'failure' in results:
            return "fail", time_taken
        else:
            return 'success', time_taken
