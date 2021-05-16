# -*- coding: utf-8 -*-
# @Time    : 09.05.21 21:47
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : smashHitmessages.py
# @Software: PyCharm

from core.Token import TokenGenerator

class smashHitmessages(TokenGenerator):

    def __init__(self):
        super().__init__()

    def grant(self):
        decision =  {"status_code":5000,
                                "decision":"GRANT",
                                "decision_token":self.token_generator(),
                                "timestamp":self.decision_timestamp()
                                }

        return decision

    def deny(self):
        deny = {"status_code": 6000,
                           "decision": "DENY",
                           "decision_token":self.token_generator(),
                            "timestamp": self.decision_timestamp()
                           }
        return deny

    def deny_incomplete(self):
        deny_incomplete = {"status_code": 6100,
                           "decision": "DENY",
                           "decision_token":self.token_generator(),
                           "timestamp":self.decision_timestamp()
                           }

        return deny_incomplete

    def insert_success(self):
        deny_incomplete = {"status_code": 7100,
                           "decision": "RECORD_CREATION_SUCCESS",
                           "decision_token":self.token_generator(),
                           "timestamp":self.decision_timestamp()
                           }

        return deny_incomplete

    def insert_fail(self):
        deny_incomplete = {"status_code": 7100,
                           "decision": "RECORD_CREATION_FAILURE",
                           "decision_token":self.token_generator(),
                           "timestamp":self.decision_timestamp()
                           }

        return deny_incomplete
