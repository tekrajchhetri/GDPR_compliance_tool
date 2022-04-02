# GDPR Compliance Tool
GDPR Compliance Tool is a core component of smashHit. smashHit is a Horizon 2020 project with the primary objective of creating a secure and trustworthy data-sharing platform with a focus on consent management in a distributed environment such as the automotiveindustry, insurance and smart cities following GDPR.

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


## Developer
- Tek Raj Chhetri 
- Web: [https://tekrajchhetri.com](https://tekrajchhetri.com)
- Twitter: [TekRaj_14](https://twitter.com/TekRaj_14) 


## Project
-  [smashHit](https://www.smashhit.eu/) 

## License
[MIT](https://github.com/tekrajchhetri/GDPR_compliance_tool/blob/master/LICENSE)
