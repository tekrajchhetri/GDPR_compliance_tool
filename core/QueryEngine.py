# -*- coding: utf-8 -*-
# @Time    : 07.05.21 13:01
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : QueryEngine.py
# @Software: PyCharm


from SPARQLWrapper import SPARQLWrapper, JSON
import os
import textwrap
class QueryEngine:
    def __init__(self):
        self.HOST_URI = "https://smashhitactool.sti2.at/repositories/TestingNode"

    def get_consent_by_name_pur_dp_dr_dc(self,
                                         consentProvidedBy,
                                         purpose,
                                         dataProcessing,
                                         dataController,
                                         dataRequester
                                         ):
        query = """
                    PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
                    PREFIX gconsent5: <https://w3id.org/GConsent/versions/v0.5#>
                    PREFIX cc: <http://creativecommons.org/ns#>
                    PREFIX consent: <http://ontologies.atb-bremen.de/consent#>
                    PREFIX context: <http://ontologies.atb-bremen.de/context#>
                    PREFIX contract: <http://ontologies.atb-bremen.de/contract#>
                    PREFIX dalicc: <https://dalicc.poolparty.biz/DALICC/>
                    PREFIX dc: <http://purl.org/dc/elements/1.1/>
                    PREFIX dcat: <http://www.w3.org/ns/dcat#>
                    PREFIX dct: <http://purl.org/dc/terms/>
                    PREFIX dpv: <http://www.w3.org/ns/dpv#>
                    PREFIX fibo-fnd-agr-ctr: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>
                    PREFIX fn: <http://www.w3.org/2005/xpath-functions#>
                    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                    PREFIX grddl: <http://www.w3.org/2003/g/data-view#>
                    PREFIX kntest: <http://ontologies.atb-bremen.de/smashHitCore>
                    PREFIX odrl: <http://www.w3.org/ns/odrl/2/>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX OntoSensor: <http://mmisw.org/ont/univmemphis/sensor>
                    PREFIX prov: <http://www.w3.org/ns/prov#>
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX security: <http://ontologies.atb-bremen.de/security#>
                    PREFIX sesame: <http://www.openrdf.org/schema/sesame#>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    PREFIX xml: <http://www.w3.org/XML/1998/namespace>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

                    SELECT ?ConsentID ?Name ?Purpose ?Status ?DataController ?DataRequester ?GivenAt ?Duration ?Data ?DataProcessing
                     WHERE { 
                      ?ConsentID :isProvidedBy """ + consentProvidedBy + """.
                     ?ConsentID :forPurpose """ + purpose + """.
                      ?Purpose :forDataProcessing """ + dataProcessing + """.
                      ?ConsentID rdf:hasStatus ?Status.
                      ?ConsentID :hasDataController """ + dataController + """.
                      ?ConsentID :requestedBy """ + dataRequester + """.
                      ?ConsentID :atDate ?GivenAt.
                      ?ConsentID :hasExpiry ?Duration.
                      ?ConsentID :isAboutData ?Data.
                    } LIMIT 1 
        """
        return query

    def prefix(self):
        prefix = textwrap.dedent("""PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
            PREFIX gconsent: <https://w3id.org/GConsent#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        """)
        return prefix

    def get_consent_by_name_pur_dp(self,
                                         consentProvidedBy,
                                         purpose,
                                         dataProcessing,
                                        ):
        query = """
                    PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
                    PREFIX gconsent5: <https://w3id.org/GConsent/versions/v0.5#>
                    PREFIX cc: <http://creativecommons.org/ns#>
                    PREFIX consent: <http://ontologies.atb-bremen.de/consent#>
                    PREFIX context: <http://ontologies.atb-bremen.de/context#>
                    PREFIX contract: <http://ontologies.atb-bremen.de/contract#>
                    PREFIX dalicc: <https://dalicc.poolparty.biz/DALICC/>
                    PREFIX dc: <http://purl.org/dc/elements/1.1/>
                    PREFIX dcat: <http://www.w3.org/ns/dcat#>
                    PREFIX dct: <http://purl.org/dc/terms/>
                    PREFIX dpv: <http://www.w3.org/ns/dpv#>
                    PREFIX fibo-fnd-agr-ctr: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>
                    PREFIX fn: <http://www.w3.org/2005/xpath-functions#>
                    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                    PREFIX grddl: <http://www.w3.org/2003/g/data-view#>
                    PREFIX kntest: <http://ontologies.atb-bremen.de/smashHitCore>
                    PREFIX odrl: <http://www.w3.org/ns/odrl/2/>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX OntoSensor: <http://mmisw.org/ont/univmemphis/sensor>
                    PREFIX prov: <http://www.w3.org/ns/prov#>
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX security: <http://ontologies.atb-bremen.de/security#>
                    PREFIX sesame: <http://www.openrdf.org/schema/sesame#>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    PREFIX xml: <http://www.w3.org/XML/1998/namespace>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

                    SELECT ?ConsentID ?Name ?Purpose ?Status ?DataController ?DataRequester ?GivenAt ?Duration ?Data ?DataProcessing
                     WHERE { 
                      ?ConsentID :isProvidedBy """ + consentProvidedBy + """.
                     ?ConsentID :forPurpose """ + purpose + """.
                      ?Purpose :forDataProcessing """ + dataProcessing + """.
                      ?ConsentID rdf:hasStatus ?Status.
                      ?ConsentID :hasDataController ?DataController.
                      ?ConsentID :requestedBy ?DataRequester.
                      ?ConsentID :atDate ?GivenAt.
                      ?ConsentID :hasExpiry ?Duration.
                      ?ConsentID :isAboutData ?Data.
                    } LIMIT 1 
        """
        return query

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

    def consent_by_name(self, name):
        query = "To be updated"
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
        mapfunc =  {"consent_by_name": self.consent_by_name}
        return mapfunc[name]


    def which_query(self, consentProvidedBy=None, purpose=None, dataProcessing=None, dataController=None,
                    dataRequester=None):
        if consentProvidedBy is None:
            return {"Invalid request format. Error-SMAC1"}
        else:
            if self.check_all_none([purpose, dataRequester,dataController,dataProcessing]):
                return {"map" : "consent_by_name", "arg":consentProvidedBy}


    def select_query_gdb(self, consentProvidedBy, purpose, dataProcessing, dataController,
                    dataRequester):
        sparql_inits = self.init_sparql(self.HOST_URI, self.get_username(), self.get_password())
        which_query_return = self.which_query(consentProvidedBy, purpose, dataProcessing, dataController,
                    dataRequester)
        sparql_inits.setQuery(self.function_map(which_query_return["map"])(which_query_return["arg"]))
        sparql_inits.setReturnFormat(JSON)
        results = sparql_inits.query().convert()
        return results
