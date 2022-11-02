# -*- coding: utf-8 -*-
# @Time    : 31.10.22 16:29
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : NGAC.py
# @Software: PyCharm

import requests
import json
import time
import aiohttp
import asyncio


class NGAC:
    def __init__(self) -> None:
        self.results = []

    async def gather_with_concurrency(self, n, *tasks):
        semaphore = asyncio.Semaphore(n)

        async def sem_task(task):
            async with semaphore:
                return await task

        return await asyncio.gather(*(sem_task(task) for task in tasks))

    async def addControllerNGAC(self, session, _controller_id, _privacy_policy):
        _URL = "REST_ENDPOINT"

        payload = {
            "token": "admin_token",
            "data_controller": f"dc[{_controller_id}]",
            "privacy_policy": _privacy_policy
        }
        async with session.post(_URL,
                                data=payload) as resp:
            data = await resp.text()
            return json.loads(data)['respStatus']

    async def addProcessorNGAC(self, session, _processor_id, _data_controller, _privacy_policy):
        _URL = "REST_ENDPOINT"

        payload = {
            "token": "admin_token",
            "data_processor": f"dp[{_processor_id}]",
            "data_controller": f"dc[{_data_controller}]",
            "privacy_policy": _privacy_policy
        }
        async with session.post(_URL,
                                data=payload) as resp:
            data = await resp.text()
            return json.loads(data)['respStatus']

    async def addDataSubjectNGAC(self, session, _data_subject_id, _privacy_preference, _data_items):
        _URL = "REST_ENDPOINT"

        payload = {
            "token": "admin_token",
            "data_subject": f"ds[{_data_subject_id}]",
            "privacy_preference": _privacy_preference,
            "data_items": _data_items
        }

        async with session.post(_URL,
                                data=payload) as resp:
            data = await resp.text()
            return json.loads(data)['respStatus']

    async def updateNGAC(self, requestedBy, hasDataController, hasDataProcessor, fordataprocessing, GrantedAtTime,
                         inMedium, purpose,
                         isAboutData, city, consentID, country, state, dataprovider, expirationtime):

        yourprivacypoicy = "YYY"
        yourprivacy_preference = "XXX"
        your_data_items = "XXX"

        conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
        session = aiohttp.ClientSession(connector=conn)

        conc_req = 4
        results = await self.gather_with_concurrency(conc_req, *[
            self.addControllerNGAC(session=session, _controller_id=hasDataController, _privacy_policy=yourprivacypoicy),
            self.addProcessorNGAC(session=session, _processor_id=hasDataProcessor, _data_controller=hasDataController,
                                  _privacy_policy=yourprivacypoicy),
            self.addDataSubjectNGAC(session=session, _data_subject_id=dataprovider,
                                    _privacy_preference=yourprivacy_preference,
                                    _data_items=your_data_items)
            ])

        await session.close()

        if 'failure' in results:
            return "fail"
        else:
            return 'success'
