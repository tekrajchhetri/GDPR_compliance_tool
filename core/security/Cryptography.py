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

    def generate_asymetric_key(self, keyfile):
        directory = self.get_directory_name()
        encrypted_key = keyfile.export_key(passphrase=self.get_pass_phrase(), pkcs=8,
                                       protection="scryptAndAES128-CBC")
        file = f"{directory}.bin"
        if self.makedir(directory):
            self.write_file(f"{self.getCurrentDirectory()}/{directory}/{file}", encrypted_key)

        if not self.makedir(directory) and not self.file_exists(file):
                self.write_file(f"{self.getCurrentDirectory()}/{directory}/{file}", encrypted_key)



    def generate_key(self):
        keyfile = self.initKey()
        self.generate_asymetric_key(keyfile=keyfile)







