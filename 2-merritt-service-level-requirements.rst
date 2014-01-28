***************************************
2. Merritt Service Level Requirements
***************************************

===================
2.1 Merritt
===================

The Merritt Digital Repository is a new service from the University of California Curation Center (UC3), which replaces the Digital Preservation Repository (DPR).  Merritt offers a great deal more flexibility and functionality than available in the DPR, while still providing the same high level of digital preservation.  Institutions can provide public access to their content in Merritt, if they wish.  You also be able to deposit collections in Merritt, and make them available through OAC/Calisphere or eScholarship.  More information on Merritt can be found at the `UC3 website <http://www.cdlib.org/services/uc3/merritt/>`_.

===================
2.2 Metadata
===================

2.2.1 Descriptive Metadata
----------------------------

Descriptive metadata is not required, but we strongly encourage you supply the following Dublin Core-based kernel metadata:

+-----------------------------------------------------------------------------------------------+
| *[NOTE: See the* `Merritt and Metadata Guide <http://merritt.cdlib.org/help/metadata_guide>`_ |
| *for more information on descriptive metadata recommendations]*                               |
+===============================================================================================+
| Who (Creator)                                                                                 |
+-----------------------------------------------------------------------------------------------+
| What (Title)                                                                                  |
+-----------------------------------------------------------------------------------------------+
| When (Date)                                                                                   |
+-----------------------------------------------------------------------------------------------+
| Where (Identifier)                                                                            |
+-----------------------------------------------------------------------------------------------+

Descriptive metadata in other encoding formats may be submitted, such as MARC, MIX or MODS records.  These metadata will receive the same level of digital preservation as the digital content.  At the moment, additional metadata will not be searchable in Merritt.

We derive the following metadata during the Merritt ingest process, and can identify and provide access to digital objects submitted with no descriptive metadata.  Only the most basic and fundamental of Merritt services will be available for such objects:

* Object ID
* Date Ingested

2.2.2 Technical Metadata
----------------------------

We derive technical metadata required to support the orderly management of digital objects in Merritt, based on submitted content files.  Currently, the CDL utilizes the `JSTOR/Harvard Object Validation Environment (JHOVE) <http://hul.harvard.edu/jhove/>`_ tool to derive technical metadata for accepted content file types. We plan to move to `JHOVE2 <http://www.jhove2.org/>`_ when it is released.

You may submit any additional technical metadata associated with a particular digital object (such as checksum [MD2, MD5, SHA-1, SHA-256, SHA-384, SHA-512, or CRC-32] and byte size values but are not required to do so.  We will store any supplied additional technical metadata with the object. 

===================
2.3 Content Files
===================

The file formats used to create or store content is a primary factor in their future viability. Formats more likely to be accessible in the future are:

* Non-proprietary
* Open, documented standard
* In common usage by research community
* Use standard character encoding (ASCII, UTF-8)
* Unencrypted
* Uncompressed

Examples of preferred format choices:

* Images: JPEG, JPG-2000, PNG, TIFF
* Texts: HTML, XML, PDF/A, UTF-8, ASCII
* Audio: AIFF, WAVE
* Containers: GZIP, ZIP

See the `UC3 Data Management Guidelines <http://www.cdlib.org/services/uc3/datamanagement/organizing.html>`_ for more recommendations on file formats, file naming, and other data management recommendations.