# -*- coding: utf-8 -*-
# @Time    : 29.06.21 15:53
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : Cryptography.py
# @Software: PyCharm

from Crypto.PublicKey import RSA
from core.helper.CryptoHelper import CryptoHelper
import base64
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad
import math
import re


class KeyGeneration(CryptoHelper):
    def __int__(self):
        super.__int__(self)

    def initKey(self):
        return RSA.generate(2048)

    def write_into_file_after_cond_check(self, type, directory, encrypted_data):

        if self.makedir(directory):
            self.write_file(self.get_full_file_path_name(type=type), encrypted_data)

        if not self.makedir(directory) and not self.file_exists(
            self.get_full_file_path_name(type=type)
        ):
            self.write_file(self.get_full_file_path_name(type=type), encrypted_data)

    def generate_rsa_key(self, keyfile):
        directory = self.get_directory_name()
        encrypted_key = keyfile.export_key(
            passphrase=self.get_pass_phrase(), pkcs=8, protection="scryptAndAES128-CBC"
        )
        self.write_into_file_after_cond_check(
            type="rsa", directory=directory, encrypted_data=encrypted_key
        )

    def generate_sec_key(self):
        secKey = []
        directory = self.get_directory_name()
        encryptObj = Encrypt()
        for i in range(1):
            secKey.append(encryptObj.encrypt_rsa(self.generate_random__sec_key(32)))

        self.write_into_file_after_cond_check(
            type="secret", directory=directory, encrypted_data=secKey
        )

    def generate_random__sec_p(self):
        secP = []
        directory = self.get_directory_name()
        encryptObj = Encrypt()
        for i in range(1):
            P = self.generate_random__sec_keyP()
            secP.append(encryptObj.encrypt_rsa(P.to_bytes(16, "big")))

        self.write_into_file_after_cond_check(
            type="random", directory=directory, encrypted_data=secP
        )

    def generate_iv_key(self):
        ivKey = []
        directory = self.get_directory_name()
        encryptObj = Encrypt()
        for i in range(1):
            ivKey.append(encryptObj.encrypt_rsa(self.generate_random__sec_key(16)))
        self.write_into_file_after_cond_check(
            type="four", directory=directory, encrypted_data=ivKey
        )

    def generate_key(self):
        keyfile = self.initKey()
        self.generate_rsa_key(keyfile=keyfile)
        self.generate_sec_key()
        self.generate_iv_key()
        self.generate_random__sec_p()


class KeyObject:
    def get_key(self):
        ch = CryptoHelper()
        fh = open(ch.get_full_file_path_name(type="rsa"), "rb")
        encoded_key = fh.read()
        fh.close()
        return RSA.import_key(encoded_key, passphrase=ch.get_pass_phrase())


class Encrypt(KeyObject):
    def escape_special_character(self, data):
        pattern_regex = r"[ -\/:-@\[-\`{-~]"
        return re.sub(
            r"([\'\"\=\/\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])",
            r"\\\1",
            str(data.decode("utf-8")),
        )

    def encrypt_rsa(self, data):
        key = self.get_key()
        cipher_rsa = PKCS1_OAEP.new(key)
        encd_data = cipher_rsa.encrypt(data)
        return encd_data

    def encrypt_aes(self, data):
        ##Fix issue - plain text size multiple of len(iv)
        data_multiple16 = 16 - (len(data) % 16)
        datafix = data + " " * data_multiple16
        encdata = str(datafix).encode("utf-8")
        ch = CryptoHelper()
        dec = Decrypt()
        secretf = ch.get_full_file_path_name(type="secret")
        secret = ch.read_pickle_file(secretf)
        fourf = ch.get_full_file_path_name(type="four")
        iv = ch.read_pickle_file(fourf)
        for i in range(len(secret)):
            cipher_aes = AES.new(
                dec.decrypt_rsa(secret[i]), AES.MODE_EAX, dec.decrypt_rsa(iv[i])
            )
            encdata = cipher_aes.encrypt(encdata)
        return self.escape_special_character(base64.b64encode(encdata))


class Decrypt(KeyObject):
    def decrypt_rsa(self, encrypted_data):
        key = self.get_key()
        cipher_rsa = PKCS1_OAEP.new(key)
        decrypted_data = cipher_rsa.decrypt(encrypted_data)
        return decrypted_data

    def decrypt_aes(self, encrypted_data):
        chipertext = base64.b64decode(encrypted_data)
        ch = CryptoHelper()
        dec = Decrypt()
        secretf = ch.get_full_file_path_name(type="secret")
        secret = ch.read_pickle_file(secretf)
        fourf = ch.get_full_file_path_name(type="four")
        iv = ch.read_pickle_file(fourf)
        for i in [0]:
            cipher_aes = AES.new(
                dec.decrypt_rsa(secret[i]), AES.MODE_EAX, dec.decrypt_rsa(iv[i])
            )
            chipertext = cipher_aes.decrypt(chipertext)
        return chipertext.strip()
