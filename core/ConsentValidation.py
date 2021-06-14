# -*- coding: utf-8 -*-
# @Time    : 17.05.21 14:07
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : ConsentValidation.py
# @Software: PyCharm
from core.date_helper import DateHelper
from core.QueryProcessor import QueryEngine
import dask
class  ConsentValidation(QueryEngine):

    def __init__(self):
        super().__init__()

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

    def get_consent_data(self):
        pass

    def process_data_for_expiry_check(self, data):
        pass

    def check_consent_expiry(self):
        pass

    def parallelise(self):
        consent_data = self.get_consent_data()
        for i in range(len(consent_data)):
            processdata = dask.delayed(self.get_consent_data)(consent_data[i]).compute()
            check_consent_expiry = dask.delayed(self.check_consent_expiry)(processdata[0],processdata[1],processdata[2]).compute()
