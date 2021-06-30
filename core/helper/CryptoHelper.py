# -*- coding: utf-8 -*-
# @Time    : 29.06.21 20:38
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : CryptoHelper.py
# @Software: PyCharm

import os
class  CryptoHelper:

    def getCurrentDirectory(self):
        return os.path.abspath(os.getcwd())

    def get_pass_phrase(self):
        return os.environ.get("SECURITY_KEY_RSA")

    def directory_exists(self, directory):
        directory = f"{self.getCurrentDirectory()}/{directory}"
        isdir = os.path.isdir(directory)
        return isdir

    def get_directory_name(self):
        return "sec_public_private_key"

    def makedir(self, directory="sec"):
        isdir = self.directory_exists(directory)
        if not isdir:
            try:
                success = os.mkdir(f"{self.getCurrentDirectory()}/{directory}")
                return True if success is None else False
            except:
                pass
        return False



    def write_file(self, filename, data):
        try:
            file_out = open(filename, "wb")
            file_out.write(data)
            file_out.close()
        except:
            pass

    def file_exists(self, filename):
        try:
            filematched = [s for s in [x.lower() for x in os.listdir()] if filename.lower() in s]
        except:
            pass
        return True if len(filematched) == 1 else False






