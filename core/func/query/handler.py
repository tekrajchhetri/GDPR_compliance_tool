# -*- coding: utf-8 -*-
# @Time    : 29.05.21 21:14
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : handler.py
# @Software: PyCharm

import pymongo
import os, json, sys
import yaml
from bson.json_util import dumps

fileconfig = f"{os.path.dirname(__file__)}/config.yml"
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

def check_file(file):
    return os.path.exists(file) and os.path.isfile(file) and os.path.splitext(file)[1].lower() == ".yml"

def get_search_query(inputJSON):
    data = inputJSON
    docs = yaml.load(open(fileconfig),Loader=yaml.SafeLoader)
    items_matching_filter = list(set(docs["filter"]).intersection(data.keys()))
    query_dict = {}
    for conig_filter in items_matching_filter:
        query_dict[conig_filter] = data[conig_filter]
    return  query_dict

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    method = os.getenv("Http_Method")
    response = {"status":"","message":""}
    if (check_file(fileconfig)):
        if method in ["GET"]:
            if is_json(req):
                req = json.loads(req)
                query = get_search_query(req)
                client = pymongo.MongoClient(
                    "mongodb+srv://prototype-app-user:7eGjHckJauX7xsCJ@tek-mongo-research-clus.8brvl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                database = client["consent_create_response"]
                collection = database["consent_create_response"]
                result = collection.find(query)
                response["status"] = "SUCCESS"
                response["message"] = json.loads(dumps(list(result), indent=2))
            else:
                response["status"] = "FAIL"
                response["message"] = "DB Error, contact admin"

        else:
            response["status"] = "FAIL"
            response["message"] = "Invalid request method"
    else:
        response["status"] = "ERROR"
        response["message"] = "Missing config file"


    return response

