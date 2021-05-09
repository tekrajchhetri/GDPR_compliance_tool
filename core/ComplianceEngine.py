# -*- coding: utf-8 -*-
# @Time    : 09.05.21 21:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : ComplianceEngine.py
# @Software: PyCharm
from core.smashHitmessages import smashHitmessages
import json

class ComplianceEngine(smashHitmessages):
    def __init__(self):
        super().__init__()

    def print_message(self, message_dict_format):
        return json.dumps(message_dict_format)

if __name__ == '__main__':
    c = ComplianceEngine()
    print(c.print_message(c.grant()))


