
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;
const readline = require("readline");
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Done');
});

var literaltype = "";
const SparqlClient = require('sparql-http-client');
const endpointUrl = 'https://smashhitactool.sti2.at/repositories/TestingNode';
const user = process.env.USERNAME
const password = process.env.PASSWORD


const prompt = require("prompt-sync")({ sigint: true });
//With readline select the query type
const question = prompt("Query by 1 - Name or 2 - ConsentID?");

//query by name-----------------------
if (question=='1') {

  const name=prompt("Name: ");
  /*const NameN=name.replace(/\w+/g, function(txt) {
  // uppercase first letter and add rest unchanged
  return txt.charAt(0).toUpperCase() + txt.substr(1);
  }).replace(/\s/g, '');// remove any spaces
  //console.log(NameN);
  const NameCorrect=name.replace(/\w+/g, function(txt) {
  // uppercase first letter and add rest unchanged
  return txt.charAt(0).toUpperCase() + txt.substr(1);
  })

*/
  server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
        console.log(" ");

      console.log(`Consent records for: ${name}`);
          console.log("-------------------------");
    });

  const queryByName=`
    PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>


    SELECT ?ConsentID ?Purpose ?DataController ?DataRequester ?Duration ?Data ?DataProcessing ?Status ?Date
     WHERE { 
      ?ConsentID :isProvidedBy :${name}.
      ?ConsentID :forPurpose ?Purpose.
      ?Purpose :forDataProcessing ?DataProcessing.
      ?ConsentID :hasDataController ?DataController.
      ?ConsentID :requestedBy ?DataRequester.
      ?ConsentID :hasExpiry ?Duration.
      ?ConsentID :isAboutData ?Data.
      ?ConsentID :GrantedAtTime ?GrantedAtTime.
      ?ConsentID :RevokedAtTime ?RevokedAtTime.
    
    } LIMIT 10 `;


async function f(){

const client = new SparqlClient({ endpointUrl, user, password})
const stream =  await client.query.select(queryByName)


stream.on('data', row => {
      Object.entries(row).forEach(([key, value]) => {
    
        console.log(`${key}: ${value.value}`)
      })
        console.log("------------------------------------------------------------")
        
      })

stream.on('error', err => {
      console.error(err)
    })
   // if(!stream.length){console.log("no record exists")} 

       
        }
        //if there is no query match in the KG 
 f()


}
//query by ConsentID
if (question=='2') {
  const consentID=prompt("ConsentID:");

  server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
       console.log(" ");

     console.log(`Consent records for: ${consentID}`);
        console.log("-------------------------");
});

  const consentIDN=consentID.toLowerCase();
  console.log(consentIDN);




const queryByConsentID=`
  PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>

  SELECT ?Status ?Purpose ?Name ?DataRequester ?DataController ?Duration ?Data ?Date ?GrantedAtTime ?RevokedAtTime ?DataProcessing 
   WHERE { 
    :${consentID} :isProvidedBy ?Name.
    :${consentID} :forPurpose ?Purpose.
    ?Purpose :forDataProcessing ?DataProcessing.
    :${consentID} :hasDataController ?DataController.
    :${consentID} :requestedBy ?DataRequester.
    :${consentID} :hasExpiry ?Duration.
    :${consentID} :isAboutData ?Data.
    :${consentID} :GrantedAtTime ?GrantedAtTime.
    :${consentID} :RevokedAtTime ?RevokedAtTime.
    

  } LIMIT 10 `;

async function f(){

const client = new SparqlClient({ endpointUrl, user, password})
    const stream =  await client.query.select(queryByConsentID)
    stream.on('data', row => {
      Object.entries(row).forEach(([key, value]) => {
    
        console.log(`${key}: ${value.value}`)
      })
              console.log("------------------------------------------------------------")
    })
        //if (!stream.length){console.log("no record exists")}//if there is no query match in the KG 

    stream.on('error', err => {
      console.error(err)
    })
  }
 f()

//query consent by user's consentID


}


