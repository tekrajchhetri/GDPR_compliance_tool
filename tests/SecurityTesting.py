# -*- coding: utf-8 -*-
# @Time    : 01.07.21 18:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : SecurityTesting.py
# @Software: PyCharm

import unittest
from core.security.Cryptography import Encrypt, Decrypt
class SecurityTesting(unittest.TestCase):
    def setUp(self):
        self.e = Encrypt()
        self.d = Decrypt()
        testText = "A quick brown fox jumps over the lazy dog"
        self.enc =  self.e.encrypt_aes(testText)

    def test_enc_equal(self):
        testTexts = "A quick brown fox jumps over the lazy dog"
        for i in range(10):
            self.assertEqual(self.e.encrypt_aes(testTexts),self.enc)


if __name__ == '__main__':
    unittest.main(verbosity=2)