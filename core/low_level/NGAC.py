# -*- coding: utf-8 -*-
# @Time    : 31.10.22 16:29
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : NGAC.py
# @Software: PyCharm

import json
import time
import aiohttp
import asyncio
import requests


class NGAC:
    async def gather_with_concurrency(self, n, *tasks):
        semaphore = asyncio.Semaphore(n)

        async def sem_task(task):
            async with semaphore:
                return await task

        return await asyncio.gather(*(sem_task(task) for task in tasks))

    async def addControllerNGAC(self, token, session, _controller_id, _privacy_policy):
        _URL = "REST_ENDPOINT"

        payload = {
            "token": token,
            "data_controller": f"dc[{_controller_id}]",
            "privacy_policy": _privacy_policy,
        }
        async with session.post(_URL, data=payload) as resp:
            data = await resp.text()
            return json.loads(data)["respStatus"]

    async def addProcessorNGAC(
        self, token, session, _processor_id, _data_controller, _privacy_policy
    ):
        _URL = "REST_ENDPOINT"

        payload = {
            "token": token,
            "data_processor": f"dp[{_processor_id}][{_data_controller}]",
            "data_controller": f"dc[{_data_controller}]",
            "privacy_policy": _privacy_policy,
        }
        async with session.post(_URL, data=payload) as resp:
            data = await resp.text()
            return json.loads(data)["respStatus"]

    async def addDataSubjectNGAC(
        self, token, session, _data_subject_id, _privacy_preference, _data_items
    ):
        _URL = "ENDPOINT"

        payload = {
            "token": token,
            "data_subject": f"ds[{_data_subject_id}]",
            "privacy_preference": _privacy_preference,
            "data_items": _data_items,
        }

        async with session.post(_URL, data=payload) as resp:
            data = await resp.text()
            return json.loads(data)["respStatus"]

    async def addConsentNGAC(
        self,
        token,
        session,
        consent_id,
        _processor_id,
        _data_controller,
        application,
        dataprocessingoperations,
        purpose,
        _data_subject_id,
        _privacy_preference,
        constraint,
    ):
        _URL = "REST_ENDPOINT"

        payload = {
            "token": token,
            "policy": _privacy_preference,
            "consent_id": consent_id,
            "data_controller": f"dc[{_data_controller}]",
            "data_processor": f"dp[{_processor_id}][{_data_controller}]",
            "application": f"dp[{_processor_id}][{_data_controller}]_{application}",
            "operations": str(
                [
                    f"dp[{_processor_id}][{_data_controller}]_{x}"
                    for x in dataprocessingoperations
                ]
            ),
            "purpose": f"p({purpose})",
            "data_subject": f"ds[{_data_subject_id}]",
            "data_item": f"pdi({_data_subject_id})[{_data_subject_id}]",
            "data_category": "pdc{" + _data_subject_id + "}",
            "constraint": constraint,
        }

        async with session.post(_URL, data=payload) as resp:
            data = await resp.text()
            return json.loads(data)["respStatus"]

    def updateRevokation(self, token, _privacy_preference, consent_id):
        _URL = "REST_ENDPOINT"

        payload = {
            "token": token,
            "policy": _privacy_preference,
            "consent_id": consent_id,
        }
        _r = requests.post(_URL, data=payload)
        return json.loads(_r.text)["respStatus"]

    def check_access_permission(
        self,
        purpose,
        hasDataProcessor,
        dataprovider,
        hasDataController,
        fordataprocessing,
        token="TOKEN",
    ):

        _URLP = f"ENDPOINT/getpol?token={token}"
        _rP = requests.get(_URLP)
        _privacy_preference = (
            json.loads(_rP.text)["respBody"]
            if len(json.loads(_rP.text)["respBody"]) > 4
            else "dplp_min"
        )

        payload = {
            "user": f"dp[{hasDataProcessor}][{hasDataController}]",
            "ar": str(
                [
                    f"dpo[{hasDataProcessor}][{hasDataController}]_{x}"
                    for x in fordataprocessing
                ]
            ),
            "purpose": f"p({purpose})",
            "policy": _privacy_preference,
            "object": f"pdi({dataprovider})[{dataprovider}]",
        }

        _URLacess = "ENDPOINT/access"
        _r = requests.get(_URLacess, params=payload)
        try:
            return json.loads(_r.text)["respMessage"]
        except Exception as ex:
            pass

    def getpolicy(self, yourtoken):
        _URLP = f"ENDPOINT/getpol?token={yourtoken}"
        _rP = requests.get(_URLP)
        yourprivacypoicy = (
            json.loads(_rP.text)["respBody"]
            if len(json.loads(_rP.text)["respBody"]) > 4
            else "dplp_min"
        )
        return yourprivacypoicy

    async def updateNGAC(
        self,
        requestedBy,
        hasDataController,
        hasDataProcessor,
        fordataprocessing,
        GrantedAtTime,
        inMedium,
        purpose,
        isAboutData,
        city,
        consentID,
        country,
        state,
        dataprovider,
        expirationtime,
    ):

        yourtoken = "XXXXXXXXXXXXXX"
        yourprivacypoicy = self.getpolicy(yourtoken)
        yourprivacy_preference = "XXXXXXXXXXXXXX"
        your_data_items = "XXXXXXXXXXXXXX"
        yourapplication = "XXXXXXXXXXXXXX"
        yourconstraint = "XXXXXXXXXXXXXX"

        conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
        session = aiohttp.ClientSession(connector=conn)

        conc_req = 4
        results = await self.gather_with_concurrency(
            conc_req,
            *[
                self.addControllerNGAC(
                    token=yourtoken,
                    session=session,
                    _controller_id=hasDataController,
                    _privacy_policy=yourprivacypoicy,
                ),
                self.addProcessorNGAC(
                    token=yourtoken,
                    session=session,
                    _processor_id=hasDataProcessor,
                    _data_controller=hasDataController,
                    _privacy_policy=yourprivacypoicy,
                ),
                self.addDataSubjectNGAC(
                    token=yourtoken,
                    session=session,
                    _data_subject_id=dataprovider,
                    _privacy_preference=yourprivacy_preference,
                    _data_items=your_data_items,
                ),
                self.addConsentNGAC(
                    token=yourtoken,
                    session=session,
                    _privacy_preference=yourprivacypoicy,
                    consent_id=consentID,
                    _processor_id=hasDataProcessor,
                    _data_controller=hasDataController,
                    _data_subject_id=dataprovider,
                    application=isAboutData,
                    dataprocessingoperations=fordataprocessing,
                    purpose=purpose,
                    constraint=yourconstraint,
                ),
            ],
        )

        await session.close()
        if "failure" in results:
            return "fail"
        else:
            return "success"
