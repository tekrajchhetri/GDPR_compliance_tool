# -*- coding: utf-8 -*-
# @Time    : 25.06.21 13:40
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : JWTHelper.py
# @Software: PyCharm
import datetime
from hashlib import blake2b
import os
class JWTHelper:

    def __random_unique_timestamp_hash(self):
        tsp = hex(int(datetime.datetime.utcnow().timestamp()))
        salt1 = os.urandom(blake2b.SALT_SIZE)
        h1 = blake2b(salt=salt1)
        tsp_str = str(tsp).encode()
        h1.update(tsp_str)
        hstring = h1.hexdigest()
        return hstring

    def organisation_map(self, organisation_map_code):
        """ Map to actual function
        :param name: name which function to map
        :return: mapped code
        """
        hstring = self.__random_unique_timestamp_hash()
        try:
            mapfunc = {
                       "LUH": hstring,
                       "SPC": hstring,
                        "CCC": hstring
                       }

            return mapfunc[organisation_map_code]
        except:
            return 0

