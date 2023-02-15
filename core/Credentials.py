# -*- coding: utf-8 -*-
# @Time    : 12.05.21 15:24
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : Credentials.py
# @Software: PyCharm
import os


class Credentials:
    def get_username(self):
        return os.environ.get("USERNAME")

    def get_password(self):
        return os.environ.get("PASSWORD")
