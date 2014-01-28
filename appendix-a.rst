******************************************************************************
Appendix A. Descriptive Metadata Guidelines (Detailed)
******************************************************************************

The following conventions are used to express guidelines for each metadata element:

* **Definition:** A definition of the element. 
* **Recommended data values:** Recommended data values for the element. May include references to appropriate content standard, authority file, thesaurus, encoding standard, etc. to guide data value entry. 
* **Crosswalks:** The crosswalks provide encoding analogs between elements in Dublin Core and MODS, two schemas for descriptive metadata that are commonly used with METS. 
* **Examples:** Provides examples of preferred data values within elements. 

===========
Identifier
===========

**Definition:** A unique identifier for the resource.

**Recommended data values:** Identify the resource by means of a unique string or number conforming to a formal or locally-derived identification system. Example formal identification systems include:

* Uniform Resource Identifier (URI), including the Uniform Resource Locator (URL) 
* Digital Object Identifier (DOI) 
* International Standard Book Number (ISBN) 

The METS top-level <mets> element must have an OBJID attribute containing an ARK identifier for the digital object. For more information, see **Section 3.1**. 

**Crosswalks:**

* **Dublin Core**: 
    * <dc:identifier> 
* **MODS:**
    * <mods:identifier type=““> 
    * < mods:location>
        < mods:url> 
* **METS:**
    * <mets:mets OBJID=""> 

**Examples:**

| *calb_p3353 [Note: locally-derived unique identifier]*
| *0609609718 [Note: ISBN]*

===========
Title
===========

**Definition:** A succinct, identifying name for the resource. 

**Recommended data values:** Transcribe the formal title of the resource or supply a title, if necessary, using an appropriate content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_, or `Graphic Materials (GIHC) <http://www.loc.gov/rr/print/gm/graphmat.html>`_.

**Crosswalks:**

* **Dublin Core:**
    * <dc:title> 
* **MODS:**
    * <mods:titleInfo>
        <mods:title> 
    * <mods:titleInfo>
        <mods:title>
            <mods:subtitle>

**Examples:**

.. raw:: html

    <div class="line"><u>Formal titles</u></div>
    <div class="line">Two dancers on a stage / Frasher Foto <i>[Note: transcribed according to AACR2]</i></div>
    <div class="line">The Rocky Mountains, emigrants crossing the plains [graphic] / F.F. Palmer, del. <i>[Note: transcribed according to Graphic Materials]</i></div>
    <br/>
    <div class="line"><u>Supplied titles</u></div>
    <div class="line">[Photograph of musicians performing at a cultural program] <i>[Note: derived according to AACR2]</i></div>
    <div class="line">Mitchell Bonner photograph of musicians performing at a cultural program <i>[Note: derived according to DACS]</i></div>
    <div class="line">[Phoenix] / Ben Shahn <i>[Note: derived according to Graphic Materials]</i></div>

===========
Creator
===========

**Definition:** The name of the person, institution, agent, or group primarily responsible for the creation of the resource.

**Recommended data values:** The form of the name should be taken from a standard naming authority file, such as the `Library of Congress Name Authority File (LCNAF) <http://authorities.loc.gov/>`_ or `Union List of Artists’ Names (ULAN) <http://www.getty.edu/research/conducting_research/vocabularies/ulan/>`_. If a name does not appear in an authority file, establish the name according to a content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, or `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_.

Additionally, if possible, indicate the code for a standard naming authority file from which the name is taken. Use “lcnaf” for the LCNAF or “ulan” for ULAN. For all others, use the appropriate code for the source (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_). 

If the name is not found in a standard naming authority file, indicate the content standard by which the name is established, e.g., “aacr” for AACR2, “dacs” for DACS, and “gihc” for Graphic Materials (GIHC) (see the Library of Congress’ `Descriptive Conventions Code List <http://www.loc.gov/marc/relators/reladesc.html>`_). If a content standard is not used, use “local”.

**Crosswalks:**

* **Dublin Core:**
    * <dc:creator> 
* **MODS:**
    * <mods:name type=“personal | corporate | conference” authority=““>
        <mods:namePart> 
    * <mods:name type=“personal | corporate | conference” authority=““>
        <mods:namePart>
            <mods:role>
                <mods:roleTerm type=“text”> 

**Examples:**

.. raw:: html

    <div class="line"><u>Personal name entry</u></div>
    <div class="line">Yamada, Mitsuye <i>[Note: determined from local cataloging authority or LCNAF]</i></div>
    <div class="line">Chase, Alexander W. (Alexander Wells), 1843-1888 <i>[Note: derived according to AACR2]</i></div>
    <div class="line">White, Ira Johnson <i>[Note: determined from ULAN]</i></div>
    <div class="line">Robinson family <i>[Note: derived according to DACS]</i></div>
    <br/>
    <div class="line"><u>Corporate name entry</u></div>
    <div class="line">American Philosophical Society <i>[Note: determined from local cataloging authority or LCNAF]</i></div>
    <div class="line">Frasher Foto (Firm) <i>[Note: derived according to AACR2]</i></div>

=========
Date
=========

**Definition:** A single date or inclusive dates indicating when the resource was created.

**Recommended data values:** Construct dates using an appropriate content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_, or `Graphic Materials (GIHC) <http://www.loc.gov/rr/print/gm/graphmat.html>`_.

At least one form of the date should be normalized (note that the Date element is repeatable) using one of the following standards: 

* `Temporal Enumerated Ranges (TEMPER) <http://www.cdlib.org/inside/diglib/ark/temperspec.pdf>`_ standard. TEMPER is a simple date and time syntax for representing points, lists, and ranges of time stamps. The syntax is designed to be machine-parseable and human-reader-friendly, and to support simple lexical sorting algorithms. TEMPER consists of four-, eight-, and 14-digit points, point ranges, and lists of points and ranges. 
* `International Standard Organization (ISO) 8601 <http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=40874&ICS1=1&ICS2=140&ICS3=30>`_ standard, using a modified version of the `W3C date and time formats profile <http://www.w3.org/TR/NOTE-datetime>`_. 

**Crosswalks:**

* **Dublin Core:**
    * <dc:date> 
    * <dcterms:created> 
* **MODS:**
    * <mods:originInfo>
        <mods:dateCreated encoding=“temper | w3cdtf” qualifier=““>  *[Note: do not use <dateCaptured> when describing date of creation for a born-digital resource]*
    * <mods:originInfo>
        <mods:dateOther encoding=“temper | w3cdtf” qualifier=““> 
    * <mods:publicationInfo>
        <mods:dateIssued encoding=“temper | w3cdtf” qualifier=““> 

**Examples:**

.. raw:: html

    <u>TEMPER encoding</u><br><br>
    <b><i>Single dates</i></b>

| 1901 = 1901
| January 1901 = 19010100
| 1901 January 3 = 19010103 

.. raw:: html

    <b><i>Date spans</i></b>

| 1900-1950 = 1900-1950
| 1956 January-July = 19560100-19560700
| 1980s = 1980-1989 *[Note: use an interval to indicate every year of the decade]*
| 19th century = 1801-1900 

.. raw:: html

    <b><i>Broken date spans</i></b>

| 1924, 1956-1975 = 1924, 1956-1975 *[Note: separate by a comma]*

.. raw:: html

    <b><i>Open date spans</i></b>

| 1911- = 1911-
| -1911 = -1911

.. raw:: html

    <b><i>Approximate dates</i></b>

| circa 1950 = 1950~ 

.. raw:: html

    <b><i>Undated material</i></b>

undated: circa mid 20th century = 1935~-1965~ *[Note: if a resource is undated this can be stated but provide an estimate if possible; normalize as an interval, perhaps using the dates of the life of creator, etc.]*

.. raw:: html

    <u>International Standard Organization (ISO) 8601 encoding (using a modified version of the W3C date and time formats profile)</u><br><br>
    <b><i>Single dates</i></b>

| 1901 = 1901
| January 1901 = 1901-01
| 1901 January 3 = 1901-01-03 

.. raw:: html

    <b><i>Date spans</i></b>

| 1900-1950 = 1900/1950
| 1956 January-July = 1956-01/1956-07
| 1980s = 1980/1989 *[Note: use an interval to indicate every year of the decade]*
| 19th century = 1801/1900 

.. raw:: html

    <b><i>Broken date spans</i></b>

| 1924, 1956-1975 = 1924, 1956/1975 *[Note: separate by a comma]*

.. raw:: html

    <b><i>Open date spans</i></b>

| 1911- = 1911/9999 *[Note: use an interval and set the end date to 9999]*

.. raw:: html

    <b><i>Approximate dates</i></b>

| circa 1950 = 1945/1955 *[Note: normalize as an interval to express an appropriate date range]*

.. raw:: html

    <b><i>Undated material</i></b>

| undated: circa mid 20th century = 1935/1965 *[Note: if a resource is undated this can be stated but provide an estimate if possible; normalize as an interval, perhaps using the dates of the life of creator, etc.]*

====================
Description
====================

**Definition:** A brief free-text note, abstract, table of contents listing, or descriptive statement that characterizes more fully than the title does the scope or content of the resource.

**Recommended data values:** Use when the intellectual content of the item is not sufficiently captured in the title and other descriptors. Construct a note using an appropriate content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_, or `Graphic Materials (GIHC) <http://www.loc.gov/rr/print/gm/graphmat.html>`_.

**Crosswalks:**

* **Dublin Core:**
    * <dc:description> 
    * <dcterms:abstract> 
* **MODS:**
    * <mods:abstract> 
    * <mods:tableOfContents> 
    * <mods:note> 
    * <mods:note type=““> *[Note: use for scope and content notes that are equivalent to MARC 520 element]*

**Examples:**

Depicts unknown automobile driver stopping at roadside to add water to engine on all-day drive from Chico to Sacramento. Exact location unknown. Verso stamped with 596; manuscript note indicates car owned by “N.E.R.” *[Note: derived according to AACR2]*

View of the Alaskan King Ice Cream Parlor, with horse-drawn delivery wagon in foreground and City Hall in background, Eugene, OR. *[Note: derived according to DACS]*

Signed in red ink. Edition of 59; Library has 14/59. *[Note: derived according to Graphic Materials]*

==================
Language
==================

**Definition:** Term that indicates the language that is an integral part of the resource, such as a caption that is part of a photograph or a title that is part of a painting.

**Recommended data values:** At least one form of the language term should be normalized in coded form using a three-letter code from the from the `International Organization for Standardization (ISO) 639-2 Codes for the Representation of Names of Languages <http://www.loc.gov/standards/iso639-2/>`_ (note that the Language element is repeatable, for representing the language term in textual form).

**Crosswalks:**

* **Dublin Core:**
    * <dc:language> 
* **MODS:**
    * <mods:languageTerm authority=“iso639-2b” type=“code”> 

**Examples:**

| eng *[Note: use for English]*
| vie *[Note: use for Vietnamese]*
| ger *[Note: use for German]*

=====================
Subject (Name)
=====================

**Definition:** Significant names (personal, corporate, family, meeting, etc.) represented in or by the resource.

**Recommended data values:** The form of the name should be taken from a standard naming authority file, such as the `Library of Congress Name Authority File (LCNAF) <http://authorities.loc.gov/>`_ or `Union List of Artists’ Names (ULAN) <http://www.getty.edu/research/conducting_research/vocabularies/ulan/>`_. If a name does not appear in an authority file, establish the name according to a content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, or `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_.

Additionally, if possible, indicate the code for a standard naming authority file from which the name is taken. Use “lcnaf” for the LCNAF or “ulan” for ULAN. For all others, use the appropriate code for the source (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_). 

If the name is not found in a standard naming authority file, indicate the content standard by which the name is established, e.g., “aacr” for AACR2, “dacs” for DACS, and “gihc” for Graphic Materials (GIHC) (see the Library of Congress’ `Descriptive Conventions Code List <http://www.loc.gov/marc/relators/reladesc.html>`_). If a content standard is not used, use “local”.

**Crosswalks:**

* **Dublin Core:**
    * <dc:subject> 
* **MODS:**
    * <mods:subject authority=““>
        <mods:titleInfo authority=““>
            <mods:title> 

**Examples:**

Kim Hà, 1950-. Qua con bao du : hoi ky vuot bien bang duong bo. *[Note: manuscript material documenting creation of a monograph titled “Qua con bao du”; entry derived according to AACR2]*

=====================
Subject (Place)
=====================

**Definition:** Significant names of geographic locations represented in or by the resource.

**Recommended data values:** The form of the name should be taken from a standard naming authority file, such as the `Library of Congress Name Authority File (LCNAF) <http://authorities.loc.gov/>`_ or `Thesaurus of Geographic Names (TGN) <http://www.getty.edu/research/conducting_research/vocabularies/tgn/>`_. If a name does not appear in an authority file, establish the name according to a content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_ or `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_.

Additionally, if possible, indicate the code for a standard naming authority file from which the name is taken. Use “lcnaf” for the LCNAF or “ulan” for ULAN. For all others, use the appropriate code for the source (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_). 

If the name is not found in a standard naming authority file, indicate the content standard by which the name is established, e.g., “aacr” for AACR2, “dacs” for DACS, and “gihc” for Graphic Materials (GIHC) (see the Library of Congress’ `Descriptive Conventions Code List <http://www.loc.gov/marc/relators/reladesc.html>`_). If a content standard is not used, use “local”.

**Crosswalks:**

* **Dublin Core:**
    * <dc:coverage> 
    * <dcterms:spatial> 
* **MODS:**
    * <mods:subject authority=““>
        <mods:geographic> 
    * <mods:subject authority=““>
        <mods:hierarchicalGeographic> 
    * <mods:subject authority=““>
        <mods:cartographics> 

**Examples:**

| Santa Cruz (Calif.) *[Note: determined from local cataloging authority or LCNAF]*
| Santa Cruz *[Note: determined from TGN]*
| Rancho Boca de la Playa (Calif.) *[Note: established according to AACR2]*

================================================
Subject (Topic, Function, or Occupation)
================================================

**Definition:** Significant topics or subjects (including concepts, events, etc.), functions, or occupations represented in or by the resource.

**Recommended data values:** The form of the heading should be taken from a standard or local thesaurus, such as the `Library of Congress Subject Headings (LCSH) <http://authorities.loc.gov/>`_, `Art and Architecture Thesaurus (AAT) <http://www.getty.edu/research/conducting_research/vocabularies/aat/>`_, or `Thesaurus of Graphic Materials I (TGM I) <http://www.loc.gov/rr/print/tgm1/>`_.

If a heading does not appear in a thesaurus, establish the heading according to standard thesaurus rules (such as the Library of Congress’ *Subject Cataloging Manual*, AAT rules, or TGM I rules), or local thesaurus rules.

Additionally, if possible, indicate the code for a standard naming authority file from which the heading is taken. Use “lcsh” for LCSH, “aat” for AAT, or “gmgpc” for TGM I (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_).

If the heading does not appear in a standard thesaurus, indicate the thesaurus rules by which the term is established, e.g., “lcsh” for LCSH, “aat” for AAT, or “gmgpc” for TGM I (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_). If standard thesaurus rules are not used, use “local”.

**Crosswalks:**

* **Dublin Core:**
    * <dc:subject> 
* **MODS:**
    * <mods:subject authority=““>
        <mods:topic> 
    * <mods:subject authority=““>
        <mods:occupation> 

**Examples:**

| Viticulture -- California -- Sonoma County *[Note: determined from LCSH]*
| Surveyors--California--Orange County *[Note: determined from LCSH]*
| Street railroads *[Note: determined from AAT]*
| Agricultural laborers--Italian Americans--California--Salinas *[Note: determined from TGM I]*

===========
Genre
===========

**Definition:** Primary genre(s) represented in or by the resource.

**Recommended data values:** The form of the heading should be taken from a standard or local thesaurus, such as the `Library of Congress Subject Headings (LCSH) <http://authorities.loc.gov/>`_, `Art and Architecture Thesaurus (AAT) <http://www.getty.edu/research/conducting_research/vocabularies/aat/>`_, `Genre Terms (RBGENR) <http://library.osu.edu/sites/users/russell.363/RBMS Thesauri/genre/alphabetical_list.htm>`_, or `Thesaurus of Graphic Materials II (TGM II) <http://www.loc.gov/rr/print/tgm2/>`_.

If a heading does not appear in a thesaurus, establish the heading according to standard thesaurus rules (such as the Library of Congress’ *Subject Cataloging Manual*, AAT rules, or TGM II rules), or local thesaurus rules.

Additionally, if possible, indicate the code for a standard naming authority file from which the heading is taken. Use “lcsh” for LCSH, “aat” for AAT, or “gmgpc” for TGM II (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_).

If the heading does not appear in a standard thesaurus, indicate the thesaurus rules by which the term is established, e.g., “lcsh”, “aat”, or “gmgpc”. Use the appropriate code for the thesaurus by which the term is established (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_). If standard thesaurus rules are not used, use “local”.

**Crosswalks:**

* **Dublin Core:**
    * <dc:type> 
* **MODS:**
    * <mods:genre authority=“ ”>

**Examples:**

| Photographs *[Note: determined from LCSH]*
| Photographic prints *[Note: determined from AAT]*
| Photographic prints *[Note: determined from TGM II]*

========
Type
========

**Definition:** A high-level type data value that generally characterizes the resource represented by the digital object. This high-level data value may also be repeated, or more specific genre data values may also be encoded as part of the descriptive metadata (see **Genre**).

**Recommended data values:** Choose data values from one of the following lists, based on the descriptive metadata scheme being utilized. Select data values from the MODS type vocabulary if in doubt:

* `Dublin Core type vocabulary <http://dublincore.org/documents/dcmi-type-vocabulary/>`_
* `MODS type vocabulary <http://www.loc.gov/standards/mods/v3/mods-userguide-elements.html#typeofresource>`_ (see values listed under <typeOfResource>) 

**Crosswalks:**

* **Dublin Core:**
    * <dc:type> 
* **MODS:**
    * <mods:typeOfResource> 
* **METS:**
    * <mets:mets TYPE=""> 

**Examples:**

| image *[Note: determined from Dublin Core type vocabulary]*
| still image *[Note: determined MODS type vocabulary]*

==============================================
Format/Physical Description
==============================================

**Definition:** The physical or digital manifestation of the resource. Typically, this may include the media-type or dimensions of the resource. Examples of dimensions include size and duration.

**Recommended data values:** Construct a statement using an appropriate content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_, or `Graphic Materials (GIHC) <http://www.loc.gov/rr/print/gm/graphmat.html>`_.

**Crosswalks:**

* **Dublin Core:**
    * <dc:format> 
    * <dcterms:extent>
* **MODS:**
    * <mods:physicalDescription>
        <mods:extent> 
    * <mods:physicalDescription>
        <mods:form> 
    * <mods:physicalDescription>
        <mods:internetMediaType>

**Examples:**

| 1 photographic print ; 9 x 14 cm. *[Note: derived according to AACR2]*
| 14 letters *[Note: derived according to DACS]*
| 1 leaflet : ill. ; 21.5 x 38.5 cm., folded to 21.5 x 10 cm. *[Note: derived according to Graphic Materials]*

===========================
Related Collection/Project
===========================

**Definition:** A machine access-oriented identifier for a collection or project that the resource is a member of or related to in some manner.

**Recommended data values:** If the resource is a member of or related to a collection or project, at least one **Related Collection/Project** element must refer to a unique identifier for the collection or project (e.g., a URL to a webpage, collection guide, or finding aid that describes the collection).  

Alternatively, indicate the title for a collection or project. 

For guidelines on encoding METS-based links from digital objects to associated, parent-level collection descriptions (represented either in the form of a MARC record or an EAD finding aid), see `Appendix C <>`_. Use a METS <mdRef> element with a MDTYPE attribute set to either "MARC" or "EAD". 

**Crosswalks:**

* **Dublin Core:**
    * <dc:relation> 
    * <dcterms:isPartOf> 
* **MODS:**
    * <mods:relatedItem>
        <mods:url> 
    * <mods:relatedItem>
        <mods:identifier> 

**Examples:**

.. raw:: html

    <div class="line"><u>URL for a collection guide (or finding aid) in the Online Archive of California</u></div>
    <div class="line">http://www.oac.cdlib.org/findaid/ark:/13030/kt6199s0j9/</div>
    <br/>
    <div class="line"><u>URL for a collection</u></div>
    <div class="line">http://jarda.cdlib.org</div>
    <div class="line">http://laassubject.org/</div>
    <br/>
    <div class="line"><u>Title</u></div>
    <div class="line">Silicon Valley History Online</div>

==========================
Institution/Repository
==========================

**Definition:** The name of the owning or contributing institution of the resource.

**Recommended data values:** The form of the name should be taken from a standard naming authority file, such as the `Library of Congress Name Authority File (LCNAF) <http://authorities.loc.gov/>`_. If the name does not appear in an authority file, establish the name according to a content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, or `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_.

In order for the CDL to uniquely identify and manage digital objects by contributing institution, the CDL strongly recommends the use of a METS <mdRef> element with a MDTYPE attribute set to "other" and a OTHERMDTYPE attribute set to "contributing-institution-code". Additionally, use a XLINK:HREF attribute to reference the normalized version of the MARC Organization Code for the contributing institution. The code should be listed at the end of the following URI string: "http://id.loc.gov/organizations/". For more information, see **Section 3.1**. 

**Crosswalks:**

* **Dublin Core:**
    * <dc:publisher> 
* **MODS:**
    * <mods:location>
        <mods:physicalLocation authority="">
        <mods:physicalLocation>
    * <mods:note displayLabel="Digital object made available by">
* **METS:**
    * <mets:mdRef LOCTYPE="URL" MDTYPE="other" OTHERMDTYPE="contributing-institution-code" xlink:href="http://id.loc.gov/organizations/" />

**Examples:**

| Fowler Museum of Cultural History *[Note: determined from local cataloging authority or LCNAF]*
| Orange Public Library *[Note: derived according to AACR2]*
| University of California, San Francisco. Library. Archives and Special Collections *[Note: derived according to AACR2]*

=================
Contributor
=================

**Definition:** The name of the person, institution, agent, or group responsible for contributing to the resource in some significant manner, such as a illustrator, designer, autographer, etc.

**Recommended data values:** The form of the name should be taken from a standard naming authority file, such as the `Library of Congress Name Authority File (LCNAF) <http://authorities.loc.gov/>`_ or `Union List of Artists’ Names (ULAN) <http://www.getty.edu/research/conducting_research/vocabularies/ulan/>`_. If a name does not appear in an authority file, establish the name according to a content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, or `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_.

Additionally, if possible, indicate the code for a standard naming authority file from which the name is taken. Use “lcnaf” for the LCNAF or “ulan” for ULAN. For all others, use the appropriate code for the source (see the Library of Congress’ `Term, Name, and Title Sources Code List <http://www.loc.gov/marc/relators/relasour.html>`_). 

If the name is not found in a standard naming authority file, indicate the content standard by which the name is established, e.g., “aacr” for AACR2, “dacs” for DACS, and “gihc” for Graphic Materials (GIHC) (see the Library of Congress’ `Descriptive Conventions Code List <http://www.loc.gov/marc/relators/reladesc.html>`_). If a content standard is not used, use “local”.

**Crosswalks:**

* **Dublin Core:**
    * <dc:contributor> 
* **MODS:**
    * <mods:name type=“personal | corporate | conference” authority=“ ”>
        <mods:namePart>
            <mods:role>
                <mods:roleTerm type=“text”> 

**Examples:**

.. raw:: html

    <div class="line"><u>Personal name entry</u></div>
    <div class="line">Yamada, Mitsuye <i>[Note: determined from local cataloging authority or LCNAF]</i></div>
    <div class="line">Chase, Alexander W. (Alexander Wells), 1843-1888 <i>[Note: derived according to AACR2]</i></div>
    <div class="line">White, Ira Johnson <i>[Note: determined from ULAN]</i></div>
    <div class="line">Robinson family <i>[Note: derived according to DACS]</i></div>
    <br/>
    <div class="line"><u>Corporate name entry</u></div>
    <div class="line">American Philosophical Society <i>[Note: determined from local cataloging authority or LCNAF]</i></div>
    <div class="line">Frasher Foto (Firm) <i>[Note: derived according to AACR2]</i></div>

==================
Publisher
==================

**Definition:** The name of the publisher of a formally published resource. This element may not be relevant for unpublished materials.

**Recommended data values:** The form of the name should be taken from a standard naming authority file, such as the `Library of Congress Name Authority File (LCNAF) <http://authorities.loc.gov/>`_ or `Union List of Artists’ Names (ULAN) <http://www.getty.edu/research/conducting_research/vocabularies/ulan/>`_. If a name does not appear in an authority file, establish the name according to a content standard such as `Anglo-American Cataloging Rules (AACR2) <http://www.aacr2.org/>`_, `Cataloging Cultural Objects (CCO) <http://www.vraweb.org/CCOweb/>`_, or `Describing Archives: a Content Standard (DACS) <http://www.archivists.org/catalog/pubDetail.asp?objectID=1279>`_.

**Crosswalks:**

* **Dublin Core:**
    * <dc:publisher> 
* **MODS:**
    * <mods:originInfo>
        <mods:publisher>

**Examples:**

| Simon & Schuster *[Note: determined from local cataloging authority or LCNAF]*
| New Albion Records *[Note: derived according to AACR2]*
