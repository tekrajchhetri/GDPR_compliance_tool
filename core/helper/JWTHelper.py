# -*- coding: utf-8 -*-
# @Time    : 25.06.21 13:40
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : JWTHelper.py
# @Software: PyCharm

class JWTHelper:
    def organisation_map(self, code):
        """ Map to actual function
        :param name: name which function to map
        :return: mapped code
        """
        try:
            name = code.upper()
            mapfunc = {
                       "LUH": 2040,
                       "SPC": 2020,
                        "CCC": 3030
                       }
            return mapfunc[name]
        except:
            return 0