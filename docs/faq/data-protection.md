---
title: Data Protection
hide:
  - toc
---


??? "1. How is the data protected? What is the data protection policy?"

      510, digital and data unit, is part of the The Netherlands Red Cross (NLRC). The NLRC has a **Data Protection Policy** enforced since 2018. **Both the NLRC and the 121 platform adhere to the European General Data Protection Regulation (GDPR)**. The GDPR also specified data breach reporting, which has to be reported to Dutch Autoriteit Persoonsgegevens. NLRC employs a legal officer specialized in data protection. NLRC is a data processor for the client, and this is agreed in the Service Level Agreement (SLA). For more information about data processor: https://www.gdpreu.org/the-regulation/key-concepts/data-controllers-and-processors/ 

      The partner remains the data controller and is therefore responsible for any data entered into the platform. The partner should therefore be informed and in compliance with their data protection legislation.

      Please, contact our Account Manager Team to **discuss any requirements and questions** in regard to our GDPR responsabilities at <info@121.global>.

??? "2. Where and how do you store and process data?"

    The 121 Platform and The Netherlands Red Cross (NLRC) adheres to the General Data Protection Regulation (GDPR), which is the most comprehensive and restrictive of the jurisdiction. Data is stored, hosted and processed in West Europe.
  
    If you use KOBO toolbox for registration, the data will remain stored in the KOBO server. Kindly note this is separate from 121 platform data process and outside of our control.


??? "3. What is your cloud server and host provider?"

    The 121 Platform runs in Microsoft Azure Cloud. By default, the location for all resources is Western Europe. Optionally, and upon request to our team, it may be possible to host and store the data in a different region. Please, contact our team for further information <info@121.global>.

    It may be possible to host the 121 platform in the country which data storage and processing is happening but this depends on location availability of Azure datacenters. 


??? "4. Can you host the data in-country?"

    Depending on availability of Azure datacenters, data storage and processing may be possible in-country. Alternative options can be discussed with our team, such as alternative IaaS or PaaS providers, or an on-premise hosting solutions. 
   
    Note that hosting data on-premise servers, or on third-party servers for which we have no agreement contract, may affect the 121 platform maintenance. It may require your team to support the maintenance of your 121 instance.
    
    Please contact us to discuss best alternatives and solutions on <info@121.global>.


??? "5. In which geographical locations do you store or process data?"

    Data is stored, hosted and processed in West Europe on Azure Cloud servers.
  
    If you use KOBO toolbox for registration, the data will remain stored in the KOBO server, which is located in Europe. Kindly note this is separate from 121 platform data process and outside of our control.

    If you use Twilio Inc.’s, telecommunications services, the data will be stored in a server located the United States. Twilio Inc. participates in the EU-US Data Privacy Framework. More information on how Twilio processes personal data can be found in its [Data Protection Addendum.](https://www.twilio.com/en-us/legal/data-protection-addendum)


??? "6. How long do you store the data?"

    The data is stored for a maximum of 7 years on our Azure cloud server after the last update. Data that has not been updated in the last 7 years will be deleted from the cloud server. If your programmes require a shorter storage period, this can be requested from our team. 

    Upon closure of your instance, your data will be deleted and erased from our cloud server - including users, programs and beneficiary details. Beware that this action is irreversible and data cannot be recovered afterwards. Should any personal data still be relevant we kindly ask you to save any necessary recordings beforehand.

    **Data collected with third party tool** integrated with 121 platform are not hosted on our servers. Third party handle the data storage. For instance, data collected with KOBO tool will be stored on KOBO servers and fall under their data protection policy. Similar conditions apply to Twilio Inc. or other third-party integrated to the 121 Platform. Kindly note this is separate from 121 platform data process and outside of our control. Please, refer to article 5 of our FAQ, Data Protection Section.

??? "7. How do you ensure data confidentiality, integrity and availability?"

    **Confidentiality** is protected by allowing only a limited, controlled, set of administrators access the production-related resources in Azure. Also, confidentiality is protected by having separate 121 instances with seperate databases and credentials for each client, and for each client having individual user accounts with role-based access to the data, including the technical administrator.

    **Availability** is protected by using an optimized configuration of resources in Microsoft Azure, including automated back-ups and health checks. Furthermore, automated exception reports are set up, so that in case of service unavailability, the DevOps team can quickly respond. Also, any new code is thoroughly tested using both automated tests and manual tests before going into production.

    **Integrity** is protected by extensive testing of the software using various types of automated and also manual tests, and using DBMS-provided integrity functionality with an ERD in 3rd normal form (primary key-foreign key relationships, unique contraints, not null columns, and the like). Malicious attempts at accessing the data are mitigated by daily monitoring of logs and resources and by regular pentests performend by an external company. The whole The Netherlands Red Cross (NLRC) has undersigned the IFRC Code of Conduct and also external contractors do so.

??? "8. Who processes the data?"

    The main processor is NLRC, who is subject to the EU General Data Protection Regulation (GDPR). It maintains the 121 platform but will only access personal data if necessary to provide support or for product improvements. 

    However, to operate the 121 platform, several data processors (trusted parties that assist with the actual functioning of the platform) are required.  

    The user can find more information about the third parties (sub-processors) involved in 121 and review their Data Protection Addendums through the links provided below: 

      - **Microsoft Azure Legal Information** [https://azure.microsoft.com/en-us/support/legal/](https://azure.microsoft.com/en-us/support/legal/)

        And when applicable:

    - **Twilio Flex** [https://www.twilio.com/en-us/legal/online-terms-updates](https://www.twilio.com/en-us/legal/online-terms-updates)  

      - **KoboToolbox** [https://www.ifrc.org/ifrc-kobo](https://www.ifrc.org/ifrc-kobo)

    121 can also make use of EspoCRM, an open-source software self-hosted by the client in a server with a location chosen by the client  [https://www.espocrm.com/tos/](https://www.espocrm.com/tos/)

??? "9. What are my responsabilities as a 121 user?"

    Below you can find a non-exhaustive list of user responsibilities regarding the protection of personal data processed through the 121 platform. Please note that there might be other obligations imposed by national or international legislation applicable to your organization.
    
    **Non-exhaustive list of user responsibilities:**  

    - Ensure adherence to applicable legislation. 
    - Ensure that anyone with access to 121 under the NS or Organisation must maintain the confidentiality of their account and password. 
    - Ensure that all personnel involved, including new staff, are adequately trained for their roles and understand their responsibilities and the importance of data protection.  
    - Evaluate if a data protection impact assessment (DPIA) is required for the specific use-case and context. A DPIA assesses privacy risks associated with the processing of personal data and determines necessary measures to mitigate the identified risks effectively. An outline of DPIAs can be found here (this link is only to provide information about the general DPIA process, your NS or Organisation may be subject to a different set of requirements). 
    - Establish and adhere to a data retention policy that accurately reflects the nature and sensitivity of the personal data processed.  
    - Provide adequate and understandable information about personal data processing and any related rights to the data subjects in local language(s), in line with the applicable legislation requirements.  
    - Ensure that data subjects can effectively exercise their rights, such as their access, rectification, erasure, and objection rights, or any additional rights granted under the applicable legislation.  
    - Have a data breach protocol in place. 

    Consider any other requirements that may be imposed by applicable legislation.

??? "10. What are some additional privacy best practices for end-users?"

    Recommended reading for the Red Cross Red Crescent movement users:

    - IFRC Practical Guidance for Data Protection in Cash and Voucher Assistance 
    - IFRC Data Protection overview and general best practices  

    Recommended reading to all Organisations:

    - General Data Protection Regulation (GDPR)

    - Module 3 (Data and Digital responsibility) of the Data and Digital Literacy Introduction Course 

    Additional recommendations: 

    - Do Not collect more data than is necessary for the purpose of the specific program. 
    - Do Not keep data for longer than necessary. 
    - Performing monthly/bi-monthly access review. 
    - Handle responsibly any excel files exported from 121. 

    This is strongly adviced to delete the files after doing the duplication check in way that cannot be easily recovered. The User may apply additional measures such as protecting the workbook with a password. This can be done following this steps: 

      - Select File > Info.
      - Select the Protect Workbook box and choose Encrypt with Password. 
      - Enter a password in the Password box, and then select OK. 
      - Confirm the password in the Reenter Password box, and then select OK. 
      - Update the initial password shared with you to access the 121 platform and choose a robust new password (e.g., use passphrases containing capital letters, numbers and symbols). 
      - Follow a data protection training.  
      - Use a digital password manager (e.g., Bitwarden) 


-8<- "docs/_snippets/contact-support.md"
