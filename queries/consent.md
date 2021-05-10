# Research
## [STI Innsbruck](https://www.sti-innsbruck.at)

<p float=“left”>
<img src="https://www.sti-innsbruck.at/sites/default/files/uploads/media/STI-IBK-Logo_CMYK_Pfad_XL.jpg" alt="STI Innsbruck" width="200px"/>
</p>

# SPARQL QUERIES
- Use the repository: TestingNode

## Get all consent records (consent id and all information about it) from the smashHit knowledge graph. 
```
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
PREFIX gconsent: <https://w3id.org/GConsent#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?ConsentID ?Name ?Purpose ?Data ?Duration ?DataRequester ?DataController ?GrantedAtTime ?RevokedAtTime ?Medium
 WHERE { 
  ?ConsentID a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>.
  ?ConsentID :isProvidedBy ?Name.
  ?ConsentID :inMedium ?Medium.
  ?ConsentID :forPurpose ?Purpose.
  ?ConsentID :requestedBy ?DataRequester.
  ?ConsentID :isAboutData ?Data.
  ?ConsentID :hasExpiry ?Duration.
  ?ConsentID :hasDataController ?DataController.
  ?ConsentID :GrantedAtTime ?GrantedAtTime.
  ?ConsentID :RevokedAtTime ?RevokedAtTime.
}
 
```
## Get all ConsentID and Data Providers ....
```
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
SELECT ?ConsentID ?Name ?DataRequester ?DataController
 WHERE { 
  ?ConsentID :isProvidedBy ?Name.
  ?ConsentID :requestedBy ?DataRequester.
  ?ConsentID :hasDataController ?DataController.
} LIMIT 20
```
## Get ConsentID based on the name of the data provider ....
```
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>

SELECT ?ConsentID
 WHERE { 
  ?ConsentID :isProvidedBy :JaneDoe.	
} LIMIT 10 

```
## Get ConsentID and all ralated information based on the name of the data provider ....
``````
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>

SELECT ?ConsentID ?Purpose ?Data ?Duration ?DataRequester ?DataController ?GrantedAtTime ?RevokedAtTime ?Medium
 WHERE { 
  ?ConsentID :isProvidedBy :JaneDoe.
  ?ConsentID :inMedium ?Medium.
  ?ConsentID :forPurpose ?Purpose.
  ?ConsentID :requestedBy ?DataRequester.
  ?ConsentID :isAboutData ?Data.
  ?ConsentID :hasExpiry ?Duration.
  ?ConsentID :hasDataController ?DataController.
  ?ConsentID :GrantedAtTime ?GrantedAtTime.
  ?ConsentID :RevokedAtTime ?RevokedAtTime.
} LIMIT 10 

`````````
## Update existing consent statuses and it's date.

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

DELETE {?ConsentID :GrantedAtTime "2021-03-03T09:00:00"^^xsd:dateTime.
    ?ConsentID :RevokedAtTime "2021-04-30T09:00:00"^^xsd:dateTime.
}

INSERT {?ConsentID :GrantedAtTime "2020-03-03T09:00:00"^^xsd:dateTime.
		?ConsentID :RevokedAtTime "2020-04-30T09:00:00"^^xsd:dateTime. }

WHERE  {?ConsentID :GrantedAtTime "2021-03-03T09:00:00"^^xsd:dateTime.
    	?ConsentID :RevokedAtTime "2021-04-30T09:00:00"^^xsd:dateTime.
         FILTER (?ConsentID = :kg234562) 
}

```
## Consent revocation: Update existing consent status from "Granted" to "Revoked". The query creates a new isntance of the consent status with it's date.
```
INSERT DATA{:kg234562  :RevokedAtTime "2020-04-30T09:00:00"^^xsd:dateTime.}
``````
## Consent granting (for a new consent record, which does not have any consent decisions yet). The query needs the specific data (ConsentID, Consent granting date/time).  
```
INSERT DATA{?ConsentiD :GrantedAtTime "YYY-MM-DDT00:00:00"^^xsd:dateTime.}
```
