# -*- coding: utf-8 -*-
# @Time    : 07.05.21 13:01
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : QueryEngine.py
# @Software: PyCharm


from SPARQLWrapper import  JSON
from core.Credentials import Credentials
from core.SPARQL import SPARQL
import textwrap
import json
class QueryEngine (Credentials, SPARQL):
    def __init__(self):
        super().__init__()

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

    def insert_query(self, ConsentIDInput, DataControllerInput, DataInput, DataProcessingInput, DataRequesterInput,
                     DurationInput, GrantedAtTimeInput, MediumInput, NameInput, PurposeInput):
        insquery = textwrap.dedent("""{0} 
        INSERT DATA {{
            :{1} a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>;
            :isProvidedBy :{2};
                       :inMedium :{3};
                       :forPurpose "{4}";
                        :forDataProcessing :{5}; 
                       :requestedBy :{6};
                       :isAboutData :{7};
                       :hasExpiry :{8};
                       :hasDataController :{9};
                       :GrantedAtTime "{10}^^xsd:dateTime".
                   }}       
               
          """).format(self.prefix(),  ConsentIDInput, NameInput, MediumInput, PurposeInput, DataProcessingInput,
                      DataRequesterInput, DataInput, DurationInput,
                      DataControllerInput, GrantedAtTimeInput)

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

    def post_data(self, ConsentIDInput, DataControllerInput, DataInput, DataProcessingInput, DataRequesterInput,
                  DurationInput, GrantedAtTimeInput, MediumInput, NameInput, PurposeInput):

        respone = self.post_sparql(self.get_username(), self.get_password(),
                                   self.insert_query(ConsentIDInput= ConsentIDInput,
                                                     DataControllerInput = DataControllerInput,
                                                     DataInput = DataInput,
                                                     DataProcessingInput = DataProcessingInput,
                                                     DataRequesterInput = DataRequesterInput,
                                                     DurationInput=DurationInput,
                                                     GrantedAtTimeInput = GrantedAtTimeInput,
                                                     MediumInput = MediumInput, NameInput=NameInput,
                                                     PurposeInput=PurposeInput)
                                   )
        return respone




