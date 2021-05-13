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
const user = process.env.USERNAME
const password = process.env.PASSWORD


const prompt = require("prompt-sync")({ sigint: true });
//With readline select the query type
const question = prompt("1 - Query or 2 - Annotate?");

if (question=='1') {
	var x = require('./getData.js');
	//console.log( 'done');
}
else if(question=='2') {
	var y = require('./insertData.js');
	//console.log( 'done');
}
