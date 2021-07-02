# -*- coding: utf-8 -*-
# @Time    : 07.05.21 13:01
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : QueryProcessor.py
# @Software: PyCharm



from core.Credentials import Credentials
from core.storage.SPARQL import SPARQL
from core.helper.HelperACT import HelperACT
from core.smashHitmessages import smashHitmessages
import textwrap
from core.security.Cryptography import Encrypt
class QueryEngine (Credentials, SPARQL, smashHitmessages, HelperACT):
    def __init__(self):
        self.encobj = Encrypt()
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




    def insert_query(self, requestedBy,hasDataController, fordataprocessing, GrantedAtTime, inMedium, purpose,
                     isAboutData, city, consentID, country, state, dataprovider, expirationtime):

        granted = "GRANTED"
        insquery = textwrap.dedent("""{0} 
        INSERT DATA {{
            :{1} a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>;
            :inMedium :{2};
            dpv:hasPurpose :{3};
            {4}
            :GrantedAtTime :{5};
            {6}
            :hasExpiry :{7};
            :atCountry :{8};
            :atCity :{9};
            :atState :{10};
            :requestedBy :{11};
            :hasDataController :{12};
            :isProvidedBy :{13};
            :status :{14}.
                   }}       
               
          """).format(self.prefix(),
                      consentID,
                      self.encobj.encrypt_aes(inMedium),
                      self.encobj.encrypt_aes(purpose),
                      self.list_to_query(isAboutData, "isAboutData", self.encobj),
                      self.encobj.encrypt_aes(GrantedAtTime),
                      self.list_to_query(fordataprocessing, "forDataProcessing", self.encobj),
                      self.encobj.encrypt_aes(expirationtime),
                      self.encobj.encrypt_aes(country),
                      self.encobj.encrypt_aes(city),
                      self.encobj.encrypt_aes(state),
                      self.encobj.encrypt_aes(requestedBy),
                      self.encobj.encrypt_aes(hasDataController),
                      self.encobj.encrypt_aes(dataprovider),
                      self.encobj.encrypt_aes(granted))

        return insquery



    def consentID_by_consentprovider_ID(self, consentprovider_ID):
        """
        Get consent ID by consent provide ID
        :param consentID_by_consentprovider_ID: Unique ID mapped to data subjectr
        :return: consentID
        """
        query = textwrap.dedent("""{0}
                SELECT ?ConsentID   
                 WHERE {{ 
                 ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
                  ?ConsentID :isProvidedBy :{1}.
                  ?ConsentID :GrantedAtTime ?GrantedAtTime.
                   FILTER NOT EXISTS {{ ?ConsentID :RevokedAtTime ?RevokedAtTime.}}
                }}""").format(self.prefix(), self.encobj.encrypt_aes(consentprovider_ID))

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

    def revoke_broken_consent_query(self, consentID, type="REVOKED"):
        revokedTime = '\'{}^^xsd:dateTime\''.format(self.decision_timestamp())
        encRevoked = self.encobj.encrypt_aes(revokedTime)
        query = textwrap.dedent("""{0} 
            DELETE {{?ConsentID :status :{1}.}}
            INSERT {{?ConsentID :status :{2}.
            ?ConsentID :RevokedAtTime :{3}.
            }}
             WHERE {{
             ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
              FILTER(?ConsentID = :{4})
             }}""").format(self.prefix(),
                           self.encobj.encrypt_aes("GRANTED"),
                           self.encobj.encrypt_aes(type),
                           encRevoked,
                           consentID
                           )

        return query


















