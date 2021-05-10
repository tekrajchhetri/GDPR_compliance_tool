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
        decision =  {"status_consent":5000,
                                "decision":"GRANT",
                                "decision_token":self.token_generator()
                                }

        return decision

    def deny(self):
        deny = {"status_consent": 6000,
                           "decision": "DENY",
                           "decision_token":self.token_generator()
                           }
        return deny

    def deny_incomplete(self):
        deny_incomplete = {"status_consent": 6100,
                           "decision": "DENY",
                           "decision_token":self.token_generator()}

        return deny_incomplete