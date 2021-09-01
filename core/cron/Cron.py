# -*- coding: utf-8 -*-
# @Time    : 23.08.21 17:29
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : Cron.py.py
# @Software: PyCharm
from core.compliance.ComplianceEngine import ComplianceEngine

class Cron():

    def __init__(self):
        self.ce = ComplianceEngine()

    def automated_compliance(self):
        #call list of automated compliance check
        self.ce.compliance_check_act(level="all")



if __name__ == '__main__':
    # perform compliance check on X intervals as set in  ofelia
    crons = Cron()
    crons.automated_compliance()
