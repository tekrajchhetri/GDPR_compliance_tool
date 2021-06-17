# -*- coding: utf-8 -*-
# @Time    : 09.05.21 22:17
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : TestComplianceEngine.py
# @Software: PyCharm

from core.compliance.ComplianceEngine import ComplianceEngine
import unittest
class TestComplianceEngine(unittest.TestCase):

    def setUp(self):
        self.cengine = ComplianceEngine()

    def test_smashHitmessage_grant(self):
        expected_decision = "GRANT"
        expected_decision_id = 5000
        from_ce = self.cengine.grant()
        self.assertEqual(expected_decision, from_ce["decision"])
        self.assertEqual(expected_decision_id, from_ce["status_code"])

    def test_smashHitmessage_deny(self):
        expected_decision = "DENY"
        expected_decision_id = 6000
        from_ce = self.cengine.deny()
        self.assertEqual(expected_decision, from_ce["decision"])
        self.assertEqual(expected_decision_id, from_ce["status_code"])

    def test_smashHitmessage_deny_incomplete(self):
        expected_decision = "DENY"
        expected_decision_id = 6100
        from_ce = self.cengine.deny_incomplete()
        self.assertEqual(expected_decision, from_ce["decision"])
        self.assertEqual(expected_decision_id, from_ce["status_code"])



if __name__ == '__main__':
    unittest.main(verbosity=2)
