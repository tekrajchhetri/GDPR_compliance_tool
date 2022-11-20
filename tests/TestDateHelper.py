# -*- coding: utf-8 -*-
# @Time    : 09.05.21 19:09
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : TestDateHelper.py
# @Software: PyCharm
from core.helper.date_helper import DateHelper
import unittest
import datetime


class TestDateHelper(unittest.TestCase):
    def setUp(self):
        self.dthelper = DateHelper()

    def test_helper_extract_days(self):
        self.assertEqual(self.dthelper.helper_extract_days("10day"), 10)
        self.assertEqual(self.dthelper.helper_extract_days("10 days"), 10)
        self.assertEqual(self.dthelper.helper_extract_days("10  days"), None)
        self.assertEqual(self.dthelper.helper_extract_days("10-days"), None)
        self.assertEqual(self.dthelper.helper_extract_days("10.days"), None)

    def test_helper_extract_months(self):
        self.assertEqual(self.dthelper.helper_extract_months("10months"), 10)
        self.assertEqual(self.dthelper.helper_extract_months("10 month"), 10)
        self.assertEqual(self.dthelper.helper_extract_months("10  months"), None)
        self.assertEqual(self.dthelper.helper_extract_months("10-months"), None)
        self.assertEqual(self.dthelper.helper_extract_months("10.months"), None)
        self.assertEqual(self.dthelper.helper_extract_months("10.years"), None)
        self.assertEqual(self.dthelper.helper_extract_months("10.day"), None)

    def test_helper_extract_year(self):
        self.assertEqual(self.dthelper.helper_extract_year("101year"), 101)
        self.assertEqual(self.dthelper.helper_extract_year("10 years"), 10)
        self.assertEqual(self.dthelper.helper_extract_year("10  months"), None)
        self.assertEqual(self.dthelper.helper_extract_year("10-year"), None)
        self.assertEqual(self.dthelper.helper_extract_year("10.years"), None)
        self.assertEqual(self.dthelper.helper_extract_year("10.day"), None)

    def test_date_in_utc(self):
        utc_time = "2021-05-12T13:19:12.660Z"
        non_utc_time = datetime.datetime.now()
        self.assertEqual(self.dthelper.is_utc(utc_time), True)
        self.assertEqual(self.dthelper.is_utc(non_utc_time), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
