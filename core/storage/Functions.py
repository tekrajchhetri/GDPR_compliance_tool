# -*- coding: utf-8 -*-
# @Time    : 04.06.21 17:45
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : Functions.py
# @Software: PyCharm

import requests
class Functions:
    def __init__(self):
        self.STORE = "https://openfaas.sti2.at/function/store"

    def store(self, data):
        header = {"Content-Type": "application/json"} 
        response = requests.post(self.STORE,
                            headers=header,
                            json=data)
        return response.text





