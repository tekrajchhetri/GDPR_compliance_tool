# -*- coding: utf-8 -*-
# @Time    : 29.06.21 15:53
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : Cryptography.py
# @Software: PyCharm
from Crypto.PublicKey import RSA
from core.helper.CryptoHelper import CryptoHelper
import base64
from Crypto.Cipher import  PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import re
class KeyGeneration(CryptoHelper):
    def __int__(self):
        super.__int__(self)

    def initKey(self):
        return RSA.generate(4096)

    def generate_asymetric_key(self, keyfile):
        directory = self.get_directory_name()
        encrypted_key = keyfile.export_key(passphrase=self.get_pass_phrase(), pkcs=8,
                                       protection="scryptAndAES128-CBC")

        if self.makedir(directory):
            self.write_file(self.get_full_file_path_name(), encrypted_key)

        if not self.makedir(directory) and not self.file_exists(self.get_full_file_path_name()):
                self.write_file(self.get_full_file_path_name(), encrypted_key)


    def generate_key(self):
        keyfile = self.initKey()
        self.generate_asymetric_key(keyfile=keyfile)

class KeyObject:
    def get_key(self):
        ch = CryptoHelper()
        encoded_key = open(ch.get_full_file_path_name(), "rb").read()
        return  RSA.import_key(encoded_key, passphrase=ch.get_pass_phrase())

class Encrypt(KeyObject):
    def escape_special_character(self, data):
        pattern_regex = r"[ -\/:-@\[-\`{-~]"
        return re.sub(r'([\'\"\=\/\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', r'\\\1', str(data.decode("utf-8")))

    def encrypt(self,  data):
        data =str(data).encode("utf-8")
        key =  self.get_key()
        cipher_rsa = PKCS1_OAEP.new(key)
        encd_data = cipher_rsa.encrypt(data)
        return  self.escape_special_character(base64.b64encode(encd_data))

class Decrypt(KeyObject):
    def decrypt(self, encrypted_data):
        key = self.get_key()
        cipher_rsa = PKCS1_OAEP.new(key)
        decrypted_data = cipher_rsa.decrypt(base64.b64decode(encrypted_data))
        return decrypted_data







