# -*- coding: utf-8 -*-
# @Time    : 29.06.21 15:53
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : Cryptography.py
# @Software: PyCharm
from Crypto.PublicKey import RSA
from core.helper.CryptoHelper import CryptoHelper

class KeyGeneration(CryptoHelper):
    def __int__(self):
        super.__int__(self)

    def generate(self):
        dir = self.makedir()
        if dir:
            key = RSA.generate(2048)
            private_key = key.export_key()
            file_out = open(f"{self.directory}/private_key.pem", "wb")
            file_out.write(private_key)
            file_out.close()
            public_key = key.publickey().export_key()
            file_out = open(f"{self.directory}/public_key.pem", "wb")
            file_out.write(public_key)
            file_out.close()


