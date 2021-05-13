const SparqlClient = require('sparql-http-client')
const endpointUrl = 'https://smashhitactool.sti2.at/repositories/TestingNode/statements'
const updateUrl= endpointUrl
const storeUrl = updateUrl
const user = process.env.USERNAME
const password = process.env.PASSWORD

const prompt = require("prompt-sync")({ sigint: true });
//With readline select the query type
console.log("------Consent Funtions-----");
console.log("Enter the following information:");


//Insert new consent recoed in the knowledge graph-----------------------

 const ConsentID=prompt("ConsentID: ");
 const DataProvider=prompt("Data Provider: ");
 const Purpose=prompt("Purpose for consent: ");
 const DataProcessing=prompt("Data Processing: ");
 const Duration=prompt("Duration: ");
 const DataController=prompt("Data Controller: ");
 const DataRequester=prompt("Data Requester: ");
 const Data=prompt("Consent about data type: ");
 const GrantedAtTime=prompt("GrantedAtTime: ");
 const RevokedAtTime=prompt("RevokedAtTime: ");
 const Medium=prompt("Medium: ");



const InsertConsentQuery = `
  		PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>

        INSERT DATA {:${ConsentID} a <http://ontologies.atb-bremen.de/smashHitCore#ConsentID>;
          	:isProvidedBy :${DataProvider};
           	:inMedium :${Medium};
          	:forPurpose :${Purpose};
          	:requestedBy :${DataRequester};
         	:isAboutData :${Data};
         	:hasExpiry :${Duration};
        	:hasDataController :${DataController};
         	:GrantedAtTime :${GrantedAtTime};
        	:RevokedAtTime :${RevokedAtTime}.
        	:${Purpose} :forDataProcessing :${DataProcessing}.}

 `
const client = new SparqlClient({ endpointUrl, updateUrl, user, password})
async function f(){
const stream = await client.query.update(InsertConsentQuery)

}

f().catch(() => {});





