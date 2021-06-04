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
import textwrap
import json
class QueryEngine (Credentials, SPARQL):
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
                  ?ConsentID :RevokedAtTime ?RevokedAtTime.
                   FILTER (?RevokedAtTime = "None") 
                }}""").format(self.prefix())
        return query

    def list_to_query(self, data):
        querydata = ""
        for vlaue in data:
            strs = ":forDataProcessing :" + vlaue + ";\n"
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
               
          """).format(self.prefix(),  consentID, inMedium, purpose, self.list_to_query(isAboutData),GrantedAtTime,
                      self.list_to_query(fordataprocessing), expirationtime, country, city, state, requestedBy,
                      hasDataController, dataprovider, granted)
        return insquery



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

    def for_processing(resource_dict):
        """
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




