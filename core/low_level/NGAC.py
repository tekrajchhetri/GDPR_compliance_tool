# -*- coding: utf-8 -*-
# @Time    : 31.10.22 16:29
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : NGAC.py
# @Software: PyCharm

import requests
import json
class NGAC:
    def addControllerNGAC(self, _controller_id, _privacy_policy):
        _URL = "REST_ENDPOINT"

        _data={
            "token":"admin_token",
            "data_controller":f"dc[{_controller_id}]",
            "privacy_policy":_privacy_policy
        }

        _r = requests.post(_URL, data=_data)
        print(_r.text)
        return json.loads(_r.text)['respStatus']


    def addProcessorNGAC(self, _processor_id, _data_controller,_privacy_policy):
        _URL = "REST_ENDPOINT"

        _data = {
            "token": "admin_token",
            "data_processor": f"dp[{_processor_id}]",
            "data_controller": f"dc[{_data_controller}]",
            "privacy_policy": _privacy_policy
        }

        _r = requests.post(_URL, data=_data)
        print(_r.text)
        return json.loads(_r.text)['respStatus']


    def addDataSubjectNGAC(self, _data_subject_id,_privacy_preference,_data_items):
        _URL = "REST_ENDPOINT"

        _data = {
            "token": "admin_token",
            "data_subject": f"ds[{_data_subject_id}]",
            "privacy_preference": _privacy_preference,
            "data_items": _data_items
        }

        _r = requests.post(_URL, data=_data)
        print(_r.text)
        return json.loads(_r.text)['respStatus']
    
    def updateNGAC(self, requestedBy,hasDataController,hasDataProcessor, fordataprocessing, GrantedAtTime, inMedium, purpose,
                     isAboutData, city, consentID, country, state, dataprovider, expirationtime):

        yourprivacypoicy = "YYY"
        yourprivacy_preference="XXX"
        your_data_items="XXX"

        controller = self.addControllerNGAC(_controller_id=hasDataController, _privacy_policy=yourprivacypoicy)
        processor = self.addProcessorNGAC(_processor_id=hasDataProcessor,_data_controller=hasDataController,
                                          _privacy_policy=yourprivacypoicy)
        datasubject = self.addDataSubjectNGAC(_data_subject_id=dataprovider,
                                              _privacy_preference=yourprivacy_preference,
                                              _data_items=your_data_items)

        if 'failure' in [controller, processor, datasubject]:
            return "fail"
        else:
            return 'success'


        