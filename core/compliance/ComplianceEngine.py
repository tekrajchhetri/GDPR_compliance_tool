# -*- coding: utf-8 -*-
# @Time    : 09.05.21 21:46
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : ComplianceEngine.py
# @Software: PyCharm
from core.query_processor.QueryProcessor import QueryEngine
from  core.helper.date_helper import DateHelper
import json
import requests
import ast
from core.storage.Functions import Functions
from core.smashHitmessages import smashHitmessages
import datetime
from core.low_level.NGAC import NGAC
class ComplianceEngine(QueryEngine, DateHelper):
    def __init__(self):
        super().__init__()
        self.TRIGGER_URL_NOTIFY = "https://tektestapi.herokuapp.com/notify" #dummy test URL to be replaced
        self.TRIGGER_URL_CONTROLLER = "https://tektestapi.herokuapp.com/controller"  # dummy test URL to be replaced
    def broken_consent(self, consentID, reason_for_logging):
        if len(reason_for_logging.strip()) < 2:
            return self.dataformatnotmatch()
        if self.check_active_granted_consent(consentID=consentID):
            respone = self.post_sparql(userid=self.get_username(), password=self.get_password(),
                                       query=self.revoke_broken_consent_query(consentID=consentID,type="BROKEN_CONSENT"),
                                       consent_id_for_logging=consentID, reason_for_logging= reason_for_logging,
                                       type="broken_consent"
                                       )
            updateRevokations = NGAC().updateRevokation(token="admin_token",
                                                        _privacy_preference=NGAC().getpolicy("admin_token"),
                                                        consent_id=consentID
                                                        )

            return respone
        else:
            return self.processing_fail_message()



    def revoke_consent(self, consentID):
        if self.check_active_granted_consent(consentID=consentID):
            respone = self.post_sparql(userid=self.get_username(), password=self.get_password(),
                                       query=self.revoke_broken_consent_query(consentID=consentID),
                                       consent_id_for_logging=consentID, type="revoke")
            updateRevokations = NGAC().updateRevokation(token="admin_token",
                                                        _privacy_preference=NGAC().getpolicy("admin_token"),
                                                        consent_id=consentID
                                                        )

            return respone
        else:
            return self.processing_fail_message()


    def get_consent_data(self, level="all",consentID=None,consentProvidedBy=None):
        if level =="all":
            all_consent  = self.select_query_gdb(additionalData="consent_for_compliance")
            return json.loads(all_consent)
        elif level =="consent":
            all_consent  = self.select_query_gdb(additionalData="consent_for_compliance_consent",
                                                 consentID=consentID)
            return json.loads(all_consent)
        elif level =="dataprovider":
            all_consent  = self.select_query_gdb(additionalData="consent_for_compliance_dataprovider",
                                                 consentProvidedBy=consentProvidedBy)
            return json.loads(all_consent)

    def notify(self, data):
        header = {"Content-Type": "application/json"}
        r = requests.post(self.TRIGGER_URL_NOTIFY, data=json.dumps(data), headers=header)
        msg = json.loads(r.text)
        self.store(msg)

    def check_consent_expiry(self, exp_date):
        return  self.has_expired(exp_date)

    def get_processing_details_from_controller(self, whoseInfoDict):
        header = {"Content-Type": "application/json"}
        r = requests.post(self.TRIGGER_URL_CONTROLLER, data=json.dumps(whoseInfoDict), headers=header)
        msg = json.loads(r.text)
        return msg

    def get_trigger_type(self, level="all"):
        return "automated" if level == "all" else "user"

    def compliance_check_act(self, level="all",consentID=None,consentProvidedBy=None):
        howTriggered = self.get_trigger_type(level=level)
        responseList=[]
        consent_datas = self.get_consent_data(level=level, consentID=consentID, consentProvidedBy=consentProvidedBy)
        for consent_data in consent_datas["results"]["bindings"]:
            cid = self.remove_uris(consent_data["ConsentID"]["value"])
            dpid = self.decrypt_data(self.remove_uris(consent_data["DataProvider"]["value"]))
            exp_date = self.remove_xst_date(self.decrypt_data(
                self.remove_uris(consent_data["Duration"]["value"])))
            data_requester = self.decrypt_data(self.remove_uris(consent_data["DataRequester"]["value"]))
            data_controller = self.decrypt_data(self.remove_uris(consent_data["DataController"]["value"]))
            data_processor = self.decrypt_data(self.remove_uris(consent_data["DataProcessor"]["value"]))
            data_processing_list = [self.decrypt_data(self.remove_uris(litem))
                 for litem in consent_data["DataProcessing"]["value"].split(",")]
            purpose = self.decrypt_data(self.remove_uris(consent_data["Purpose"]["value"]))

            isAboutData = [self.decrypt_data(self.remove_uris(litem))
                 for litem in consent_data["Data"]["value"].split(",")]
            toCheckData = [{v.split("-")[0]: ast.literal_eval(v.split("-")[1])} for v in isAboutData]
            consent_data = {"data": toCheckData, "dataprocessing": data_processing_list, "purpose": purpose}
            for_requesting_info_from_dc_dp = {"ConsentID":cid,
                                              "data_requester_id":data_requester,
                                              "data_controller_id":data_controller,
                                              "data_processor_id":data_processor,
                                              "data_provider_id":dpid}
            fromControllerDetails = self.get_processing_details_from_controller(for_requesting_info_from_dc_dp)
            # [{'mobilecat': {'data': ['m', 'd']}}, {'SensorDataCategory': {'data': ['GPS', 'speed']}}]
            compliance_result = {}
            shouldNotify = False
            if not self.has_expired(expirydate=exp_date):
                #consent is valid and active so make further check
                if self.has_valid_purpose(purpose, fromControllerDetails["purpose"]):
                    if self.has_processing_rights(data_processing_list, fromControllerDetails["dataprocessing"]):
                        if self.is_doing_valid_data_processing(toCheckData, fromControllerDetails["data"]):
                            #all_good so ask for compliance from privacy and security
                            if self.joint_compliance(fordataprocessing=data_processing_list,
                                                     dataprovider=dpid,
                                                     purpose=purpose,
                                                     hasDataController=data_controller,
                                                     hasDataProcessor=data_processor
                                                     ):
                                shouldNotify = False
                            else:
                                compliance_result[
                                    "joint_compliance"] = "Failed to comply from security and privacy"
                                shouldNotify = True
                        else:
                            compliance_result[
                                "data"] = "Data (access) is different form what was consented"
                            shouldNotify = True
                    else:
                        compliance_result[
                            "dataprocessing"] = "Dataprocessing is different than what was consented"
                        shouldNotify = True
                else:
                    #purpose is invalid
                    compliance_result[
                        "purpose"] = "Data is used for different purpose {} than the requested in consent {}"\
                        .format(fromControllerDetails["purpose"],purpose)
                    shouldNotify = True
            else:
                # revoke the consent
                self.broken_consent(consentID=cid, reason_for_logging="Consent expired")
                compliance_result["consent_expired"] = "Consent has expired so consent has been automatically revoked"
                #consent has expired
                shouldNotify = True


            if shouldNotify:
                compliance_status = {"consent_info":for_requesting_info_from_dc_dp, "compliance_status":compliance_result}
                responseList.append(compliance_status)
            else:
                compliance_status = {"consent_info": for_requesting_info_from_dc_dp,
                                             "compliance_status": "Everything is good and compliant"}
                responseList.append(compliance_status)

        if howTriggered == "automated":
            self.notify({"compliance_check":responseList})

        else:
            message_resp = self.compliance_message()
            message_resp["message"] =  {"compliance_check":responseList}
            return message_resp



    def joint_compliance(self, fordataprocessing, dataprovider, purpose, hasDataController, hasDataProcessor):
        # call security and privacy with privacy setting specifics to your need
        # https://github.com/tog-rtd/SmashHit.git
        result =  NGAC().check_access_permission(fordataprocessing=fordataprocessing,
                                              dataprovider=dataprovider,
                                              purpose=purpose,
                                              hasDataController=hasDataController,
                                              hasDataProcessor=hasDataProcessor)

        return True if result=="success" else False


class ComplianceObligationNotification(smashHitmessages, Functions):
    def __int__(self):
        super(ComplianceObligationNotification, self).__int__()

    def store_compliance_obligation_notification_status(self, received_info):
        toReturn_Message = self.compliance_obligation_notification_message()
        received_info_msg = {
            "compliance_action_request": received_info["compliance_action_request"],
            "compliance_obligation_status": received_info["compliance_obligation_status"],
            "consent_id": received_info["consent_id"],
            "decision_token": received_info["decision_token"],
            "timestamp": str(datetime.datetime.utcnow())
        }
        data = {"received_info":received_info_msg, "acknowledge_message":toReturn_Message}
        record_success = self.store(data)
        if "SUCCESS" in record_success:
            return toReturn_Message
        else:
            message = self.insert_fail()
            message["message"] = "ERROR OCCURED, TRY AGAIN"
            return message





 
