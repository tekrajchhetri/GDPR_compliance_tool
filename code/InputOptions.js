//Script to allow selection between quering the knowledge graph and annotating consent



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
const user='admin';
const password='Sm@shHitA_CT00L';


const prompt = require("prompt-sync")({ sigint: true });
//With readline select the query type
const question = prompt("1 - Query or 2 - Annotate?");

if (question=='1') {
	var circle = require('./getData.js');
	//console.log( 'done');
}
if (question=='2') {
	var circle = require('./Annotate.js');
	//console.log( 'done');
};