---
layout: registry-doc
title: Supported Harvest Sources and Formats
next_section: registry/start
prev_section: registry/index
permalink: /docs/registry/setup/
breadcrumbs: Calisphere Admin Guide
---

##Data sources
We can harvest metadata from a range of sources. Currently, there are four general types of sources from which we are harvesting into the Common Index:

- UC campus libraries' DAMS/repository systems
- UC campus libraries' content published on other platforms and websites
- The [UCLDC Shared DAMS]({{ site.url }}{{ site.baseurl }}/docs/dams/index/)
- The OAC/Calisphere METS repository

We will work with content owners to define metadata mappings and the harvesting approach for each specific source/collection target, as described below and elsewhere in this guide.

Please [contact us](mailto: ucldc@ucop.edu) if you have a new data source from which you would like us to harvest a collection(s).

##Harvest protocols
We are using the term "harvest" loosely to apply to a range of approaches that we are using to bring metadata into the Common Index.  Examples include:

- Using the OAI-PMH protocol to harvest metadata from CONTENTdm (e.g., UCSC)
- Using an API to access Solr indexes, underlying campus' DAMS (e.g., UCLA, UCSD) 
- Obtaining a metadata export, such as in the MARCXML format (e.g., UCSB)

We have been working with each content owner to determine their preferred method, and anticipate collaborating on utilizing other standardized methods to harvest metadata in the near future (e.g., using the ResourceSync protocol). 

##Content types
We are currently able to harvest metadata for digital objects that generally meet the following criteria:

- The object must be hosted in a system that provides a display of the metadata and associated digital file(s).
- The object must be openly available for public viewing, downloading, and/or streaming (depending on the format), within its native context (i.e., from the harvest source). 
- The object must have associated digital file(s). "Metadata only" records are not currently supported by the UCLDC platform.

Digital objects 

There are no restrictions on file formats or metadata types.  

For more information, see [Harvest and Access Policies]({{ site.url }}{{ site.baseurl }}/docs/registry/access-policies/).

<div class="note"><p>By “digital object”, we mean a content file(s) and affiliated metadata record(s) that represents an individual resource (e.g., a digitized or born-digital item).  Digital objects may be part of a broader collection.</p></div>

