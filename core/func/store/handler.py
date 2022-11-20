# -*- coding: utf-8 -*-
# @Time    : 29.05.21 17:51
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : handler.py
# @Software: PyCharm

import pymongo
import os, json, sys


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
    response = {"status": "", "message": ""}

    if method in ["POST", "PUT"]:
        if is_json(req):
            req = json.loads(req)
            client = pymongo.MongoClient(
                "mongodb+srv://prototype-app-user:7eGjHckJauX7xsCJ@tek-mongo-research-clus.8brvl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
            )
            database = client["consent_create_response"]
            collection = database["consent_create_response"]
            insert = collection.insert_one(req)
            if insert.inserted_id:
                response["status"] = "SUCCESS"
                response["message"] = insert.inserted_id
            else:
                response["status"] = "FAIL"
                response["message"] = "DB Error, contact admin"

        else:
            response["status"] = "FAIL"
            response["message"] = "Invalid data format"

    else:
        response["status"] = "FAIL"
        response["message"] = "Invalid request method"

    return response
