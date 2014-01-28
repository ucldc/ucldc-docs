******************************************************************************
Appendix B. Rights Management Administrative Metadata Guidelines (Detailed)
******************************************************************************

==================
Copyright Status
==================

**Definition:** Indicates general type of copyright status for the resource. 

**Recommended data values:** If using Dublin Core or MODS, enter one of the following data values: enter “Public domain” if in the public domain, “Copyrighted” if copyrighted, or “Unknown” of copyright status is unknown. 

If using METSRights: enter “PUBLIC DOMAIN” if in the public domain, or “COPYRIGHTED” if copyrighted . If the copyright status is unknown, enter “OTHER” and add the following additional attribute: OTHERCATEGORYTYPE=“UNKNOWN”. Note that all attributes and attribute values must be in upper case when using the METSRights schema.

**Crosswalks:**

* **METSRights:**
    * <rts:RightsDeclarationMD RIGHTSCATEGORY=“ ”> 
    * <rts:RightsDeclarationMD RIGHTSCATEGORY=“OTHER” OTHERCATEGORYTYPE=“UNKNOWN”> 
* **PREMIS**
    * <pre:rightsBasis>
    * <pre:copyrightInformation> 
        <pre:copyrightStatus>
        <pre:copyrightJurisdiction>
        <pre:copyrightStatusDeterminationDate>
* **Dublin Core:**
    * <dc:rights> 
* **MODS:**
    * <mods:accessCondition type=“useAndReproduction”>

============================
Copyright Statement
============================

**Definition:** A free-text note that describes copyright restrictions pertaining to the resource. 

**Recommended data values:** Usage of one of the following copyright statements is recommended, based on the data value assigned in **Copyright Status:**

* When the status is “unknown”: 
    Some materials in these collections may be protected by the U.S. Copyright Law (Title 17, U.S.C.). In addition, the reproduction, and/or commercial use, of some materials may be restricted by gift or purchase agreements, donor restrictions, privacy and publicity rights, licensing agreement(s), and/or trademark rights. Distribution or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. To the extent other restrictions apply, permission for distribution or reproduction from the applicable rights holder is also required. Responsibility for obtaining permissions, and for any use rests exclusively with the user.
* When the status is “public domain”:
    Material in the public domain. No restrictions on use. 
* When the status is “copyrighted”:
    Transmission or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user. 

**Crosswalks:**

* **METSRights:**
    * <rts:Context CONTEXTCLASS=“GENERAL PUBLIC”> 
        <rts:Constraints> 
            <rts:ConstraintDescription> 
* **PREMIS**
    * <pre:copyrightInformation> 
        <pre:copyrightNote>
* **Dublin Core:**
    * <dc:rights> 
* **MODS:**
    * <mods:accessCondition type=“useAndReproduction”>

=======================
Copyright Date 
=======================

**Definition:** The year the resource was copyrighted. Use only if **Copyright Status** is “Copyrighted”.

**Recommended data values:** Supply the year the resource was copyrighted, typically based on a copyright notice on the resource itself. The resource does not have to have been registered with the copyright office. Do not approximate copyright year if it does not appear on the work, or in some reliable alternate source for this information. Use the standardized form of YYYY, and do not include month or day information.

**Crosswalks:**

* **METSRights:**
    * <rts:RightsDeclarationMD RIGHTSCATEGORY=“COPYRIGHTED”>
        <rts:RightsDeclaration> 
* **PREMIS**
    * <pre:copyrightInformation> 
        <pre:copyrightNote>
* **Dublin Core:**
    * <dcterms:dateCopyrighted> 
* **MODS:**
    * <mods:originInfo>
        <mods:copyrightDate encoding=“temper | w3cdtf” qualifier=“ ”> 

========================
Copyright Owner Name
========================

**Definition:** The name(s) of the copyright holders of the resource. Use only if **Copyright Status** is “Copyrighted”.

**Recommended data values:** Specify the most common form of the name in natural or direct order.

**Crosswalks:**

* **METSRights:**
    * <rts:RightsHolder> 
        <rts:RightsHolderName> 
* **PREMIS**
    * <pre:copyrightInformation> 
        <pre:copyrightNote>
* **Dublin Core:**
    * <dc:rightsHolder> 
* **MODS:**
    * <mods:accessCondition type=“useAndReproduction”>

=====================================
Copyright Owner Contact Information
=====================================

**Definition:** Publicly accessible contact information for the copyright owner(s) of the resource. Use only if **Copyright Status** is “Copyrighted”.

**Recommended data values:** Provide as much contact information as possible that can be made available to the public. Otherwise, use the phrase “Consult contributing institution” or a similar note.

**Crosswalks:**

* **METSRights:**
    * <rts:RightsHolder> 
        <rts:RightsHolderContact> 
            <rts:RightsHolderContactAddress> 
* **PREMIS**
    * <pre:copyrightInformation> 
        <pre:copyrightNote>
* **Dublin Core:**
    * <dc:rightsHolder> 
* **MODS:**
    * <mods:accessCondition type=“useAndReproduction”>

