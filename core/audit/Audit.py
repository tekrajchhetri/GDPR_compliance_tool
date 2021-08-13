# -*- coding: utf-8 -*-
# @Time    : 06.07.21 19:13
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : Audit.py
# @Software: PyCharm
import json
import pymongo
from core.query_processor.QueryProcessor import QueryEngine
from core.storage.Functions import Functions
class Audit:
    def __init__(self):
        self.qe = QueryEngine()


    def consent_id_to_list(self, retrieved_consentID):
        to_match_cid = []
        for consent_id in retrieved_consentID["bindings"]:
            to_match_cid.append(consent_id["ConsentID"]["value"].split("#")[1])
        return to_match_cid


    def audit_all_consent_by_dp(self, data_provider_id,level_of_details):
        """ Fetch all the details about the consent, decision for auditing purpose
        :param data_provider: unique data provider ID
        :param details_level:
                        Partial: Only fetches the decision details. It includes details about consent ID, decision token,
                        the datetime information particular to the data_provider
                        Full: fetch complete details about all the given consent as well as the decision information.
        :return: JSON response with fetched details
        """
        all_consentID = self.qe.select_query_gdb(consentProvidedBy=data_provider_id, purpose=None, dataProcessing=None,
                                                 dataController=None, dataRequester=None, additionalData="consentID")
        to_match_cid = self.consent_id_to_list(json.loads(all_consentID)["results"])
        data = {"query_type": "all", "consent_id_list": to_match_cid}
        faas_Call = Functions()
        response = faas_Call.invoke_query_function(json_data=data)

        if level_of_details=="partial":
            audit_success_message = self.qe.audit_success()
            formatted_decision = {"data_provider":data_provider_id, "consent_decision":response}
            audit_success_message["message"] = formatted_decision
            return audit_success_message
        elif level_of_details == "full":
            return self.qe.audit_success()
        else:
            return self.qe.dataformatnotmatch()



    def audit_all_active_consent(self):
        pass

