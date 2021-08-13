# -*- coding: utf-8 -*-
# @Time    : 09.05.21 21:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : ComplianceEngine.py
# @Software: PyCharm
from core.query_processor.QueryProcessor import QueryEngine
import dask

class ComplianceEngine(QueryEngine):
    def __init__(self):
        super().__init__()

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
        pass

    def process_data_for_expiry_check(self, data):
        pass

    def check_consent_expiry(self):
        pass

    def parallelise(self):
        consent_data = self.get_consent_data()
        for i in range(len(consent_data)):
            processdata = dask.delayed(self.get_consent_data)(consent_data[i]).compute()
            check_consent_expiry = dask.delayed(self.check_consent_expiry)(processdata[0],processdata[1],processdata[2]).compute()


