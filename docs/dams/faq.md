---
layout: dams-doc
title: Shared DAMS FAQ
permalink: /docs/dams/faq/
breadcrumbs: DAMS User Guide
---

<a href="#faq1">1. What is the UCLDC?</a><br>
<a href="#faq2">2. What is the UCLDC shared DAMS?</a><br>
<a href="#faq3">3. Who can use and access the shared DAMS?</a><br>
<a href="#faq4">4. What kinds of resources can be managed in it?</a><br>
<a href="#faq5">5. What was the vision for a systemwide DAMS and where did it come from?</a><br> 
<a href="#faq6">6. How was the UCLDC model determined and why was Nuxeo selected as the shared DAMS?</a><br>
<a href="#faq7">7. How long did it take to implement the DAMS and make it available to the Libraries?</a><br>
<a href="#faq8">8. What does Nuxeo offer the UC Libraries right now (September 2015)?</a><br>
<a href="#faq9">9. What does Nuxeo offer in the way of support for the Libraries?</a><br>
<a href="#faq10">10. What kind of metadata schemes does Nuxeo support?</a><br>
<a href="#faq11">11.  What are the technical components of Nuxeo?</a><br>
<a href="#faq12">12.  Are the metadata records and files (that are stored in Nuxeo) backed up?</a><br>
<a href="#faq13">13. Does Nuxeo/the current UCLDC stack support linked data?</a><br>
<a href="#faq14">14.  What plans are in place to enhance Nuxeo, to meet any additional or new use cases or requirements?</a><br>
<a href="#faq15">15. Does the shared DAMS and UCLDC allow for co-development or other collaboration opportunities with the campus libraries?</a><br>
<a href="#faq16">16. Does CDL plan to charge for use of the Nuxeo DAMS?</a><br>
<a href="#faq17">17. Is CDL exploring other options beyond Nuxeo?</a><br>	
<a href="#faq18">18. If CDL and the Libraries decide to move to another platform for the shared DAMS, is there a strategy for migrating content out of Nuxeo to the new solution?</a><br>
<br>


## The Basics
***

### <a name="faq1">1. What is the UCLDC?</a>

The UC Libraries Digital Collection (UCLDC) is a technical stack for managing, aggregating, and providing access to digital resources owned by institutions across the libraries and the state. It provides:

* A pipeline for exposing metadata broadly
* A showcase for digital collections
* A DAMS for creating and storing digital content and metadata
* A registry for planning future initiatives

<a href="https://wiki.library.ucsf.edu/display/UCLDC/UCLDC+Model+and+Major+Components">Our project wiki</a> has some older but still-relevant information about the technical model.

### <a name="faq2">2. What is the UCLDC shared DAMS?</a>

One component of the larger UCLDC framework, the shared DAMS (digital asset management system) is a tool for creating and managing object-level metadata and content files. It also provides workflows for, if desired, publishing digital objects to Calisphere (for public access) and/or depositing them in Merritt (for long-term preservation). The shared DAMS is a customized implementation of <a href="http://www.nuxeo.com/">Nuxeo</a>, an enterprise platform that is used by a variety of organizations–from media companies to CollectionSpace (developed by UC Berkeley and the Museum of the Moving Image)–for their content management needs. <a href="https://registry.cdlib.org/documentation/docs/dams/index/">Learn more about the DAMS...</a>.

### <a name="faq3">3. Who can use and access the shared DAMS?</a>

Only authorized users—UC Libraries staff, student workers, and other individuals expressly designated by the UC Libraries—may use the shared DAMS. The libraries can control permissions for their staff for performing various functions in the system such as creating objects and editing metadata. <a href="https://registry.cdlib.org/documentation/docs/dams/dams-policies/">For more information...</a>

Note that in the UCLDC model, the shared DAMS does not provide public access to end-users. Rather, the public interface (Calisphere) is a separate layer of the UCLDC stack, which allows us to aggregate and display collections from both the DAMS and other sources such as campus Fedora-based systems.

### <a name="faq4">4. What kinds of resources can be managed in it?</a>

At this time, the shared DAMS is open only to digital content owned and/or stewarded by the UC Libraries. The initial use cases for the software have focused on unique materials held and digitized by the UC Libraries, although there is the potential to provide the service more broadly. Nuxeo supports a wide range of file formats--including images, text documents, audio files, video files, and beyond--and metadata options. Files and metadata may be modeled into both simple and complex objects. <a href="https://registry.cdlib.org/documentation/docs/dams/dams-policies/">Learn more about specific file formats and the metadata scheme that we have implemented...</a>


## Background: How We Got Here
***

### <a name="faq5">5. What was the vision for a systemwide DAMS and where did it come from?</a>
 
The vision for a systemwide DAMS--as well as for the UCLDC platform as a whole--was arrived at through a systemwide planning process over approximately six years and comprising various task forces and committees (<a href="http://libraries.universityofcalifornia.edu/sopag/activities-and-groups">DLSTF1, DLSTF2, NGTS New Modes of Access, and NGTS POT1</a>).

By 2009-2010, broad consensus had emerged that a systemwide solution was needed for the description and management of digital content, with a particular and acute urgency around unique digital content owned and stewarded by the libraries: images, texts, and A/V materials predominantly (but by no means entirely) held by special collections and archives. Without such a solution, several of the libraries had found that they were unable to generate, steward, and provide access to their digital collections on an ongoing basis.
 
This situation was seen as a serious threat not only to the libraries’ ability to independently serve their researchers, but also to the vision of a “UC Libraries Digital Collection”: a coordinated, combined digital collection that would showcase the riches of the libraries to users worldwide, as envisioned in <a href="http://libraries.universityofcalifornia.edu/groups/files/cdc/docs/uc_collection_concept_paper_endorsed_ULs_2009.08.13.pdf">a paper by the UC Libraries Collection Development Committee</a>.

### <a name="faq6">6. How was the UCLDC model determined and why was Nuxeo selected as the shared DAMS?</a>
 
Under NGTS POT1, a number of systemwide “lightning teams” were formed to work on different aspects of the UCLDC vision. Two teams in particular most directly shaped the specific direction of the model and the technologies now being implemented. Those teams were focused on establishing the requirements and the technical model for the UCLDC project.

<ul>
<li><b>Requirements</b>: Lightning Team 1A surveyed staff across the libraries to determine requirements for a systemwide DAMS (as well as for a harvest component and a public access layer).<br><br>

The requirements heavily emphasized functionality necessary for campus libraries to perform management functions as relate to common workflows for digitization and metadata creation. The team did not include advanced technical requirements, such as linked data capabilities, in its report.</li><br>
 
<li><b>Technical Model</b>: Lightning Team 1C, which included technologists from 4 campuses and CDL, put forth a technical model for the UCLDC and recommended a platform for the DAMS. The team based these decisions on an analysis of vetted systems and a comparison of the systems relative to the requirements put forth by LT1A (described above). The team determined that Nuxeo held the greatest possibility for meeting the most requirements on the quickest possible timeline. Thus, they recommended it be implemented “as the first step towards a systemwide digital asset management system strategy.”<br><br>

Meanwhile, mindful of growing interest on the campuses of participating in community development in this space, and particularly around the Fedora framework, the team recommended an additional “long-term strategy of participating in the library-specific Project Hydra and Islandora communities utilizing the Fedora (or Fedora Futures) repository framework.” (<a href="http://libraries.universityofcalifornia.edu/groups/files/POT1_LT1C_finalreport_08Feb2012.pdf">POT1 Lightning Team 1C report, p. 10</a>).</li>


</ul>
 
The Systemwide Operations and Planning Advisory Group (SOPAG) accepted POT1’s summary report, with the exception that it would not endorse Fedora as the long-term solution for the DAMS infrastructure:
	
<ul><i>While the LT1C Final Report introduces the concept of short- and long-term strategies for developing a systemwide DAMS, SOPAG supports only the technical model as presented in Figure 1, p.3 and does not believe that long-term system technologies can be defined at this stage. As with any UC Libraries shared service initiative, after the service has moved from the implementation stage and into the operational stage, an operations team will be charged with the responsibility to monitor technology developments and provide recommendations for service enhancements. We trust that following this established process for operations and continual improvement will meet the service and technical needs of the future UC Libraries Digital Collection.</i></ul>

The University Librarians subsequently charged CDL to implement the UCLDC, now under the auspices of SAG2. CDL followed the recommendations of the lightning teams/SOPAG in its implementation project.

### <a name="faq7">7. How long did it take to implement the DAMS and make it available to the Libraries?</a>

CDL opened the DAMS to campus libraries in July 2014, after approximately ten months of implementation work. This was about a year ahead of POT1’s timeline, with the aim of getting campus users in “on the ground” and enabling them to test, provide feedback, and begin to transition over the remaining months of the implementation period. Campus users at that point could log into Nuxeo using Shibboleth, upload files, build simple and complex objects using the custom metadata model, and batch edit metadata. Since then we have continued to develop toward additional requirements (both existing and uncovered), for example by adding a bulk file import client.

The soft launch of the Calisphere beta site in July 2015 (which will be open only to UC Libraries stakeholders for advanced review and testing) is right on track with POT1’s timeline and will signify the successful implementation of the full “pipeline” and goals of the project: the implementation of the DAMS, the harvest from various campus systems, the development of a robust public interface, and the distribution of all metadata to the Digital Public Library of America (a service  not originally in scope but folded into the project upon recognition of the overlap in required infrastructure). Full public access will be available with the release of the Calisphere beta site approximately 4-8 weeks later, in time for the new school year.

Only three major requirements will not be met on the two-year timeline: controlled vocabularies in the DAMS; support for “on-the-fly” creation of topical collections on Calisphere; and restricted access to content through Calisphere. Prioritization was necessary given the short timeline for the multi-layered project, and, in consultation with campus partners, these three requirements were deemed lower priorities for launch. Now that the pipeline is in place, we could work on implementing these and other more advanced features that the Libraries need and want.
 

## Current Implementation
***

### <a name="faq8">8. What does Nuxeo offer the UC Libraries right now (September 2015)?</a>

The CDL implementation of Nuxeo currently meets a majority of the requirements defined by the POT1 lightning team, for example:

* login and authentication through Shibboleth
* support for complex objects
* batch edit, bulk import, and other critical functionality for library workflows
* a flexible metadata model, allowing for a custom schema(s) if necessary
* accommodation of all file types and unlimited storage on Amazon’s S3 cloud service
 
Note that these and other requirements are specific to library needs and workflows (and, indeed, to UC library needs and workflows). Despite the fact that Nuxeo is a generic DAMS product, it has been easily customized to support and meet the unique needs of UC library users.
 
For a detailed account of POT1 requirements and the extent to which they are anticipated to be met by Nuxeo and the UCLDC model at the project’s conclusion (August 2015), please see our <a href="https://wiki.library.ucsf.edu/download/attachments/101285936/2015-03-06_ucldc_requirements.xlsx?api=v2">requirements summary</a>.

### <a name="faq9">9. What does Nuxeo offer in the way of support for the Libraries?</a>

The way that the current service is structured, there are effectively two “layers” of support for libraries using the DAMS: Nuxeo and CDL.

CDL has a support contract and service level agreement ("Silver level") with Nuxeo, which provides us with ready access to Nuxeo's technical team -- as well as access to the latest hotfixes, service packs, and upgrades to the platform. We have been impressed with the rapid response that we've received from Nuxeo to help us implement and customize the product. As a recent example, the Nuxeo team helped us troubleshoot and enhance the product to support importing of PCD (photo compact disc) format files--as required by UC Irvine--within the span of a few days. Nuxeo has also been responsive to incorporating enhancements that we've requested into their <a href="http://roadmap.nuxeo.com/">development roadmap</a>, such as updates to Studio (an online tool that makes it easy for us to configure and customize the software without expending development resources).  <a href="http://www.nuxeo.com/products/support/#maintenance">Read more about our service level agreement...</a>

Nuxeo’s open-source code base, myriad plug-ins, and extension points allow CDL to provide a second layer of support for the Libraries. The software has proven flexible and customizable enough for us to meet the requirements identified by POT1 as well as new needs identified by the UC Libraries. For example, a number of campus libraries expressed a desire for bulk importing large numbers of files into Nuxeo without CDL’s mediation. (Although Nuxeo does latently support bulk upload through the user interface, it is necessarily limited by bandwidth.) Within a matter of weeks, we were able to leverage Nuxeo’s API to rapidly prototype and develop a client application, which campus users could install on their desktops. Campus users have been using the client for the past few months to successfully upload batches of files on a self-serve basis. 

More information about specific UCLDC Shared DAMS functionality is available on our <a href="https://registry.cdlib.org/documentation/docs/dams/index/">user guide</a>.

### <a name="faq10">10. What kind of metadata schemes does Nuxeo support?</a>

Nuxeo's metadata scheme is highly customizable and extensible, and can be modified using the Studio tool rather than requiring developer time. To date, we have configured Nuxeo to support a specific metadata schema (UCLDC), which was developed in consultation with the UCLDC Project Stakeholder Group. The schema adapts Dublin Core-based elements (which in turn have analogs with other standard data structure schemes such as VRA Core, MODS, and MARC). The schema was intentionally designed to account for a broad range of content types and to support discovery and use. So far this schema has proved appropriate and effective for the Libraries’ content, and it accommodates repeating fields, multi-valued fields, complex objects, etc.

If a campus library requires a custom metadata schema, we have the option to modify the UCLDC schema or add additional schemas. For example, over the course of using Nuxeo, we have extended particular metadata fields (e.g., Description) to address needs voiced by campus libraries to have more granular types of descriptive notes in their metadata -- which can then be available for indexing and display. It is also possible to integrate external vocabularies into the schema for ease of cataloging and authority control.

The metadata records in Nuxeo can be obtained in the form of XML; the XML can then be transformed into other outputs (e.g., JSON, Dublin Core XML) using standard transformation tools such as XSLT. Hence, if there is a scenario where a particular output is required by a campus library, the Nuxeo XML output is highly adaptable.

### <a name="faq11">11.  What are the technical components of Nuxeo?</a>

The technology stack utilizes Apache Tomcat with Redis, Postgres, and Elasticsearch components. The core repository utilizes CMIS/Visible Content Store. For file storage, we are utilizing Amazon Web Service's (AWS) Simple Storage Service (S3). S3 is dynamically provisioned, so we can scale to any volume without pre-provisioning capacity.

The software is updated using .jar files. Customizations can be applied using Studio, an online platform that generates .jar configuration files.  

### <a name="faq12">12.  Are the metadata records and files (that are stored in Nuxeo) backed up?</a>

Yes. We are using the <a href="http://aws.amazon.com/">Amazon Web Service (AWS) Simple Storage Service (S3)</a> to store content files and the <a href="http://aws.amazon.com/rds/">AWS Relational Database Service (RDS)</a> to store the backend Nuxeo databases/metadata records. The S3 "Standard Storage" tier that we are utilizing includes secure cross-region replication of files and version services. RDS also includes automated backup, database snapshots, and data recovery services. 

### <a name="faq13">13. Does Nuxeo/the current UCLDC stack support linked data?</a>

Although the metadata managed within Nuxeo is not natively stored in the RDF format, both Nuxeo specifically and the UCLDC stack generally support Linked Open Data use cases. Within Nuxeo, for example, we believe it would be both immediately advantageous and relatively straightforward to integrate linked data controlled vocabularies. The UCLDC scheme in Nuxeo anticipates drawing on name authorities, thesauri, and other controlled vocabularies that are available as linked data, and we could create a “picker” in the user interface to make it easy for library staff to find and add this metadata to their objects.  

The UCLDC harvesting infrastructure, meanwhile -- which harvests and aggregates metadata from Nuxeo as well as other platforms maintained across the UC Libraries -- latently incorporates linked data elements. For example, harvested metadata is normalized and structured based on the Digital Public Library of America's (DPLA) Metadata Application Profile; the harvested metadata is subsequently expressed as JSON-LD and shared with DPLA. The harvested metadata is also being stored in the UCLDC Common Index (Solr), for exposure <a href="https://registry.cdlib.org/documentation/docs/technical-docs/solr-api/">through an API</a> as well as schema.org encodings in the forthcoming Calisphere BETA site.  

We are interested in the potential for linked data and open to exploring with the Libraries additional use cases for incorporating it throughout the UCLDC stack. That said, we believe that linked data opportunities are not dependent on using RDF as a primary data store--.. and that we should focus specifically on the linked data opportunities that promote efficiencies and/or advance access to the Libraries’ collections. 


## Looking Ahead
***

### <a name="faq14">14.  What plans are in place to enhance Nuxeo, to meet any additional or new use cases or requirements?</a>

For requirements that are not anticipated to be met this summer, Nuxeo provides promising solutions (and, indeed, we see some of these requirements explicitly on the product’s roadmap). It is overwhelmingly the case that some requirements were not met this summer simply because they require more systemwide discussion than could be accomplished on the project’s ambitious timeframe. CDL anticipates working with the Libraries to further unpack, prioritize, and add new requirements to this service offering, whether we meet these requirements within Nuxeo or with another product. To view our Nuxeo development work queue, <a href="https://www.pivotaltracker.com/n/projects/935010">see our Pivotal Tracker site.</a>

### <a name="faq15">15. Does the shared DAMS and UCLDC allow for co-development or other collaboration opportunities with the campus libraries?</a>

Nuxeo is a flexible platform with a well-documented API, offering a range of opportunities for co-developing new features and integrations with other systems. As an example, staff from the UC Santa Cruz Libraries and CDL Nuxeo team developed a strategy for integrating data between Omeka and Nuxeo; UC Santa Cruz subsequently created a <a href="https://github.com/UCSCLibrary">plug-in for Omeka</a> that allows users to import content from Nuxeo into Omeka, utilizing the APIs from each platform; the content can then subsequently be published through Omeka, leveraging Omeka to create a tailored or customized view of that content (e.g., as part of an exhibit). 

More broadly, the UCLDC platform also supports a range of opportunities for co-development, leveraging the <a href="https://registry.cdlib.org/documentation/docs/technical-docs/index/">suite of APIs</a> that are available.

We welcome opportunities to work with the UC Libraries to identify and develop other enhancements to Nuxeo and the broader UCLDC platform. For example, we anticipate that Nuxeo could be extended to integrate shared name authority and thesaurus data, potentially using linked open data techniques; this type of functionality could benefit from co-development approaches. If there is a particular area of the platform that you would like to extend, and are interested in collaborating with us on development work, please contact us! 

### <a name="faq16">16. Does CDL plan to charge for use of the Nuxeo DAMS?</a>

CDL does not currently charge the Libraries for use of the Nuxeo DAMS, nor for the storage of metadata and files in Amazon S3. We have no plans to start charging for the service. Only if storage costs became unsustainable for CDL would we consider re-charging for storage only; we would make an assessment in consultation with the Libraries.

Note that we have provided an ingest pipeline to Merritt from the Nuxeo DAMS. Once a given UC Library transfers content from Nuxeo into Merritt, the pass-through storage costs associated with Merritt will be charged to that UC Library. Only a UCLDC Collection Administrator can designate content for transfer using this workflow.

### <a name="faq17">17. Is CDL exploring other options beyond Nuxeo?</a>	

Yes.
 
Given the express statement in the UCLDC planning process of the need for long-term planning around a DAMS solution--and given the rapidly changing nature of technology and the digital library landscape--CDL has been following alternative developments, particularly in the Fedora/Hydra communities, even while we have moved forward on the implementation of the Nuxeo solution as charged by the libraries. Indeed, we have de facto considered it part of our charge to keep an eye on this space and consider its implications for the ongoing development and provisioning of a systemwide DAMS service. (For example, we are currently evaluating the Portland Common Data Model and we participated in the UC San Diego Hydra/Fedora/PCDM camp.)
 
Meanwhile, we have learned many things from implementing and customizing the Nuxeo platform that we believe warrant discussion among the UC Libraries, vis-à-vis a potential pivot to Fedora. For example, one potential strategy to engage in library community development efforts--while maintaining the high level of service enabled by the Nuxeo platform--would be to incorporate other library technologies into the broader UCLDC stack (such as we have done using Loris); “borrow and build” may in fact be an option. We have anticipated a full evaluation given the explicit recommendation voiced by LT1C and SOPAG’s cover letter—and, indeed, believe it is necessary.
 
The timing and move to new technologies should be a systemwide conversation that is respectful of the process, the needs voiced, and the resources required.

### <a name="faq18">18. If CDL and the Libraries decide to move to another platform for the shared DAMS, is there a strategy for migrating content out of Nuxeo to the new solution?</a>

Nuxeo supports batch exporting of metadata, with references to associated content files in Amazon S3, through its administrative user interface as well as <a href="https://registry.cdlib.org/documentation/docs/technical-docs/nuxeo-api/">through its API</a>. Hence, we have flexible options for migrating content from Nuxeo to another platform.
