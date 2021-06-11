# -*- coding: utf-8 -*-
# @Time    : 07.05.21 13:01
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : QueryEngine.py
# @Software: PyCharm


from SPARQLWrapper import  JSON
from core.Credentials import Credentials
from core.SPARQL import SPARQL
from core.date_helper import DateHelper
from core.smashHitmessages import smashHitmessages
import textwrap
import json
class QueryEngine (Credentials, SPARQL, smashHitmessages):
    def __init__(self):
        super().__init__()

    def prefix(self):
        prefix = textwrap.dedent("""PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
            PREFIX gconsent: <https://w3id.org/GConsent#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX dpv: <http://www.w3.org/ns/dpv#>
        """)
        return prefix

    def bulk_consentID(self):
        query = textwrap.dedent("""{0}
                SELECT ?ConsentID   
                 WHERE {{ 
                  ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
                  ?ConsentID :GrantedAtTime ?GrantedAtTime.
                   FILTER NOT EXISTS {{ ?ConsentID :RevokedAtTime ?RevokedAtTime.}} 
                }}""").format(self.prefix())
        return query

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


    def insert_query(self, requestedBy,hasDataController, fordataprocessing, GrantedAtTime, inMedium, purpose,
                     isAboutData, city, consentID, country, state, dataprovider, expirationtime):
        granted = "GRANTED"
        insquery = textwrap.dedent("""{0} 
        INSERT DATA {{
            :{1} a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>;
            :inMedium :{2};
            dpv:hasPurpose :{3};
            {4}
            :GrantedAtTime {5};
            {6}
            :hasExpiry {7};
            :atCountry :{8};
            :atCity :{9};
            :atState :{10};
            :requestedBy :{11};
            :hasDataController :{12};
            :isProvidedBy :{13};
            :status :{14}.
                   }}       
               
          """).format(self.prefix(),  consentID, inMedium, purpose, self.list_to_query(isAboutData, "isAboutData"),GrantedAtTime,
                      self.list_to_query(fordataprocessing, "forDataProcessing"), expirationtime, country, city, state, requestedBy,
                      hasDataController, dataprovider, granted)
        return insquery



    def consentID_by_consentprovider_ID(self, consentprovider_ID):
        """
        Get consent ID by consent provide ID
        :param consentID_by_consentprovider_ID: Unique ID mapped to data subject
        :return: consentID
        """
        query = textwrap.dedent("""{0}
                SELECT ?ConsentID   
                 WHERE {{ 
                 ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
                  ?ConsentID :isProvidedBy :{1}.
                  ?ConsentID :GrantedAtTime ?GrantedAtTime.
                   FILTER NOT EXISTS {{ ?ConsentID :RevokedAtTime ?RevokedAtTime.}}
                }}""").format(self.prefix(), consentprovider_ID)
        return query

    def consent_by_consentID(self, consentID):
        query = textwrap.dedent("""{0}
              SELECT ?ConsentID
              WHERE {{ 
              ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
               FILTER NOT EXISTS {{ ?ConsentID :RevokedAtTime ?RevokedAtTime.}}
               FILTER(?ConsentID = :{1})
                }}""").format(self.prefix(), consentID)
        return query

    def granted_consent_by_consentID(self, consentID):
        query = textwrap.dedent("""{0}
              SELECT ?status
              WHERE {{ 
              ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
              ?ConsentID :status ?status.
              FILTER(?ConsentID = :{1})
        }}""").format(self.prefix(), consentID)

        return query

    def revoke_query(self, consentID):
        query = textwrap.dedent("""{0} 
            DELETE {{?ConsentID :status :GRANTED.}}
            INSERT {{?ConsentID :status :REVOKED.
            ?ConsentID :RevokedAtTime {1}.
            }}
             WHERE {{
             ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
              FILTER(?ConsentID = :{2})
             }}""").format(self.prefix(), '\'{}^^xsd:dateTime\''.format(self.decision_timestamp()), consentID)

        return query

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
        mapfunc = {
                   "bulk_consentid": self.bulk_consentID,
                   "consentID_by_consentprovider_ID": self.consentID_by_consentprovider_ID,
                    "granted_consent_by_consentID": self.granted_consent_by_consentID,
                    "consent_by_consentID": self.consent_by_consentID,


                   }
        return mapfunc[name]

    def which_query(self, consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None, additionalData=None, consentID=None):
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


    def post_data(self, validated_data):
        requestedBy = None
        hasDataController = None
        for agent in validated_data["Agents"]:
            if agent["role"] == "controller":
                hasDataController = agent["id"]
            elif agent["role"] == "requester":
                requestedBy = agent["id"]
        fordataprocessing = validated_data["DataProcessing"]
        GrantedAtTime = validated_data["GrantedAtTime"]
        inMedium = validated_data["Medium"]
        purpose = validated_data["Purpose"]
        isAboutData = validated_data["Resource"]
        city = validated_data["city"]
        consentID = validated_data["consentid"]
        country = validated_data["country"]
        state = validated_data["state"]
        dataprovider = validated_data["dataprovider"]
        if "expirationTime" in validated_data:
            expirationtime = validated_data["expirationTime"]
        else:
            expirationtime=None


        dt = DateHelper()
        if expirationtime is not None and not dt.is_utc(expirationtime):
            return self.dataformatnotmatch()

        if not dt.is_utc(GrantedAtTime):
            return self.dataformatnotmatch()

        if expirationtime is not None:
            expirationtime = '\'{}^^xsd:dateTime\''.format(expirationtime)
        GrantedAtTime  = '\'{}^^xsd:dateTime\''.format(GrantedAtTime)



        respone = self.post_sparql(self.get_username(), self.get_password(),
                                   self.insert_query(requestedBy= requestedBy,
                                                     hasDataController = hasDataController,
                                                     fordataprocessing = fordataprocessing,
                                                     GrantedAtTime = GrantedAtTime,
                                                     inMedium = inMedium,
                                                     purpose=purpose,
                                                     isAboutData = isAboutData,
                                                     city = city,
                                                     consentID=consentID,
                                                     country=country,
                                                     state=state,
                                                    dataprovider= dataprovider,
                                                     expirationtime=expirationtime
                                                    )
                                   )
        return respone

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

    def revoke_consent(self, consentID):
        if self.check_active_granted_consent(consentID=consentID):
            respone = self.post_sparql(self.get_username(), self.get_password(),
                                       self.revoke_query(consentID=consentID), type="revoke")
            return respone
        else:
            return self.processing_fail_message()



    def broken_consent(self, consentID, reason_for_logging):
        if len(reason_for_logging.strip()) < 5:
            return self.dataformatnotmatch()









