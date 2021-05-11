# -*- coding: utf-8 -*-
# @Time    : 07.05.21 13:01
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : QueryEngine.py
# @Software: PyCharm


from SPARQLWrapper import SPARQLWrapper, JSON
import os
import textwrap
import json
class QueryEngine:
    def __init__(self):
        self.HOST_URI = "https://smashhitactool.sti2.at/repositories/TestingNode"


    def prefix(self):
        prefix = textwrap.dedent("""PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
            PREFIX gconsent: <https://w3id.org/GConsent#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        """)
        return prefix

    def bulk_consentID(self):
        query = textwrap.dedent("""{0}
                SELECT ?ConsentID   
                 WHERE {{ 
                  ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
                  ?ConsentID :GrantedAtTime ?GrantedAtTime.
                  ?ConsentID :RevokedAtTime ?RevokedAtTime.
                   FILTER (?RevokedAtTime = "None") 
                }}""").format(self.prefix())
        return query

    def consentID_by_name(self, name):
        query = textwrap.dedent("""{0}
                SELECT ?ConsentID   
                 WHERE {{ 
                  ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
                  ?ConsentID :isProvidedBy :{1}.
                  ?ConsentID :GrantedAtTime ?GrantedAtTime.
                  ?ConsentID :RevokedAtTime ?RevokedAtTime.
                   FILTER (?RevokedAtTime = "None") 
                }}""").format(self.prefix(), name)
        return query

    def get_username(self):
        return os.environ.get("USERNAME")

    def get_password(self):
        return os.environ.get("PASSWORD")

    def init_sparql(self, hostname, userid, password):
        sparql = SPARQLWrapper(hostname)
        sparql.setCredentials(userid, password)
        return sparql

    def check_all_none(self, list_of_elements):
        toCheck = None
        return all([elem == toCheck for elem in list_of_elements])

    def function_map(self, name):
        mapfunc = {
                   "bulk_consentid": self.bulk_consentID,
                   "consentID_by_name": self.consentID_by_name,

                   }
        return mapfunc[name]

    def which_query(self, consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None, additionalData=None):
        if additionalData=="bconsentID":
            return dict({"map": "bulk_consentid"})

        if additionalData=="consentID" and consentProvidedBy is not None:
            return dict({"map": "consentID_by_name", "arg": consentProvidedBy})



    def select_query_gdb(self, consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None, additionalData=None):
        sparql_inits = self.init_sparql(self.HOST_URI, self.get_username(), self.get_password())
        which_query_return = self.which_query(consentProvidedBy, purpose, dataProcessing, dataController,
                    dataRequester, additionalData)
        if("arg" in which_query_return.keys()):
            sparql_inits.setQuery(self.function_map(which_query_return["map"])(which_query_return["arg"]))
        else:
            sparql_inits.setQuery(self.function_map(which_query_return["map"])())
        sparql_inits.setReturnFormat(JSON)
        results = sparql_inits.query().convert()
        return json.dumps(results)