# -*- coding: utf-8 -*-
# @Time    : 29.05.21 21:14
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : handler.py
# @Software: PyCharm

import pymongo
import os, json, sys
from bson.json_util import dumps,loads

def is_json(input):
    """Checks if the input is a json
    :param input:
    :return: bool
    """
    isJSON = False
    try:
        jsoninput = json.loads(input)
        isJSON = True
    except:
        isJSON = False
    return isJSON


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    method = os.getenv("Http_Method")
    response = {}
    if method in ["GET"]:
        if is_json(req):
            req = json.loads(req)
            client = pymongo.MongoClient(
                    "mongodb+srv://prototype-app-user:7eGjHckJauX7xsCJ@tek-mongo-research-clus.8brvl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
                    maxPoolSize=400)
            database = client["consent_create_response"]
            collection = database["consent_create_response"]
            if req["query_type"] == "all":
                result = collection.find({'consent_id': {'$in': req["consent_id_list"]}})
                return dumps(list(result), indent=2)

            if req["query_type"]=="single":
                result = collection.find_one(req["consent_id_single"])
                return result
        else:
            response["status"] = "FAIL"
            response["message"] = "DB Error, contact admin"

    else:
        response["status"] = "FAIL"
        response["message"] = "Invalid request method"



    return response

