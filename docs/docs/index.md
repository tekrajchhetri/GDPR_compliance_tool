#Automatic Contracting Tool (ACT) 

This document will provide an overview of the Automatic Contracting Tool, its functionalities and technical details. 

## Introduction
## Example consent from BC1
The ACT expects the consent in the following JSON format for BC1 (Insurance) usecase.
```json
{
  "Agents": [
    {
      "id": "60a55c53d79bc757698041e9",
      "role": "controller"
    },
    {
      "id": "60a55c9dd79bc757698041ea",
      "role": "requester"
    }
  ],
  "DataProcessing": [
    "Analysis",
    "collection",
    "storage"
  ],
  "ExpirationDate": "Fri, 21 May 2021 12:10:39 GMT",
  "GivenAtLocation": "Madrid, Spain",
  "GrantedAtTime": "Fri, 21 May 2021 12:10:39 GMT",
  "Medium": "Online",
  "PersonaldataId": "AX12123422",
  "Purpose": "60a55bf3d79bc757698041e8",
  "Resource": {
    "PersonalData": [
      {
        "data": [
          "dateOfBirth",
          "address"
        ],
        "name": "whatever"
      }
    ],
    "SensorDataCategory": [
      {
        "data": [
          "GPS",
          "speed"
        ],
        "name": "cardata"
      }
    ]
  },
  "dataUsage": [
    "GPS",
    "speed",
    "milleage",
    "personalData",
    "trafficJamLocation"
  ]
}
```
## Commands


