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
## More Instructions

Please check [https://tekrajchhetri.com/opensource/gdpr_tool/](https://tekrajchhetri.com/opensource/gdpr_tool/) for instructions and additional details.

## API

![image](https://user-images.githubusercontent.com/52251022/144920140-4011ede4-919a-46e7-9581-73695953a57d.png)


## Deployment in Remote Server

## FaaS
![image](https://user-images.githubusercontent.com/52251022/120083394-b3f37080-c0c8-11eb-8362-99063e0fc720.png)


## Performance Monitor

![image](https://user-images.githubusercontent.com/52251022/120082126-7b9c6400-c0c1-11eb-874a-d5c4eb34e813.png)

![image](https://user-images.githubusercontent.com/52251022/120082109-68899400-c0c1-11eb-99cc-d4b23f80c89f.png)

## ACT and S&P interactions
![image](https://user-images.githubusercontent.com/52251022/220625143-9623a2e2-4af1-4561-ad13-7093ac39b68a.png)

Figure: Access check (single) without altering the data processing operation - “Collect”

![image](https://user-images.githubusercontent.com/52251022/220625176-f168c6a3-eaad-4196-a54a-2fdfb3a83f5b.png)

Figure: Access check (single) after altering the data processing operation - “Collect” to something different “test”

![image](https://user-images.githubusercontent.com/52251022/220625212-dab10c72-7406-4593-a2c4-dba311a43116.png)

Figure: Updating security and privacy upon consent revocation

![image](https://user-images.githubusercontent.com/52251022/220625237-b0472c02-1c9b-407a-ab20-0d960b1b402e.png)

Figure: Access check for multiple data processing operations


## Developer
- Tek Raj Chhetri 


## Project
-  [smashHit](https://www.smashhit.eu/) 

## License
[MIT](https://github.com/tekrajchhetri/GDPR_compliance_tool/blob/master/LICENSE)
