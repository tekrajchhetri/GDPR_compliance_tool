# -*- coding: utf-8 -*-
# @Time    : 12.05.21 15:28
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : SPARQL.py
# @Software: PyCharm

from core.smashHitmessages import smashHitmessages
from SPARQLWrapper import SPARQLWrapper, BASIC
from core.storage.Functions import Functions


class SPARQL(smashHitmessages, Functions):
    def __init__(self):
        super().__init__()
        self.HOST_URI = "https://smashhitactool.sti2.at/repositories/smashHitfinal"

    def init_sparql(self, hostname, userid, password):
        sparql = SPARQLWrapper(hostname)
        sparql.setCredentials(userid, password)
        return sparql

    def post_sparql(
        self,
        userid,
        password,
        query,
        consent_id_for_logging,
        type="insert",
        reason_for_logging="",
    ):
        hostname = (
            "https://smashhitactool.sti2.at/repositories/smashHitfinal/statements"
        )

        sparql = SPARQLWrapper(hostname)
        sparql.setHTTPAuth(BASIC)
        sparql.setCredentials(userid, password)
        sparql.setQuery(query)
        sparql.method = "POST"
        sparql.queryType = "INSERT"
        sparql.setReturnFormat("json")
        result = sparql.query()
        if str(result.response.read().decode("utf-8")) == "":

            if type == "revoke":
                message = self.revoke_consent_message()
                tolog = message
            if type == "broken_consent":
                message = self.revoke_consent_message()
                message["decision"] = "BROKEN_CONSENT_CHECK_SUCCESS"
                tolog = message
                tolog["reason"] = reason_for_logging
            if type == "insert":
                message = self.insert_success()
                tolog = message

            tolog["consent_id"] = consent_id_for_logging
            record_success = self.store(tolog)
            if "SUCCESS" in record_success:
                return message
            else:
                message[
                    "message"
                ] = "CONSENT creation success but decision logging error"
        else:
            return self.insert_fail()
