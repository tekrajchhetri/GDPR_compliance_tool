# Research
## [STI Innsbruck](https://www.sti-innsbruck.at)
<p float=“left”>
<img src=“https://www.sti-innsbruck.at/sites/default/files/uploads/media/STI-IBK-Logo_CMYK_Pfad_XL.jpg” alt=“STI Innsbruck” width=“200px”/>
</p>
# SPARQL QUERIES
## Get all consent records (consent id and all information about it) from the smashHit knowledge graph. Use the repository: TestingNode ....
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
LIMIT 200

 
```
## SPARQL QUERY2 description ....
```
query2
```
## SPARQL QUERY3 description ....
```
query3
```
## SPARQL QUERY4 description ....
```
query4
```
## SPARQL QUERY5 description ....
```
query5
```
