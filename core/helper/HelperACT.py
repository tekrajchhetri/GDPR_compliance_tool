# -*- coding: utf-8 -*-
# @Time    : 14.06.21 14:07
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : HelperACT.py
# @Software: PyCharm
import json
from SPARQLWrapper import  JSON
import spacy
from fuzzywuzzy import fuzz
from operator import itemgetter
from core.security.Cryptography import  Decrypt
class HelperACT:

    def load_spacy_model(self):
        nlp = spacy.load('en_core_web_lg')
        return nlp

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
            decobj = Decrypt()
            consent_fetched = consent["results"]["bindings"][0]["status"]["value"].split("#")[1]
            consent_fetched = bytes(consent_fetched,"utf-8")
            isgranted = decobj.decrypt_aes(consent_fetched).decode("utf-8")
            return "granted" in str(isgranted).lower()
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
                    "all_details_by_dataprovider":self.all_details_by_dataprovider,
                    "audit_by_consentid":self.audit_by_consentid,
                    "all_consent_for_compliance":self.all_consent_for_compliance,
                   }
        return mapfunc[name]

    def list_to_query(self, data, whatfor, EncryptObj):
        """ Convert list to query for data processing
        :input: list
        :returns: SPARQL query string
        """
        querydata = ""
        for vlaue in data:
            strs = ":"+whatfor+" :" + EncryptObj.encrypt_aes(vlaue) + ";\n"
            querydata = strs + querydata
        return querydata

    def list_to_query_isaboutdata(self, data, whatfor, EncryptObj):
        """ Convert list to query for data processing
        :input: list
        :returns: SPARQL query string
        """
        querydata = ""
        for key in data:
            for value in data[key]:
                formatted_dat = "{}-{}".format(key, value)
                strs = ":" + whatfor + " :" + EncryptObj.encrypt_aes(formatted_dat) + ";\n"
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

        if additionalData == "check_consent" and consentID is not None:
            return dict({"map": "consent_by_consentID", "arg": consentID})

        if additionalData=="audit_by_consentprovider" and consentProvidedBy is not None:
            return dict({"map": "all_details_by_dataprovider", "arg": consentProvidedBy})

        if additionalData=="audit_by_consentid" and consentID is not None:
            return dict({"map": "audit_by_consentid", "arg": consentID})

        if additionalData == "consent_for_compliance":
            return dict({"map": "all_consent_for_compliance"})

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

    def preprocess(self, word):
        return word.strip().lower()


    def tokenize(self, word):
        """ Perform the word lemitization
        :param word: string that is to be tokenized
        :return: lemmatized word
        """
        nlp = self.load_spacy_model()
        word = self.preprocess(word=word)
        doc = nlp(word)
        return [token.lemma_ for token in doc][0]

    def match(self, x, y):
        """ Fuzzy string matching
        :param x: input string from consent
        :param y: input string from data controller/processor
        :return: boolean
        """
        ratio =  fuzz.token_set_ratio(x, y)
        return True if ratio >= 95 else False

    def has_valid_purpose(self, purpose_from_consent, current_processing_purpose_by_controller):
        """ checks the validatity of purpose in accordance with given consent
        :param purpose_from_consent:  purpose that was consented to
        :param current_processing_purpose_by_controller:  purpose current DP/DC is using data for
        :return: boolean
        """
        return self.match(self.tokenize(purpose_from_consent),
                          self.tokenize(current_processing_purpose_by_controller)
                          )

    def calculate_length(self, x):
        if type(x) == list:
            return len(x)
        else:
            return 0

    def get_keys(self, dictitems):
        return list(map(itemgetter(0), dictitems.items()))[0]

    def matcher_helper(self, consented,fromControllerOrProcessor):
        """ checks for match using fuzzy logic
        :param consented: list items from consent
        :param fromControllerOrProcessor:  list items from controller or processor
        :return: boolean
        """
        consented = sorted(
            [self.tokenize(word_for_tokenized_lemma) for word_for_tokenized_lemma in consented])
        fromControllerOrProcessor = sorted(
            [self.tokenize(word_for_tokenized_lemma) for word_for_tokenized_lemma in fromControllerOrProcessor])

        if self.calculate_length(fromControllerOrProcessor) == self.calculate_length(consented):
            condition_status = []
            for i in range(len(consented)):
                condition_status.append(self.match(consented[i], fromControllerOrProcessor[i]))
            return False if False in condition_status else True

        elif self.calculate_length(fromControllerOrProcessor) < self.calculate_length(consented):
            intersected = sorted(list(set(fromControllerOrProcessor).intersection(consented)))
            if self.calculate_length(intersected) != self.calculate_length(fromControllerOrProcessor):
                return False

            condition_status = []

            for i in range(len(fromControllerOrProcessor)):
                condition_status.append(self.match(fromControllerOrProcessor[i], intersected[i]))
            return False if False in condition_status else True

        return False


    def has_processing_rights(self, consent_for_processing, current_processing_by_controller):

        if  self.calculate_length(current_processing_by_controller) > self.calculate_length(consent_for_processing):
            return False

        return self.matcher_helper(consent_for_processing, current_processing_by_controller)

    def is_doing_valid_processing(self, consented_data_for_processing, current_data_being_used_or_processed):
        head_consented_data = [self.get_keys(dictItems) for dictItems in consented_data_for_processing]
        head_processed_data = [self.get_keys(dictItems) for dictItems in current_data_being_used_or_processed]

        if self.calculate_length(head_processed_data) > self.calculate_length(head_consented_data):
            return False

    def decrypt_data(self, data):
        """Decrypt data
        :param data: single value encrypted data
        :return: decrypted data
        """
        if data is None or "None" in data:
            return data
        else:
            dec = Decrypt()
            return dec.decrypt_aes(data).decode("utf-8")

    def remove_uris(self, data):
        """ return plain text data without URI's
        :param data: semantic data
        :return: data without semantic
        """
        return data.split('#')[1]

    def process_consent_data(self, data):
        """ process encrypted consent data
        :param data: consent data retrieved from GraphDB
        :return: decrypted consent in JSON format
        """
        resp_to_make = {}
        for value in data["results"]["bindings"]:
            list_of_consents = []
            for k in value:
                # skip consent ID as it causes error
                if k == "ConsentID":
                    continue
                elif (k == "DataProcessing"):
                    list_of_consents.append({k: [self.decrypt_data(self.remove_uris(litem)) for litem in value[k]["value"].split(",")]})
                elif (k == "Data"):
                    list_of_consents.append({k:[self.decrypt_data(self.remove_uris(litem)) for litem in value[k]["value"].split(",")]})
                else:
                    list_of_consents.append({k: self.decrypt_data(self.remove_uris(value[k]["value"]))})
            resp_to_make[self.remove_uris(value["ConsentID"]["value"])] = list_of_consents
        return resp_to_make


    def remove_xst_date(self, date_xst_str):
        return date_xst_str[1: len(date_xst_str) - 1].split("^^")[0]
    
