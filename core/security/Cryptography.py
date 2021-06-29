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

    def initKey(self):
        return RSA.generate(4096)

    def generate_public(self):
        keyfile = self.initKey()
        self.generate_private(keyfile=keyfile)
        public_key = keyfile.publickey().export_key()
        directory = "sec_public_key"
        file = f"{directory}.pem"
        if self.makedir(directory):
            self.write_file(f"{self.getCurrentDirectory()}/{directory}/{file}", public_key)

        if not self.makedir(directory) and not self.file_exists(file):
                self.write_file(f"{self.getCurrentDirectory()}/{directory}/{file}", public_key)


    def generate_private(self, keyfile):
        private_key = keyfile.export_key()
        directory = "sec_key_private"
        file = f"{directory}.pem"
        if self.makedir(directory):
             self.write_file(f"{self.getCurrentDirectory()}/{directory}/{file}", private_key)

        if not self.makedir(directory) and not self.file_exists(file):
                self.write_file(f"{self.getCurrentDirectory()}/{directory}/{file}", private_key)

    def generate_key(self):
        self.generate_public()




