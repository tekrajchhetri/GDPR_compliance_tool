# -*- coding: utf-8 -*-
# @Time    : 09.05.21 21:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : ComplianceEngine.py
# @Software: PyCharm
from core.query_processor.QueryProcessor import QueryEngine


class ComplianceEngine(QueryEngine):
    def __init__(self):
        super().__init__()

    def broken_consent(self, consentID, reason_for_logging):
        if len(reason_for_logging.strip()) < 2:
            return self.dataformatnotmatch()
        if self.check_active_granted_consent(consentID=consentID):
            respone = self.post_sparql(self.get_username(), self.get_password(),
                                       self.revoke_broken_consent_query(consentID=consentID,type="BROKEN_CONSENT"),
                                       reason_for_logging= reason_for_logging, type="broken_consent")
            return respone
        else:
            return self.processing_fail_message()



    def revoke_consent(self, consentID):
        if self.check_active_granted_consent(consentID=consentID):
            respone = self.post_sparql(self.get_username(), self.get_password(),
                                       self.revoke_broken_consent_query(consentID=consentID), type="revoke")
            return respone
        else:
            return self.processing_fail_message()

