![image](https://user-images.githubusercontent.com/52251022/216262953-b50d0c97-ca1b-46d9-ad81-881575f1b140.png)
**Abstract:** The enforcement of the GDPR in May 2018 has led to a paradigm shift in data protection. Organizations face significant challenges, such as demonstrating compliance (or auditability) and automated compliance verification due to the complex and dynamic nature of consent, as well as the scale at which compliance verification must be performed. Furthermore, the GDPR’s promotion of data protection by design and industrial interoperability requirements has created new technical challenges, as they require significant changes in the design and implementation of systems that handle personal data. We present a scalable data protection by design tool for automated compliance verification and auditability based on informed consent that is modeled with a knowledge graph. Automated compliance verification is made possible by implementing a regulation-to-code process that translates GDPR regulations into well-defined technical and organizational measures and, ultimately, software code. We demonstrate the effectiveness of the tool in the insurance and smart cities domains. We highlight ways in which our tool can be adapted to other domains.

**Keywords:** GDPR; privacy; compliance verification; informed consent; standard data protection model; data sharing; data protection by design; knowledge graph; distributed systems

**URL:** https://www.mdpi.com/1424-8220/22/7/2763 

# Publication
This work is part of "*Data Protection by Design Tool for Automated GDPR Compliance Verification Based on Semantically Modeled Informed Consent*". Therefore, if you use any code from this or [https://github.com/tog-rtd/SmashHit.git](https://github.com/tog-rtd/SmashHit.git) repository, please cite our work.

```
@Article{s22072763,
AUTHOR = {Chhetri, Tek Raj and Kurteva, Anelia and DeLong, Rance J. and Hilscher, Rainer and Korte, Kai and Fensel, Anna},
TITLE = {Data Protection by Design Tool for Automated GDPR Compliance Verification Based on Semantically Modeled Informed Consent},
JOURNAL = {Sensors},
VOLUME = {22},
YEAR = {2022},
NUMBER = {7},
ARTICLE-NUMBER = {2763},
URL = {https://www.mdpi.com/1424-8220/22/7/2763},
ISSN = {1424-8220},
ABSTRACT = {The enforcement of the GDPR in May 2018 has led to a paradigm shift in data protection. Organizations face significant challenges, such as demonstrating compliance (or auditability) and automated compliance verification due to the complex and dynamic nature of consent, as well as the scale at which compliance verification must be performed. Furthermore, the GDPR&rsquo;s promotion of data protection by design and industrial interoperability requirements has created new technical challenges, as they require significant changes in the design and implementation of systems that handle personal data. We present a scalable data protection by design tool for automated compliance verification and auditability based on informed consent that is modeled with a knowledge graph. Automated compliance verification is made possible by implementing a regulation-to-code process that translates GDPR regulations into well-defined technical and organizational measures and, ultimately, software code. We demonstrate the effectiveness of the tool in the insurance and smart cities domains. We highlight ways in which our tool can be adapted to other domains.},
DOI = {10.3390/s22072763}
}
```




## System Architecture
![updated_act-paper-2-tek](https://user-images.githubusercontent.com/52251022/156544074-12c0934a-47a8-4133-8910-196e1afe088b.jpg)

## Privacy and Security 
The tool's security and privacy component is implemented in Prolog by Rance DeLong from [Open group](https://www.opengroup.org) and extends the [Next Generation Access Control (NGAC)](https://standards.incits.org/apps/group_public/project/details.php?project_id=2328) framework, which is a framework for attribute-based access control. The security and privacy component's source code can be accessed via the link below.
 
- https://github.com/tog-rtd/SmashHit.git

## Software Requirements
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask-JWT](https://flask-jwt-extended.readthedocs.io/en/stable/) 
- [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/)
- [Docker](https://www.docker.com)
- [flask_apispec](https://flask-apispec.readthedocs.io/en/latest/index.html)
- [SPARQLWrapper](https://rdflib.dev/sparqlwrapper/)
- [Confluent](https://www.confluent.io)
- [Ofelia - a job scheduler](https://github.com/mcuadros/ofelia)
- [unittest](https://docs.python.org/3/library/unittest.html)
- [OpenFaaS](https://www.openfaas.com/)
- [mongoDB](https://www.mongodb.com/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en)
- [Spacy](https://spacy.io)
- [NLTK](http://www.nltk.org)
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)


## Cluster Information
- Tier: M0 Sandbox (General)
- Cluster: AWS / Frankfurt (eu-central-1)
- Type: Replica Set - 3 nodes

## Running Locally
Run the command below from the root directory for deployement and access via [http://localhost:5001](http://localhost:5001). The Swagger API documentation can be accessed via [http://localhost:5001/swagger-ui/](http://localhost:5001/swagger-ui/).
```bash
bash docker_run.sh

```

## API

![image](https://user-images.githubusercontent.com/52251022/144920140-4011ede4-919a-46e7-9581-73695953a57d.png)


## Deployment in Remote Server

## FaaS
![image](https://user-images.githubusercontent.com/52251022/120083394-b3f37080-c0c8-11eb-8362-99063e0fc720.png)


## Performance Monitor

![image](https://user-images.githubusercontent.com/52251022/120082126-7b9c6400-c0c1-11eb-874a-d5c4eb34e813.png)

![image](https://user-images.githubusercontent.com/52251022/120082109-68899400-c0c1-11eb-99cc-d4b23f80c89f.png)



## Instructions
This tool's distributed nature enables the installation of different components on multiple (or the same) servers. Anyone wishing to deploy and utilize these tools should follow the deployment steps outlined below.
- First, ensure that MongoDB and GraphDB have been installed. MongoDB is used for logging and GraphDB for storing instances of knowledge graphs. You can use the links below for more information and download
	- [GraphDB Download](https://www.ontotext.com/products/graphdb/download/)
	- [GraphDB Installation & System Requirements](https://graphdb.ontotext.com/documentation/10.0/installation.html)
	- [MongoDB Download](https://www.mongodb.com/try/download/community)
	- After successful installation of GraphDB, you should have access to the GraphDB user interface (the same is the case with MongoDB).
		<img width="1407" alt="image" src="https://user-images.githubusercontent.com/52251022/220882815-16e2c85f-79e2-4c9f-8648-12b0cc8db656.png">
	
	Note: You can use a database other than GraphDB, but you might have to make the adjustment in code.
- Deploy the OpenFaaS serverless functions that are present in [core/func](https://github.com/tekrajchhetri/GDPR_compliance_tool/tree/master/core/func). Follow the steps below for the deployment of serverless functions.
	- Install faasd 
		```sh
            $ git clone https://github.com/openfaas/faasd --depth=1
            $ cd faasd
            $ ./hack/install.sh
       ```
	- Install OpenFaaS CLI
		```sh 
        $ curl -sSL https://cli.openfaas.com | sudo -E sh 
        ```
	- Deploy the serverless functions
		```sh 
        		$ faas-cli up -f stack.yml 
   		```
	- For further deployment and installation instructions for OpenFaaS/OpenFaaS functions or serverless functions, refer to the links below.
		- [Deployment](https://docs.openfaas.com/deployment/)
		- [Deployment guide for Kubernetes](https://docs.openfaas.com/deployment/kubernetes/)
		- [OpenFaaS](https://docs.openfaas.com/cli/install/)  
	- After a successful installation, you should have access to the OpenFaaS user interface (UI), where you can see your deployed functions. You can also deploy new functions using the UI.
		<img width="1408" alt="openfaasui" src="https://user-images.githubusercontent.com/52251022/220880579-5bb4a369-c015-49df-b537-e58f5fb4c61f.png">

		![deploynewfunc](https://user-images.githubusercontent.com/52251022/220880651-8fd8c134-aceb-44f6-82c1-7135e0b55440.png)
		![image](https://user-images.githubusercontent.com/52251022/220886534-0ff8366b-d43e-4186-afc8-dc4356d94d10.png)



	-  After setting up the databases, deploying the serverless functions, and integrating components such as service layers, you should be able to observe logging information from various operations such as consent creation flowing into the MongoDB database.
		<img width="1023" alt="image" src="https://user-images.githubusercontent.com/52251022/220883467-daa7494f-2e40-4a77-bbf3-abcc2d3dbb10.png">
	
	**Note**: Before the deployment of functions, do not forget to adjust the connection parameters depending on your installations.
- Next is the deployment of the [security and privacy component](https://github.com/tog-rtd/SmashHit). Since the security and privacy component is written in Prolog, you must install all prerequisites for running Prolog programs and deploying the component. The following link should be useful for the deployment of the Prolog-based application.

	- [SWI-Prolog](https://www.swi-prolog.org/download/stable)
	- After the security and privacy component and service layer have been successfully deployed, you should be able to interact with security and privacy components for operations such as access checks.
	
		![image](https://user-images.githubusercontent.com/52251022/220625143-9623a2e2-4af1-4561-ad13-7093ac39b68a.png)

		Figure: Access check (single) without altering the data processing operation - “Collect”

		![image](https://user-images.githubusercontent.com/52251022/220625176-f168c6a3-eaad-4196-a54a-2fdfb3a83f5b.png)

		Figure: Access check (single) after altering the data processing operation - “Collect” to something different “test”

		![image](https://user-images.githubusercontent.com/52251022/220625212-dab10c72-7406-4593-a2c4-dba311a43116.png)

		Figure: Updating security and privacy upon consent revocation

		![image](https://user-images.githubusercontent.com/52251022/220625237-b0472c02-1c9b-407a-ab20-0d960b1b402e.png)

		Figure: Access check for multiple data processing operations
- Once you have deployed all other components, you can deploy the service layer component as well as  the scheduler. To be able to deploy the service layer and the scheduler, you first need to install Docker. You can install Docker by following the installation instructions at the link below: 
	- [Docker Installation](https://docs.docker.com/engine/install/)
	- After installing Docker, you can run the `docker_run.sh` file to deploy the service layer and the scheduler. If everything goes well, you should see the URL to access the API (application programming interface) endpoints, and you should also be able to access the Swagger UI.
	![docker-deployment](https://user-images.githubusercontent.com/52251022/221034060-5e5dce65-63d9-490a-a6bf-95439033cb3d.png)
	
	<img width="1370" alt="screen-api" src="https://user-images.githubusercontent.com/52251022/221034111-4bb4b288-3d52-4a29-b074-bbe45955bba9.png">


	-  Upon successful deployment you should be able to perform the operations like consent creation and JWT login.
		<img width="1050" alt="image" src="https://user-images.githubusercontent.com/52251022/221037627-d60c1fb6-10c6-4ed3-b613-e92f18c1f30b.png">

		<img width="1050" alt="image" src="https://user-images.githubusercontent.com/52251022/221037665-8107fb0f-1b0d-44fc-b1d8-766c278148fb.png">

## Debugging 
- Sometimes you might get dependency error. This might be due to your system configuration so ensure that there's no conflict of the libraries.
![dependency-error-annotated](https://user-images.githubusercontent.com/52251022/221037253-34e61885-99af-4d8c-bb00-a115993ca37b.png)


## Developer
- Tek Raj Chhetri 


## Project
-  [smashHit](https://www.smashhit.eu/) 

## License
[MIT](https://github.com/tekrajchhetri/GDPR_compliance_tool/blob/master/LICENSE)
