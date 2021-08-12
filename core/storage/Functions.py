# -*- coding: utf-8 -*-
# @Time    : 04.06.21 17:45
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : Functions.py
# @Software: PyCharm

import requests
import json
class Functions:
    def __init__(self):
        self.STORE = "https://openfaas.sti2.at/function/store"
        self.QUERY = "https://openfaas.sti2.at/function/query"


    def store(self, data):
        header = {"Content-Type": "application/json"} 
        response = requests.post(self.STORE,
                            headers=header,
                            json=data)
        return response.text

    def invoke_query_function(self, json_data):
        header = {"Content-Type": "application/json"}
        response = requests.get(self.QUERY,
                                json=json_data,
                                headers=header
                                )
        return json.loads(response.text)





