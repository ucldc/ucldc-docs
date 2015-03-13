***************
1. Introduction
***************

=========
1.1 Scope
=========

The CDL Guidelines for Digital Objects (CDL GDO, this document) provides specifications for digital objects prepared by institutions for submission to CDL for preservation and access, through the CDL’s `Merritt Digital Repository <http://www.cdlib.org/services/uc3/merritt/>`_ and the `Online Archive of California (OAC) <http://www.oac.cdlib.org/>`_ and `Calisphere <http://www.calisphere.universityofcalifornia.edu/>`_ services. The specifications are not intended to cover all of the administrative, operational, and technical issues surrounding the creation of digital object collections. 

The guidelines seek to support the following objectives: 

* Ensure a basic level of uniformity in the structure and encoding of non-licensed digital content managed by the CDL 
* Advance interoperability among digital content from diverse institutions 
* Promote efficient ingest procedures 
* Support the orderly management of digital content 
* Facilitate access to digital content by users 
* Minimize costs 

These guidelines do not set requirements for digital materials submitted to or collected by the CDL through other means:

* Metadata exposed to CDL harvesting systems via the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) 
* Metadata targeted by federated search systems 
* Web-crawled resources 

In addition, these guidelines do not address requirements for collections delivered to the CDL's `eScholarship <http://www.cdlib.org/services/publishing/escholarship.html>`_ or `UC Shared Images <http://www.cdlib.org/services/dsc/ucsi/>`_ programs. Institutions or individuals interested in submitting content to these repositories should consult the projects’ websites.

===================
1.2. Service Levels
===================

Digital materials of ever-increasing variety and complexity are seen to be worth collecting and preserving by memory organizations such as libraries, archives, and museums. Materials include objects converted into digital form from existing collections of manuscripts, maps, visual images, and sound files, as well as born-digital materials such as web sites, videos, and data sets. 

Digital objects hosted by the CDL typically consist of three components: metadata, a set of content files, and a link or binding mechanism to associate the two (such as a METS wrapper).  In order to create coherent and cost-effective services for such diverse collections, the CDL and other digital libraries sometimes require certain common digital object features that offer strategic points of leverage. This is a delicate undertaking, as it tends to involve a reduction in diversity that implies a loss of information, and every imposed requirement incurs the risk of rejecting valuable materials that fail to meet it. Simply meeting requirements is often hard because funding is unavailable or the original producer of the digital objects cannot be reached.  Hence, these specifications provide significant leeway in metadata and content file requirements, particularly for long-term preservation.

The Merritt Digital Repository and Online Archive of California (OAC) and Calisphere services have different technical frameworks and have operated largely independent of each other.  While we are working to integrate our services so that institutions do not have to deposit to them separately (but instead can deposit items once, and have them submitted to multiple services at the same time), the different services currently have different metadata requirements. Merritt does not require METS documents for deposit.  Instead, a much simpler metadata scheme is recommended.  However, Merritt will continue to accept METS wrappers, and in those cases where you wish to submit items to both Merritt and OAC/Calisphere, a METS wrapper will be required. 

The CDL GDO specifies requirements for two primary levels of services:

* **Merritt Service Level**: sufficient for the submission of digital objects to Merritt. There are no metadata requirements for Merritt, but it is recommended that a small descriptive metadata record be included, based upon Dublin Core.
* **OAC/Calisphere Service Level**: required for submission to OAC and Calisphere. It is also sufficient for submission of digital objects to Merritt. This level requires METS wrappers. Particular content file formats are supported at this level. 

===================
1.3. Terminology
===================

For an explanation of general terms used throughout these guidelines, see the `CDL Glossary <http://www.cdlib.org/gateways/technology/glossary.html>`_. For an explanation of concepts and terms pertaining to metadata in particular, consult the `RLG Cultural Materials Descriptive Metadata Guidelines <http://www.rlg.org/en/pdfs/RLG_desc_metadata.pdf>`_. 

======================================
1.4. How to Use These Guidelines
======================================

Consult the appropriate section of the guidelines, based on the level of CDL service that your institution is interested in utilizing:

* **Merritt Service Level:** consult **Section 2** only 
* **OAC/Calisphere Service Level:** consult **Section 3** only