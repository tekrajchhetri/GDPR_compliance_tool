# -*- coding: utf-8 -*-
# @Time    : 09.05.21 19:03
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : date_helper.py
# @Software: PyCharm
import re
from dateutil.parser import parse

class DateHelper:

    def helper_extract_days(self, datestr):
        """
            Extracts number of day(s) from given input
            Input: 10day,10days,1 day, 2 days
        """
        pattern = r"(([0-9]+\B(days|day))|[0-9]+\s(days|day))"
        return int(re.findall(r'\d+', datestr)[0]) if re.match(pattern, datestr) else None

    def helper_extract_months(self, datestr):
        """
            Extracts number of day(s) from given input
            Input: 10month,10months,1 month, 2 months
        """
        pattern = r"(([0-9]+\B(months|month))|[0-9]+\s(months|month))"
        return int(re.findall(r'\d+', datestr)[0]) if re.match(pattern, datestr) else None

    def helper_extract_year(self, datestr):
        """
            Extracts number of day(s) from given input
            Input: 10years,10years,1 year, 2 years
        """
        pattern = r"(([0-9]+\B(years|year))|[0-9]+\s(years|year))"
        return int(re.findall(r'\d+', datestr)[0]) if re.match(pattern, datestr) else None

    def is_str(self, input):
        """
        :param input: date to check if the input date is in string format
        :return: boolean
        """
        return type(input) == str

    def is_utc(self, datestr):
        """
        :param datestr:
        :return:
        """
        datestr = str(datestr) if not self.is_str(datestr) else datestr
        return parse(datestr).tzname() == "UTC"


