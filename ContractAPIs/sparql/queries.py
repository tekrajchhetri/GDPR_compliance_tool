from SPARQLWrapper import SPARQLWrapper, JSON, BASIC
import textwrap
from credentials.user_credentials import UserCredentials
from datetime import date
import os

class SPARQL(UserCredentials):
    
    def __init__(self):
        super().__init__()

        self.HOST_URI_GET = os.getenv('HOST_URI_GET')
        self.HOST_URI_POST = os.getenv('HOST_URI_POST')
    
    def init_sparql(self, hostname, userid, password):
        sparql = SPARQLWrapper(hostname)
        sparql.setCredentials(userid, password)
        return sparql
    
    def prefix(self):
        prefix = textwrap.dedent(
            """PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
            PREFIX prov: <http://www.w3.org/ns/prov#>
            PREFIX dcat: <http://www.w3.org/ns/dcat#>
            PREFIX fibo-fnd-agr-ctr: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        """)
        return prefix

    def get_all_contracts(self):
        sparql=self.init_sparql(self.HOST_URI_GET, self.get_username(), self.get_password())
        query = textwrap.dedent("""{0}
            select * 
            where{{  ?Contract a :ContractId;
                    :hasContractStatus ?ContractStatus;
                    :forPurpose ?Purpose;
                    :contractType ?ContractType;
                    :hasDataController ?DataController;
                    :ContractRequester ?ContractRequester;
                    :ContractProvider ?ContractProvider;
                    dcat:startDate ?StartDate;
                    dcat:endDate ?EndingDate;
                    fibo-fnd-agr-ctr:hasEffectiveDate ?EffectiveDate;
                    fibo-fnd-agr-ctr:hasExecutionDate ?ExecutionDate;
                    :inMedium ?Medium;
                    :hasWaiver ?Waiver;
                    :hasAmendment ?Amendment;
                    :hasConfidentialityObligation ?ConfidentialityObligation;
                    :hasDataProtection ?DataProtection;
                    :hasLimitationOnUse ?LimitationOnUse;
                    :hasMethodOfNotice ?MethodOfNotice;
                    :hasNoThirdPartyBeneficiaries ?NoThirdPartyBeneficiaries;
                    :hasPermittedDisclosure ?PermittedDisclosure;
                    :hasReceiptOfNotice ?ReceiptOfNotice;
                    :hasSeverability ?Severability;
                    :hasTerminationForInsolvency ?TerminationForInsolvency;
                    :hasTerminationForMaterialBreach ?TerminationForMaterialBreach;
                    :hasTerminationOnNotice ?TerminationOnNotice .
        }}
        """).format(self.prefix())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        response = sparql.query().convert()
        return response
    
    def get_contract_by_requester(self,name):
        sparql=self.init_sparql(self.HOST_URI_GET, self.get_username(), self.get_password())
        query = textwrap.dedent("""{0}
            SELECT ?Contract   
                WHERE {{ 
                ?Contract a :ContractId;
                        :ContractRequester :{1}.
            }}""").format(self.prefix(),name)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        response = sparql.query().convert()
        return response
    
    def get_contract_by_provider(self,name):
        sparql=self.init_sparql(self.HOST_URI_GET, self.get_username(), self.get_password())
        query = textwrap.dedent("""{0}
            SELECT ?Contract   
                WHERE {{ 
                ?Contract a :ContractId;
                        :ContractProvider :{1}.
            }}""").format(self.prefix(),name)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        response = sparql.query().convert()
        return response
    
    def get_contract_by_id(self,id):
        sparql=self.init_sparql(self.HOST_URI_GET, self.get_username(), self.get_password())
        query = textwrap.dedent("""{0}
            SELECT *   
                WHERE {{ 
                ?Contract a :ContractId;
                filter(?Contract=:{1}) .
            }}""").format(self.prefix(),id)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        response = sparql.query().convert()
        return response
    
    def contract_revoke_by_id(self,id):
        sparql=self.init_sparql(self.HOST_URI_POST, self.get_username(), self.get_password())
        revoke_date=date.today()
        query = textwrap.dedent("""{0} 
            DELETE {{?ContractId :hasContractStatus :VALID.}}
            INSERT {{?ContractId :hasContractStatus :REVOKED.
            ?ContractId :RevokedAtTime {1}.
            }}
             WHERE {{
             ?ContractId a <http://ontologies.atb-bremen.de/smashHitCore#ContractId>.
              FILTER(?ContractId = :{2})
             }}""").format(self.prefix(), '\'{}^^xsd:dateTime\''.format(revoke_date), id)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        response = "Contract has been revoked"
        return response    
    def insert_query(self, ContractId, ContractType, Purpose,
                     ContractRequester, ContractProvider,DataController,StartDate,
                     ExecutionDate,EffectiveDate,ExpireDate,Medium,Waiver,Amendment,
                     ConfidentialityObligation,DataProtection,LimitationOnUse,
                     MethodOfNotice,NoThirdPartyBeneficiaries,PermittedDisclosure,
                     ReceiptOfNotice,Severability,TerminationForInsolvency,
                     TerminationForMaterialBreach,TerminationOnNotice,ContractStatus):
        insquery = textwrap.dedent("""{0} 
            INSERT DATA {{
            :{1} a <http://ontologies.atb-bremen.de/smashHitCore#ContractId>;
            :contractType :{2};
                       :forPurpose "{3}";
                       :ContractRequester :{4};
                       :ContractProvider :{5};
                       :hasDataController :{6};
                        dcat:startDate :{7};
                        fibo-fnd-agr-ctr:hasExecutionDate :{8};
                        fibo-fnd-agr-ctr:hasEffectiveDate :{9};
                        dcat:endDate :{10};
                        :inMedium "{11}";
                        :hasWaiver "{12}";
                        :hasAmendment "{13}";
                        :hasConfidentialityObligation "{14}";
                        :hasDataProtection "{15}";
                        :hasLimitationOnUse "{16}";
                        :hasMethodOfNotice "{17}";
                        :hasNoThirdPartyBeneficiaries "{18}";
                        :hasPermittedDisclosure "{19}";
                        :hasReceiptOfNotice "{20}";
                        :hasSeverability "{21}";
                        :hasTerminationForInsolvency "{22}";
                        :hasTerminationForMaterialBreach "{23}";
                        :hasTerminationOnNotice "{24}";
                        :hasContractStatus :{25} .
                   }}       
               
          """.format(self.prefix(), ContractId, ContractType,
                     Purpose, ContractRequester,
                     ContractProvider,DataController,StartDate,
                     ExecutionDate,EffectiveDate,ExpireDate,Medium,Waiver,Amendment,
                     ConfidentialityObligation,DataProtection,LimitationOnUse,
                     MethodOfNotice,NoThirdPartyBeneficiaries,PermittedDisclosure,
                     ReceiptOfNotice,Severability,TerminationForInsolvency,
                     TerminationForMaterialBreach,TerminationOnNotice,ContractStatus))
        return insquery

    def post_data(self, ContractId, ContractType, Purpose,
                  ContractRequester, ContractProvider,DataController,StartDate,ExecutionDate,
                     ExpireDate,EffectiveDate,Medium,Waiver,Amendment,
                     ConfidentialityObligation,DataProtection,LimitationOnUse,
                     MethodOfNotice,NoThirdPartyBeneficiaries,PermittedDisclosure,
                     ReceiptOfNotice,Severability,TerminationForInsolvency,
                     TerminationForMaterialBreach,TerminationOnNotice,ContractStatus):
        response = self.post_sparql(
            self.insert_query(ContractId=ContractId,
                              ContractType=ContractType,
                              Purpose=Purpose,
                              ContractRequester=ContractRequester,
                              ContractProvider=ContractProvider,
                              DataController=DataController,
                              StartDate=StartDate,
                              ExecutionDate=ExecutionDate,
                              EffectiveDate=EffectiveDate,
                              ExpireDate=ExpireDate,
                              Medium=Medium,
                              Waiver=Waiver,
                              Amendment=Amendment,
                              ConfidentialityObligation=ConfidentialityObligation,
                              DataProtection=DataProtection,
                              LimitationOnUse=LimitationOnUse,
                              MethodOfNotice=MethodOfNotice,
                              NoThirdPartyBeneficiaries=NoThirdPartyBeneficiaries,
                              PermittedDisclosure=PermittedDisclosure,
                              ReceiptOfNotice=ReceiptOfNotice,
                              Severability=Severability,
                              TerminationForInsolvency=TerminationForInsolvency,
                              TerminationForMaterialBreach=TerminationForMaterialBreach,
                              TerminationOnNotice=TerminationOnNotice,
                              ContractStatus=ContractStatus ))
        return response

    def post_sparql(self, query):
        sparql=self.init_sparql(self.HOST_URI_POST, self.get_username(), self.get_password())
        sparql.setHTTPAuth(BASIC)
        sparql.setQuery(query)
        sparql.method = "POST"
        sparql.queryType = "INSERT"
        sparql.setReturnFormat('json')
        result = sparql.query()

        if str(result.response.read().decode("utf-8")) == "":
            return {"status": "SUCCESS"}
        else:
            return {"status": "FAILED"}