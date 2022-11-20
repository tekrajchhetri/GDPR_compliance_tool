# -*- coding: utf-8 -*-
# @Time    : 08.05.21 11:56
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : Token.py
# @Software: PyCharm

import datetime
import hashlib


class TokenGenerator:
    def decision_timestamp(self):
        return datetime.datetime.utcnow().timestamp()

    def token_generator(self):
        return hashlib.sha512(
            str(datetime.datetime.timestamp(datetime.datetime.now())).encode("utf-8")
        ).hexdigest()
