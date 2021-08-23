# -*- coding: utf-8 -*-
# @Time    : 09.05.21 21:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : ComplianceEngine.py
# @Software: PyCharm
from core.query_processor.QueryProcessor import QueryEngine
from  core.helper.date_helper import DateHelper
import json
import requests
class ComplianceEngine(QueryEngine, DateHelper):
    def __init__(self):
        super().__init__()
        self.TRIGGER_URL_NOTIFY = "http://127.0.0.1:5056/notify"

    def broken_consent(self, consentID, reason_for_logging):
        if len(reason_for_logging.strip()) < 2:
            return self.dataformatnotmatch()
        if self.check_active_granted_consent(consentID=consentID):
            respone = self.post_sparql(userid=self.get_username(), password=self.get_password(),
                                       query=self.revoke_broken_consent_query(consentID=consentID,type="BROKEN_CONSENT"),
                                       consent_id_for_logging=consentID, reason_for_logging= reason_for_logging,
                                       type="broken_consent"
                                       )
            return respone
        else:
            return self.processing_fail_message()



    def revoke_consent(self, consentID):
        if self.check_active_granted_consent(consentID=consentID):
            respone = self.post_sparql(userid=self.get_username(), password=self.get_password(),
                                       query=self.revoke_broken_consent_query(consentID=consentID),
                                       consent_id_for_logging=consentID, type="revoke")
            return respone
        else:
            return self.processing_fail_message()

    def compliance_check_act(self):
        pass

    def compliance_check_spc(self):
        pass


    def joint_compliance(self, act_compliance, spc_compliance):
        """
        :param act_compliance: Compliance check information (or decision) from ACT
        :param spc_compliance: Compliance check information (or decision) from Security and Privacy Component
        :return:
        """
        pass

    def get_consent_data(self):
        all_consent  = self.select_query_gdb(additionalData="consent_for_compliance")
        return json.loads(all_consent)



    def check_consent_expiry(self):
        consent_datas = self.get_consent_data()
        for consent_data in consent_datas["results"]["bindings"]:
            cid = self.remove_uris(consent_data["ConsentID"]["value"])
            exp_date = self.remove_xst_date(self.decrypt_data(
                               self.remove_uris(consent_data["Duration"]["value"])))
            if(self.has_expired(exp_date)):
                header = {"Content-Type": "application/json"}
                data = json.dumps({"CID":cid,"status":"Expired"})
                r = requests.post(self.TRIGGER_URL_NOTIFY, data=data, headers=header)
                msg = json.loads(r.text)
                msg["consent_id"] = cid
                self.store(msg)




if __name__ == '__main__':
    ce = ComplianceEngine()
    ce.check_consent_expiry()
