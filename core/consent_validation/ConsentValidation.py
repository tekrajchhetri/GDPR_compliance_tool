# -*- coding: utf-8 -*-
# @Time    : 17.05.21 14:07
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : ConsentValidation.py
# @Software: PyCharm
from core.helper.date_helper import DateHelper
from core.query_processor.QueryProcessor import QueryEngine
from core.low_level.NGAC import NGAC
class  ConsentValidation(QueryEngine):

    def __init__(self):
        super().__init__()

    def post_data(self, validated_data):
        requestedBy = None
        hasDataController = None
        hasDataProcessor = None
        for agent in validated_data["Agents"]:
            if agent["role"] == "controller":
                hasDataController = agent["id"]
            if agent["role"] == "processor":
                hasDataProcessor = agent["id"]
            if agent["role"] == "requester":
                #data
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



        respone = self.post_sparql(userid=self.get_username(), password=self.get_password(),

                                   query=self.insert_query(requestedBy= requestedBy,
                                                     hasDataController = hasDataController,
                                                     hasDataProcessor=hasDataProcessor,
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
                                                    ),
                                   consent_id_for_logging=consentID

                                   )

        if respone["act_status_code"]==7100:
            ngacInst = NGAC()
            status = ngacInst.updateNGAC(requestedBy= requestedBy,
                                                     hasDataController = hasDataController,
                                                     hasDataProcessor=hasDataProcessor,
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
                                                     expirationtime=expirationtime)


            if status == 'fail':
                respone["message"]="Consent created some NGAC update failed"

        return respone
