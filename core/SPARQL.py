# -*- coding: utf-8 -*-
# @Time    : 12.05.21 15:28
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : SPARQL.py
# @Software: PyCharm
from core.smashHitmessages import smashHitmessages
from SPARQLWrapper import SPARQLWrapper, JSON,BASIC
from core.Functions import Functions
class  SPARQL(smashHitmessages, Functions):
    def __init__(self):
        super().__init__()
        self.HOST_URI = "https://smashhitactool.sti2.at/repositories/EarlyPrototypeKG"

    def init_sparql(self, hostname, userid, password):
        sparql = SPARQLWrapper(hostname)
        sparql.setCredentials(userid, password)
        return sparql

    def post_sparql(self,userid, password, query):
        hostname = "https://smashhitactool.sti2.at/repositories/EarlyPrototypeKG/statements"
        sparql = SPARQLWrapper(hostname)
        sparql.setHTTPAuth(BASIC)
        sparql.setCredentials(userid, password)
        sparql.setQuery(query)
        sparql.method = "POST"
        sparql.queryType = "INSERT"
        sparql.setReturnFormat('json')
        result = sparql.query()
        if str(result.response.read().decode("utf-8")) == "":
            message =  self.insert_success()
            record_success = self.store(message)
            if "SUCCESS" in record_success:
                return message
            else:
                message["message"] = "CONSENT creation success but decision logging error"
        else:
            return self.insert_fail()
