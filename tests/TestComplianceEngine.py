# -*- coding: utf-8 -*-
# @Time    : 09.05.21 22:17
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : TestComplianceEngine.py
# @Software: PyCharm

from core.ComplianceEngine import ComplianceEngine
import unittest
class TestComplianceEngine(unittest.TestCase):

    def setUp(self):
        self.cengine = ComplianceEngine()

    def test_smashHitmessage_grant(self):
        expected_decision = "GRANT"
        expected_decision_id = 5000
        from_ce = self.cengine.grant()
        self.assertEqual(expected_decision, from_ce["decision"])
        self.assertEqual(expected_decision_id, from_ce["status_consent"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
