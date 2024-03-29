# -*- coding: utf-8 -*-
# @Time    : 09.05.21 21:47
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : smashHitmessages.py
# @Software: PyCharm

from core.Token import TokenGenerator


class smashHitmessages(TokenGenerator):
    def __init__(self):
        super().__init__()

    def grant(self):
        decision = {
            "act_status_code": 5000,
            "decision": "GRANT",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return decision

    def deny(self):
        deny = {
            "act_status_code": 6000,
            "decision": "DENY",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }
        return deny

    def deny_incomplete(self):
        deny_incomplete = {
            "act_status_code": 6100,
            "decision": "DENY_INCOMPLETE",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return deny_incomplete

    def insert_success(self):
        insert_success = {
            "act_status_code": 7100,
            "decision": "CONSENT_CREATION_SUCCESS",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return insert_success

    def audit_success(self):
        audit_success = {
            "act_status_code": 7200,
            "decision": "AUDIT_SUCCESS",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return audit_success

    def insert_fail(self):
        deny_incomplete = {
            "act_status_code": 7500,
            "decision": "RECORD_CREATION_FAILURE",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return deny_incomplete

    def dataformatnotmatch(self):
        deny_incomplete = {
            "act_status_code": 8500,
            "decision": "DATA_FORMAT_ERROR",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return deny_incomplete

    def revoke_consent_message(self):
        revoke_consent = {
            "act_status_code": 8000,
            "decision": "CONSENT_REVOCATION_SUCCESS",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return revoke_consent

    def compliance_message(self):
        compliance_message = {
            "act_status_code": 9000,
            "decision": "COMPLIANCE_STATUS",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return compliance_message

    def compliance_obligation_notification_message(self):
        compliance_message = {
            "act_status_code": 9900,
            "decision": "COMPLIANCE_OBLIGATION_STATUS_NOTIFICATION_RECEIVED",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return compliance_message

    def processing_fail_message(self):
        revoke_consent = {
            "act_status_code": 8200,
            "decision": "FAILED",
            "message": "Processing failed, check input",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return revoke_consent

    def jwt_invalid_message(self):
        revoke_consent = {
            "act_status_code": 8900,
            "decision": "FAILED",
            "message": "JWT invalid / Unauthorized",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return revoke_consent

    # this error means something has changed in the code, leading to the occurance of error
    def token_expired(self):
        error = {
            "act_status_code": 8910,
            "decision": "FAILED",
            "message": "Token Expired / No Token Present",
            "decision_token": self.token_generator(),
            "timestamp": self.decision_timestamp(),
        }

        return error
