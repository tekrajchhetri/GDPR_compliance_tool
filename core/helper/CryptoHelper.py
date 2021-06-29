# -*- coding: utf-8 -*-
# @Time    : 29.06.21 20:38
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : CryptoHelper.py
# @Software: PyCharm

import os
class  CryptoHelper:

    def __init__(self):
        self.directory_name = "sec"
        self.directory = f"{self.getCurrentDirectory()}/{self.directory_name}"

    def getCurrentDirectory(self):
        return os.path.abspath(os.getcwd())

    def directory_exists(self):
        isdir = os.path.isdir(self.directory)
        return isdir

    def makedir(self):
        isdir = self.directory_exists()
        if not isdir:
            os.mkdir(self.directory)
            return True
        else:
            return False

    def is_correct_type(self, filename):
        return filename.split(".")[1] == "pem"


    def file_exists(self, filename):
        if self.is_correct_type(filename):
            if self.directory_exists():
                filepath = f"{self.directory}/{filename}"
                return os.path.isfile(filepath)
        return False
