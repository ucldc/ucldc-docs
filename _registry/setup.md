---
title: Supported Harvest Sources and Formats
next_section: registry/start
prev_section: registry/index
---

##Data sources
We can harvest metadata from a range of sources. Here are the four general types of sources from which we are currently harvesting:

- UC campus libraries' DAMS/repository systems
- UC campus libraries' content published on other platforms and websites
- The [UCLDC Shared DAMS]({{ site.url }}{{ site.baseurl }}/docs/dams/index/)
- The OAC/Calisphere METS repository

Note that even for content in the Shared DAMS, metadata is harvested into the Common Index; the harvest is the mechanism for providing access to all content, regardless of where it is hosted--at CDL or elsewhere.

We will work with content owners to define metadata mappings and the harvesting approach for each specific source/collection target, as described below and elsewhere in this guide.

Please [contact us](mailto: ucldc@ucop.edu) if you have a new data source from which you would like us to harvest a collection(s).

##Harvest protocols
We are using the term "harvest" loosely to apply to a range of approaches to bringing metadata into the Common Index. Examples include:

- Using the OAI-PMH protocol to harvest metadata from CONTENTdm
- Using an API to access a Solr index underlying a library's discovery system 
- Obtaining a metadata export, such as in the MARCXML format.

In general, our objective is to obtain from your system whatever output is easiest for you. We will work with you to determine your preferred method. In the future, we plan to investigate other standardized methods of harvesting that make it even easier to send and sync data, for example using the ResourceSync protocol. 

##Digital object types
We are currently able to harvest metadata for digital objects that generally meet the following criteria:

- The object must have associated digital file(s). "Metadata only" records are not currently supported by the UCLDC platform.
- The object must be hosted in a system that provides for the display of metadata and allows for viewing, downloading, and/or streaming (depending on the format) of digital files.
- The files and metadata must be openly and publicly available. Currently, objects with restricted access are not supported by the UCLDC platform (but this is a future goal).

<div class="note"><p>A “digital object” is a content file(s) and affiliated metadata record(s) that represent an individual resource (e.g., a digitized or born-digital item).  Digital objects may be part of a broader collection.</p></div>

##Metadata formats
There are no restrictions on metadata formats that can be harvested.  However, the metadata must be mappable to a set of standardized data elements, which have been based on the DPLA Metadata Application Profile. A small number of data elements must also be present in each record that is harvested, to suppor use and discovery of the objects. These mappings and requirements are defined in the [Metadata Harvesting Scheme and Crosswalk]({{ site.url }}{{ site.baseurl }}/docs/registry/metadata-harvest/). For more information, see [Harvest and Access Policies]({{ site.url }}{{ site.baseurl }}/docs/registry/access-policies/).
