***************************************
4. Revision History
***************************************

This is the second version of the CDL GDO. This version is based upon and supersedes the CDL Digital Object Standard, Version 1.0 (May 2001) and the OAC Best Practice Guidelines for Digital Objects, Version 1.1 (January 2004). These guidelines were prepared by the CDL Digital Object Working Group from the fall of 2004 through the winter of 2005.

The CDL GDO is reviewed and updated semi-annually by UC Curation Center and Digital Special Collections staff.

**June 2007**
    * Modified Sections 2.1 and 3.1. The METS top-level <mets> element must have an OBJID attribute containing an ARK identifier for the digital object.  Additionally, the METS top-level <mets> element must have a PROFILE attribute that contains a URI or other identifier for the METS profile.
**September 2007**
    * Modified subheadings and reorganized content within Sections 2.1 and 3.1: subheadings are now consistently based on METS element names.
    * Added METS File <file> element specifications to Sections 2.1, 2.2.2, 3.1, and 3.2.4: Technical metadata associated with a particular digital object (such as checksum [MD5, SHA-1, or CRC32] and byte size values may be supplied in the METS <file> element, but is not required. 
**April 2009**
    * Included encoding examples in Section 3.1 and Appendix C.
    * Added recommendation in Section 3.1 and :ref:`appendix-a` Appendix A ("Institution/Repository" element) for encoding unique identifiers for contributing institution.  Recommendation specifies use of <mdRef> with a MDTYPE attribute set to "other" and a OTHERMDTYPE attribute set to "contributing-institution-code".
**January 2010**
    * Reformatted document.
    * Added PREMIS rights metadata mappings in Appendix B.
**January 2011**
    * Revised Sections 1.2 and 2 to reflect use of Merritt Digital Repository service.  Changed “Basic” and “Enhanced” service levels terminology to “Merritt” and “OAC/Calisphere” service levels, respectively.
**July 2011**
    * Updated Section 3.3 to reflect supported file formats for OAC/Calisphere.  
**August 2011**
    * Updated Section 3.3 to refer to the CDL Digital File Format Recommendations.