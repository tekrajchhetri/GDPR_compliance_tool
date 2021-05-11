# Research 
## [STI Innsbruck](https://www.sti-innsbruck.at)
<p float="left">
<img src="https://www.sti-innsbruck.at/sites/default/files/uploads/media/STI-IBK-Logo_CMYK_Pfad_XL.jpg" alt="STI Innsbruck" width="200px"/>
</p>

# SPARQL QUERIES

## SPARQL QUERY ....
```
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX fibo-fnd-agr-ctr: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX fibo-fnd-plc-adr: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/>
insert data{
   :05\/05\/2021 rdf:type fibo-fnd-agr-ctr:hasEffectiveDate .
   :05\/05\/2021 rdf:type fibo-fnd-agr-ctr:hasExecutionDate .
   :05\/05\/2021 rdf:type dcat:startDate .
   :05\/05\/2024 rdf:type dcat:endDate .
   :ID_244562  dct:identifier :kg244562 .
   :ID_244563  dct:identifier :kg244563 .
   :ID_244563  dct:identifier :kg244564 .
   :ID_244563  dct:identifier :kg244565 .
   :WrittenContract rdf:type fibo-fnd-agr-ctr:WrittenContract .
    
   :Techniker_Strasse_7 rdf:type :hasAddress  .
   :Hansuntermuhler_Strasse_10 rdf:type :hasAddress  .
   :Westbhan_Strasse_2 rdf:type :hasAddress  .
   :Leopold_Strasse_15 rdf:type :hasAddress .
   
   :06759988813065 rdf:type :hasTelephone .
   :06759988813078 rdf:type :hasTelephone .
   :06759988813080 rdf:type :hasTelephone .
   :06759988813085 rdf:type :hasTelephone .
   
   :companyABC\@gmail.com rdf:type :hasEmail .
   :companyDEF\@hotmail.com rdf:type :hasEmail .
   :brade\@hotmail.com rdf:type :hasEmail .
   :george\@hotmail.com rdf:type :hasEmail .
    
   :Brade rdf:type prov:Agent .
   :Brade :hasStreetAddress :Techniker_Strasse_7 .
   :Brade :hasTelephone :06759988813065 .
   :Brade :hasEmail :brade\@hotmail.com .
    
   :George rdf:type prov:Agent .
   :George :hasStreetAddress :Leopold_Strasse_15 .
   :George :hasTelephone :06759988813085 .
   :George :hasEmail :george\@hotmail.com .
    
   :CompanyABC rdf:type prov:Organization . 
   :CompanyABC :hasStreetAddress :Hansuntermuhler_Strasse_10 .
   :CompanyABC :hasTelephone :06759988813078 .
   :CompanyABC :hasEmail :companABC\@gmail.com .
   
   :CompanyDEF rdf:type prov:Organization . 
   :CompanyDEF :hasStreetAddress :Westbhan_Strasse_2 .
   :CompanyDEF :hasTelephone :06759988813080 .
   :CompanyDEF :hasEmail :companyDEF\@hotmail.com .
   
   :Valid rdf:type :hasContractStatus .
   :InValid rdf:type :hasContractStatus .
   :1_year rdf:type :hasMinimumDuration .
   :6_month rdf:type :hasMinimumDuration .
   
}
```
================== Insert instances of a contract
```
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX fibo-fnd-agr-ctr: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
insert data{
    :kg244562 dcat:startDate :05-05-2021 .
    :kg244562 dcat:endDate :05-05-2022 .
    :kg244562 :contractType :WrittenContract .
    :kg244562 fibo-fnd-agr-ctr:hasEffectiveDate :05-05-2021 .
    :kg244562 fibo-fnd-agr-ctr:hasExecutionDate :05-05-2021 .
    :kg244562 :forPurpose "Creation of Contract for Vehicle data" .
    :kg244562 :inMedium :MobileApp123 .
    
    :kg244562 :ContractRequester :CompanyABC .
    :kg244562 :ContractProvider :Brade .
    
    :kg244562 :hasWaiver :hasWaiver .
    :kg244562 :hasAmendment :hasAmendment .
    :kg244562 :hasConfidentialityObligation :hasConfidentialityObligation .
    :kg244562 :hasDataProtection :hasDataProtection .
    :kg244562 :hasLimitationOnUse :hasLimitationOnUse .
    :kg244562 :hasMethodOfNotice :hasMethodOfNotice .
    :kg244562 :hasNoThirdPartyBeneficiaries :hasNoThirdPartyBeneficiaries .
    :kg244562 :hasPermittedDisclosure :hasPermittedDisclosure .
    :kg244562 :hasReceiptOfNotice :hasReceiptOfNotice .
    :kg244562 :hasSeverability :hasSeverability .
    :kg244562 :hasTerminationForInsolvency :hasTerminationForInsolvency .
    :kg244562 :hasTerminationForMaterialBreach :hasTerminationForMaterialBreach .
    :kg244562 :hasTerminationOnNotice :hasTerminationOnNotice .
    :kg244562 :hasContractStatus :Valid .
    :kg244562 :hasMinimumDuration :1_year .
    
    :kg244562 dct:identifier :ID_244562 .
    :kg244562 rdf:type :ContractId .
    
#    second instance of contract with two contract requester and a conract provider
    :kg244563 dcat:startDate :05-05-2021 .
    :kg244563 dcat:endDate :05-05-2022 .
    :kg244563 :contractType :WrittenContract .
    :kg244563 fibo-fnd-agr-ctr:hasEffectiveDate :05-05-2021 .
    :kg244563 fibo-fnd-agr-ctr:hasExecutionDate :05-05-2021 .
    :kg244563 :forPurpose "Creation of Contract for Vehicle data" .
    :kg244563 :inMedium :MobileApp123 .
    
    :kg244563 :ContractRequester :CompanyABC .
    :kg244563 :ContractRequester :CompanyDEF .
    :kg244563 :ContractProvider :Brade .
    
    :kg244563 :hasWaiver :hasWaiver .
    :kg244563 :hasAmendment :hasAmendment .
    :kg244563 :hasConfidentialityObligation :hasConfidentialityObligation .
    :kg244563 :hasDataProtection :hasDataProtection .
    :kg244563 :hasLimitationOnUse :hasLimitationOnUse .
    :kg244563 :hasMethodOfNotice :hasMethodOfNotice .
    :kg244563 :hasNoThirdPartyBeneficiaries :hasNoThirdPartyBeneficiaries .
    :kg244563 :hasPermittedDisclosure :hasPermittedDisclosure .
    :kg244563 :hasReceiptOfNotice :hasReceiptOfNotice .
    :kg244563 :hasSeverability :hasSeverability .
    :kg244563 :hasTerminationForInsolvency :hasTerminationForInsolvency .
    :kg244563 :hasTerminationForMaterialBreach :hasTerminationForMaterialBreach .
    :kg244563 :hasTerminationOnNotice :hasTerminationOnNotice .
    :kg244563 :hasContractStatus :Valid .
    :kg244563 :hasMinimumDuration :1_year .
    
    :kg244563 dct:identifier :ID_244563 .
    :kg244563 rdf:type :ContractId .
    
#    third instance of contract with two contract requester and a conract provider
    :kg244564 dcat:startDate :05-05-2021 .
    :kg244564 dcat:endDate :05-05-2022 .
    :kg244564 :contractType :WrittenContract .
    :kg244564 fibo-fnd-agr-ctr:hasEffectiveDate :05-05-2021 .
    :kg244564 fibo-fnd-agr-ctr:hasExecutionDate :05-05-2021 .
    :kg244564 :forPurpose "Creation of Contract for Vehicle data" .
    :kg244564 :inMedium :MobileApp123 .
    
    :kg244564 :ContractRequester :CompanyABC .
    :kg244564 :ContractProvider :Brade .
    :kg244564 :ContractProvider :George .
   
    :kg244564 :hasWaiver :hasWaiver .
    :kg244564 :hasAmendment :hasAmendment .
    :kg244564 :hasConfidentialityObligation :hasConfidentialityObligation .
    :kg244564 :hasDataProtection :hasDataProtection .
    :kg244564 :hasLimitationOnUse :hasLimitationOnUse .
    :kg244564 :hasMethodOfNotice :hasMethodOfNotice .
    :kg244564 :hasNoThirdPartyBeneficiaries :hasNoThirdPartyBeneficiaries .
    :kg244564 :hasPermittedDisclosure :hasPermittedDisclosure .
    :kg244564 :hasReceiptOfNotice :hasReceiptOfNotice .
    :kg244564 :hasSeverability :hasSeverability .
    :kg244564 :hasTerminationForInsolvency :hasTerminationForInsolvency .
    :kg244564 :hasTerminationForMaterialBreach :hasTerminationForMaterialBreach .
    :kg244564 :hasTerminationOnNotice :hasTerminationOnNotice .
    :kg244564 :hasContractStatus :Valid .
    :kg244564 :hasMinimumDuration :1_year .
   
    :kg244564 dct:identifier :ID_244564 .
    :kg244564 rdf:type :ContractId .
#    fourth instance of contract with two contract requester and a conract provider
    :kg244565 dcat:startDate :05-05-2021 .
    :kg244565 dcat:endDate :05-05-2022 .
    :kg244565 :contractType :WrittenContract .
    :kg244565 fibo-fnd-agr-ctr:hasEffectiveDate :05-05-2021 .
    :kg244565 fibo-fnd-agr-ctr:hasExecutionDate :05-05-2021 .
    :kg244565 :forPurpose "Creation of Contract for Vehicle data" .
    :kg244565 :inMedium :MobileApp123 .
    
    :kg244565 :ContractRequester :CompanyABC .
    :kg244565 :ContractRequester :CompanyDEF .
    :kg244565 :ContractProvider :Brade .
    :kg244565 :ContractProvider :George .
   
    :kg244565 :hasWaiver :hasWaiver .
    :kg244565 :hasAmendment :hasAmendment .
    :kg244565 :hasConfidentialityObligation :hasConfidentialityObligation .
    :kg244565 :hasDataProtection :hasDataProtection .
    :kg244565 :hasLimitationOnUse :hasLimitationOnUse .
    :kg244565 :hasMethodOfNotice :hasMethodOfNotice .
    :kg244565 :hasNoThirdPartyBeneficiaries :hasNoThirdPartyBeneficiaries .
    :kg244565 :hasPermittedDisclosure :hasPermittedDisclosure .
    :kg244565 :hasReceiptOfNotice :hasReceiptOfNotice .
    :kg244565 :hasSeverability :hasSeverability .
    :kg244565 :hasTerminationForInsolvency :hasTerminationForInsolvency .
    :kg244565 :hasTerminationForMaterialBreach :hasTerminationForMaterialBreach .
    :kg244565 :hasTerminationOnNotice :hasTerminationOnNotice .
    :kg244565 :hasContractStatus :Valid .
    :kg244565 :hasMinimumDuration :1_year .
   
    :kg244565 dct:identifier :ID_244565 .
    :kg244565 rdf:type :ContractId .
    
}
```
================== Update insert
```
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX fibo-fnd-agr-ctr: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX fibo-fnd-plc-adr: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/>
insert data{
      
      :hasDataController rdfs:domain :contract .
    	:CXAM rdf:type prov:Organization .
    	:CXAM :hasAssociation :kg244562 .
    	:CXAM :hasAssociation :kg244563 .
    	:CXAM :hasAssociation :kg244564 .
    	:CXAM :hasAssociation :kg244565 .
	   :Data_Controller rdf:type :DataController .
     	:CXAM :hasRole :Data_Controller .
      :1_Year :hasAssociation :kg244562 .
      :6_month :hasAssociation :kg244563 .
    	:6_month :hasAssociation :kg244564 .	
    	:1_year :hasAssociation :kg244565 .
      :kg244562 :hasExpiry :1_Year .
      :kg244563 :hasExpiry :6_month .
    	:kg244564 :hasExpiry :6_month .
    	:kg244565 :hasExpiry :1_Year .
    	:kg244562 :hasDataController :CXAM .
    	:kg244563 :hasDataController :CXAM .
    	:kg244564 :hasDataController :CXAM .
    	:kg244565 :hasDataController :CXAM .
   
}
```
================== Select an instance of a contract
```
PREFIX : <http://ontologies.atb-bremen.de/smashHitCore#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX fibo-fnd-agr-ctr: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

select * 
where{

    ?Contract a :ContractId;
              :forPurpose ?Purpose;
              :contractType ?ContractType;
              dcat:startDate ?StartDate;
              dcat:endDate ?EndingDate;
              fibo-fnd-agr-ctr:hasEffectiveDate ?EffectiveDate;
    		     fibo-fnd-agr-ctr:hasExecutionDate ?ExecutionDate;
              :inMedium ?Medium;
              :hasWaiver ?Waiver;
              :hasAmendment ?Amendment;
              :hasConfidentialityObligation ?ConfidentialityObligation;
              :hasDataProtection ?DataProtection;
              :hasLimitationOnUse ?LimitationOnUse;
              :hasMethodOfNotice ?MethodOfNotice;
              :hasNoThirdPartyBeneficiaries ?NoThirdPartyBeneficiaries;
              :hasPermittedDisclosure ?PermittedDisclosure;
              :hasReceiptOfNotice ?ReceiptOfNotice;
              :hasSeverability ?Severability;
              :hasTerminationForInsolvency ?TerminationForInsolvency;
              :hasTerminationForMaterialBreach ?TerminationForMaterialBreach;
              :hasTerminationOnNotice ?TerminationOnNotice;
              
}
```
