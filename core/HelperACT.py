# -*- coding: utf-8 -*-
# @Time    : 14.06.21 14:07
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : HelperACT.py
# @Software: PyCharm
import json
from SPARQLWrapper import  JSON

class HelperACT:
    def for_processing(resource_dict):
        """ Convert nested array of inputs into a single array
            :input: resource dict
            :returns: list of data processings
        """
        isAboutData = []
        for processing in resource_dict:
            whatToProcess = resource_dict[processing][0]["data"]
            if len(whatToProcess) == 1:
                isAboutData.append(whatToProcess[0])
            else:
                for value in range(len(whatToProcess)):
                    isAboutData.append(whatToProcess[value])
        return isAboutData

    def consent_exists(self, consent):
        try:
            consent_data = consent["results"]["bindings"][0]["ConsentID"]["value"]
            if len(consent_data.strip()) > 2:
                return True
            return False
        except:
            return False

    def has_status_granted(self, consent):
        try:
            isgranted = consent["results"]["bindings"][0]["status"]["value"]
            return "granted" in isgranted.lower()
        except:
            return False


    def check_all_none(self, list_of_elements):
        toCheck = None
        return all([elem == toCheck for elem in list_of_elements])

    def function_map(self, name):
        """ Map to actual function
        :param name: name which function to map
        :return: function name
        """
        mapfunc = {
                   "bulk_consentid": self.bulk_consentID,
                   "consentID_by_consentprovider_ID": self.consentID_by_consentprovider_ID,
                    "granted_consent_by_consentID": self.granted_consent_by_consentID,
                    "consent_by_consentID": self.consent_by_consentID,


                   }
        return mapfunc[name]

    def list_to_query(self, data, whatfor):
        """ Convert list to query
        :input: list
        :returns: SPARQL query string
        """
        querydata = ""
        for vlaue in data:
            strs = ":"+whatfor+" :" + vlaue + ";\n"
            querydata = strs + querydata
        return querydata


    def which_query(self, consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None, additionalData=None, consentID=None):
        """ Define mapping to appropriate function for query generation based on input
        :param consentProvidedBy:
        :param purpose:
        :param dataProcessing:
        :param dataController:
        :param dataRequester:
        :param additionalData:
        :param consentID:
        :return: <dict>
        """
        if additionalData=="bconsentID":
            return dict({"map": "bulk_consentid"})

        if additionalData == "consentID" and consentProvidedBy is not None:
            return dict({"map": "consentID_by_consentprovider_ID", "arg": consentProvidedBy})

        if additionalData == "check_consent_granted" and consentID is not None:
            return dict({"map": "granted_consent_by_consentID", "arg": consentID})

        if additionalData=="check_consent" and consentID is not None:
            return dict({"map": "consent_by_consentID", "arg": consentID})

    def select_query_gdb(self, consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None, additionalData=None,consentID=None):
        sparql_inits = self.init_sparql(self.HOST_URI, self.get_username(), self.get_password())
        which_query_return = self.which_query(consentProvidedBy, purpose, dataProcessing, dataController,
                    dataRequester, additionalData, consentID)
        if("arg" in which_query_return.keys()):
            sparql_inits.setQuery(self.function_map(which_query_return["map"])(which_query_return["arg"]))
        else:
            sparql_inits.setQuery(self.function_map(which_query_return["map"])())
        sparql_inits.setReturnFormat(JSON)
        results = sparql_inits.query().convert()
        return json.dumps(results)


    def check_active_granted_consent(self, consentID):
        """Performs the following tasks.
        1. Checks if there exists consent for the provided consent ID
        2. If exist then again check if the status is granted and not revoked or broken chain
        :param consentID: consent id
        :return: bool
        """
        consent = json.loads(self.select_query_gdb(consentID=consentID, additionalData="check_consent"))
        if (self.consent_exists(consent)):
            hasGrantedStatus = json.loads(self.select_query_gdb(consentID=consentID,
                                                                additionalData="check_consent_granted"))
            if (self.has_status_granted(hasGrantedStatus)):
                return True

        return False