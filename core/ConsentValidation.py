# -*- coding: utf-8 -*-
# @Time    : 17.05.21 14:07
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : ConsentValidation.py
# @Software: PyCharm
from core.date_helper import DateHelper
import dask
class  ConsentValidation(DateHelper):

    def __init__(self):
        super().__init__()


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
