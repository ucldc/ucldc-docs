*********************************************
3. OAC/Calisphere Service Level Requirements
*********************************************

=========
3.1 METS
=========

**METS Profiles**

Digital objects supported in OAC/Calisphere are managed using the METS format (Metadata Encoding and Transmission Standard).

We depend upon “METS profiles” to successfully process submitted objects.  METS profiles describe classes of METS digital objects that share common characteristics, such as content file formats (e.g., digital images, TEI texts) or metadata encoding formats (e.g., MODS or Dublin Core). Profiles should include enough details to enable METS creators and programmers to create and process METS-encoded digital objects conforming with a particular profile. A METS profile itself is an XML document that must adhere to the METS XML Profile Schema. For information about METS profiles, see the `METS website <http://www.loc.gov/standards/mets/>`_. 

METS files must conform to valid METS profiles, which must be declared during pre-submission discussions with us.  The METS top-level <mets> element must have a PROFILE attribute that contains a URI or other identifier for the METS profile.

**Metadata and Encoding Transmission Standard <METS> Element**

The METS top-level <mets> element must have an OBJID attribute containing an ARK identifier for the digital object (see bolded example). For more information about ARKs, visit the `Archival Resource Key (ARK) <https://confluence.ucop.edu/display/Curation/ARK>`_ page. 

*Example:*

.. raw:: html

    <pre>&lt;mets:mets xmlns:mets=&quot;http://www.loc.gov/METS/&quot;
        xmlns:mods=&quot;http://www.loc.gov/mods/v3&quot;
        xmlns:mix=&quot;http://www.loc.gov/mix/&quot;
        xmlns:rts=&quot;http://cosimo.stanford.edu/sdr/metsrights/&quot;
        xmlns:xlink=&quot;http://www.w3.org/TR/xlink&quot;
        xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;
        xsi:schemaLocation=&quot;http://www.loc.gov/METS/
            http://www.loc.gov/standards/mets/mets.xsd 
            http://www.loc.gov/mods/v3 
            http://www.loc.gov/standards/mods/v3/mods-3-0.xsd 
            http://www.loc.gov/mix/ 
            http://www.loc.gov/standards/mix/mix.xsd 
            http://cosimo.stanford.edu/sdr/metsrights/ 
            http://cosimo.stanford.edu/sdr/metsrights.xsd" 
        OBJID=&quot;<b>ark:/13030/kt9g50158w</b>&quot;
        TYPE=&quot;still image&quot;
        LABEL=&quot;[Pablo de la Guerra (1833-1874), son of Jos&eacute; de la Guerra y Noriega]&quot;
        PROFILE=&quot;http://www.loc.gov/mets/profiles/00000001.xml&quot;&gt;</pre>

**Content File Section <fileSec> Element**

The METS Content File Section <fileSec> element must contain links to network-exposed (i.e., online) content files using File Location <FLocat> elements (see bolded example). Each <FLocat> element must contain a XLINK:HREF attribute that identifies a link to its associated content file.

*Example:*

.. raw:: html

    <pre>&lt;mets:file ID=&quot;FID8&quot; MIMETYPE=&quot;image/jpeg&quot; SEQ=&quot;2&quot;
        CREATED=&quot;1999-06-28T00:00:00&quot; ADMID=&quot;ADM1A&quot; GROUPID=&quot;GID2&quot;&gt;
        &lt;mets:FLocat
            xlink:href=&quot;<b>http://sunsite.berkeley.edu/moa2/images/bkm00002774a_c.jpg</b>&quot;
            LOCTYPE=&quot;URL&quot; /&gt;
    &lt;/mets:file&gt;</pre>

The METS file and associated content files must be well formed and uncorrupted.

**File <file> Element and Checksum Values**

To support the orderly transmission and ingest of digital objects, we recommend including checksum (MD5, SHA-1, or CRC32) and byte size values in the METS File <file> element.

**File <file> Element MIMETYPE Attribute**

Digital objects must explicitly state content file format MIME types (Multipurpose Internet Mail Extensions) for each <file> File Element tag in the METS document (see bolded example).

*Example:*

.. raw:: html

    <pre>&lt;mets:file ID=&ldquo;FID1&rdquo; MIMETYPE=&ldquo;<b>image/tiff</b>&rdquo; SEQ=&ldquo;1&rdquo;
        CREATED=&ldquo;1999-06-17T00:00:00&rdquo; ADMID=&ldquo;ADM1A&rdquo; GROUPID=&ldquo;GID1&rdquo;&gt;</pre>

For a list of MIME type content type and subtype values, see the `MIME Media Types <http://www.iana.org/assignments/media-types/>`_ from the Internet Assigned Numbers Authority.

**Institution/Repository Information: Specialized Use of the <mdRef> Metadata Reference Element**

We recommend the use of a <mdRef> element with a MDTYPE attribute set to "other" and a OTHERMDTYPE attribute set to "contributing-institution-code".  Additionally, use a XLINK:HREF attribute to reference the normalized version of the MARC Organization Code for the contributing institution. The code should be listed at the end of the following URI string: "http://id.loc.gov/organizations/" (see bolded example).

*Example:*

.. raw:: html

    <pre>&lt;mets:dmdSec&gt;
        &lt;mets:mdRef LOCTYPE=&quot;URL&quot; MDTYPE=&quot;<b>other</b>&quot;
            OTHERMDTYPE=&quot;<b>contributing-institution-code</b>&quot;
            xlink:href=&quot;<b>http://id.loc.gov/organizations/cub</b>&quot; /&gt;
    &lt;/mets:dmdSec&gt;</pre>

**Linking from Digital Objects to Collection Descriptions: Specialized Use of the <mdRef> Metadata Reference Element**

For guidelines on linking digital objects to associated, parent-level collection descriptions (represented either in the form of a MARC record or an EAD finding aid), see `Appendix C <>`_.

==================
3.2 Metadata
==================

3.2.1 Using Metadata Schemas
----------------------------

The metadata mappings provided in this section are for extant XML extension metadata schemas such as MODS and qualified Dublin Core. 

Encode metadata consistently based on the specific usage guidelines established for the schema.  For example, if encoding in Dublin Core, follow the Dublin Core usage guidelines for each element.

Do not include HTML markup within metadata encoding, in cases where a metadata schema does not support it.

**Granularity**

Whenever possible, provide the most granular and richest metadata possible.  For example, MODS provides more granular encoding options than simple or q	ualified Dublin Core.  If encoding in Dublin Core, we encourage you to utilize qualified Dublin Core.

**Repeatability of Elements and Data Values**

Elements may be used repeatedly. Note that it may be necessary to supply multiple elements for the same piece of information, e.g., a general form of the date of creation of a resource (“January 1, 1999”) in addition to an ISO8601 normalized form of that date (“1999-01-01”).

However, avoid combining different kinds of data values or repeating the same type of data values within a single element; use separate elements for each data value. For example, avoid encoding multiple subject terms (“Municipal government; City Council members”) in a single element. Instead, encode the two different terms within their own elements.

**Character Encoding**

Use UTF-8 or UTF-16 standard character sets or encodings. We recommend using standardized forms of names for character sets, as documented by the `Internet Assigned Numbers Authority <http://www.iana.org/assignments/character-sets>`_ (e.g., use “UTF-8” and not “UTF8”).

If using the UTF-8 character set in particular, encode directly in Unicode or use Unicode decimal or hexadecimal character references. All decimal character references should begin with an ampersand and pound sign, and end with a semicolon (use the syntax “&#D;” where D is a decimal number). All hexadecimal character references should begin with an ampersand, pound sign, and lower- or uppercase “x”, and end with a semicolon (use the syntax “&#xH;” or “&#XH;” where H is a hexadecimal number); see the Unicode `Code Charts <http://www.unicode.org/charts/>`_ for hexadecimal character reference codes. 

For more detailed information about UTF-8 Unicode, see the W3C/Unicode Consortium document `Unicode in XML and other Markup Languages <http://www.w3.org/TR/unicode-xml/>`_. 

    *Example using UTF-8 Unicode hexadecimal character references to encode the letter “é” in the term “émigrés”:*

    ``... The papers also document trends in high school and university education among Russian &#x00E9;migr&#x00E9;s...``

Characters reserved for XML markup delimiters (ampersand, left angle bracket, and right angle bracket) need to be replaced with the character entities in the following table.

.. csv-table:: Reserved Characters
   :header: "Character", "Character Name", "Character Entity"
   
   "&", "Ampersand", "&amp;"
   "<", "Left angle bracket", "&lt;"
   ">", "Right angle bracket", "&gt;"
   "‘", "Single quote", "&apos;"
   "“", "Double quote", "&quot;"

**Headings, Labels, Punctuation, and Formatting**

Do not include line breaks, list formatting or other any formatting controls within the body of elements. Headings and labels should not appear within the body of elements (except for certain cases; see **Section 3.2.3**). 

Some XML extension schemas (e.g., MODS) provide label attributes on particular elements. In these cases, institutions may encode data values (e.g., text comprising concise headings or descriptions) within those label attributes as permitted by those schemas.

Note that the CDL GDO supports the creation of digital objects that are largely independent of a particular online presentation. The encoding can be manipulated and repurposed through the application of customized style sheets to meet custom display needs and formatting preferences. This includes the special formatting of text, the ordering and positioning of text, the addition of headings and labels, and punctuation. 

In order to provide a consistent user experience, our OAC/Calisphere display stylesheets support a standard presentation that may not accommodate local preferences. 

3.2.2 Descriptive Metadata
----------------------------

**Object Description**

Descriptive metadata can be used to describe different expressions of a given resource. In the case of analog objects that have been digitized, the descriptive metadata may apply to the source analog object or the digital surrogate. For example, the “creator” of a resource may apply to an illustrator of a graphic book or the name of the technician responsible for scanning an image from that book. Likewise, the “date of creation” of a resource may apply to the date of printing for a graphic book or the date of scanning an image from that book. In the case of born-digital objects, the descriptive metadata pertains to the born-digital object itself.

Some descriptive metadata schemas do not allow encoders to clearly disambiguate between uses of a given element to apply to source analog objects versus digital surrogates. Therefore, when creating descriptive metadata for an analog object that has been digitized, we suggest that you consider the following two points:

* Be consistent in your use of descriptive metadata elements: emphasize the description of *either* the source analog object *or* the digital surrogate. 
* Provide descriptive metadata that supports user access to and discovery of the digital object. Information about the source analog object may be more relevant to users. 

.. raw:: html

    <table border="1" class="docutils">
        <caption>Descriptive Metadata Guidelines (Summary) <br><br> [NOTE: See <a href="#id7"><span class="problematic" id="id8">`Appendix A &lt;&gt;`_</span></a> for detailed descriptions of each element. Element names below are also linked to those descriptions]</caption>
        <colgroup><col width="35%" /><col width="65%" /></colgroup>
        <thead valign="bottom">
            <tr class="row-odd">
                <th class="head">Element</th>
                <th class="head">Status</th>
            </tr>
        </thead>
        <tbody valign="top">
            <tr class="row-even"><td style="color: blue">Identifier</td><td style="color: red">Required element</td></tr>
            <tr class="row-odd"><td style="color: blue">Title</td><td style="color: red">Required element</td></tr>
            <tr class="row-even"><td style="color: blue">Creator</td><td><span style="color: red">Required element</span> (NOTE: if no name can be supplied, provide a name in Contributor, Institute/Repository, and/or Publisher)</td></tr>
            <tr class="row-odd"><td style="color: blue">Date</td><td style="color: red">Required element</td></tr>
            <tr class="row-even"><td style="color: blue">Description</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-odd"><td style="color: blue">Language</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-even"><td style="color: blue">Subject (Name)</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-odd"><td style="color: blue">Subject (Title)</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-even"><td style="color: blue">Subject (Place)</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-odd"><td style="color: blue">Subject (Topic, Function, or Occupation)</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-even"><td style="color: blue">Genre</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-odd"><td style="color: blue">Type</td><td style="color: red">Required element</td></tr>
            <tr class="row-even"><td style="color: blue">Format/Physical Description</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-odd"><td style="color: blue">Related Collection/Project</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-even"><td style="color: blue">Institution/Repository</td><td style="color: red">Required element</td></tr>
            <tr class="row-odd"><td style="color: blue">Contributor</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-even"><td style="color: blue">Publisher</td><td style="color: blue">Recommended element</td></tr>
        </tbody>
    </table>

3.2.3. Rights Management Administrative Metadata
--------------------------------------------------

We strongly recommend including rights metadata whenever possible, using one of the following methods: 

* Supply rights information using `METSRights <http://www.loc.gov/standards/rights/METSRights.xsd>`_ or `PREMIS <http://www.loc.gov/standards/premis/>`_, two approved extension schema for METS. 
* Use rights-related elements in the schema chosen for supplying descriptive metadata (e.g., <dc:rights> in Dublin Core, <accessCondition> in MODS).  Elements in these schemas are repeatable, so if more than one rights-related element is used, provide clarifying information about each piece of rights information -- for example, use a label attribute for MODS rights elements. 

.. raw:: html

    <table border="1" class="docutils">
        <caption>Rights Management Administrative Metadata Guidelines <br> (Summary) <br><br>[NOTE: See Appendix B for detailed descriptions of each element. Element names below are also linked to those descriptions]</caption>
        <colgroup><col width="50%" /><col width="50%" /></colgroup>
        <thead valign="bottom">
            <tr class="row-odd">
                <th class="head">Element</th>
                <th class="head">Status</th>
            </tr>
        </thead>
        <tbody valign="top">
            <tr class="row-even"><td style="color: blue">Copyright Status</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-odd"><td style="color: blue">Copyright Statement</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-even"><td style="color: blue">Copyright Date</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-odd"><td style="color: blue">Copyright Owner Name</td><td style="color: blue">Recommended element</td></tr>
            <tr class="row-even"><td style="color: blue">Copyright Owner Contact Information</td><td style="color: blue">Recommended element</td></tr>
        </tbody>
    </table>

3.2.4. Structural Metadata
----------------------------

Structural metadata must be encoded in the METS format: structural metadata is represented in the <structMap> Structural Map section of a METS document. This section defines a structure that allows users of the digital object to navigate through its hierarchical organization. Guidelines for preparing Structural Maps are documented in CDL-supported METS profiles.

3.2.5. Technical Metadata
---------------------------

We derive technical metadata required to support the orderly management of digital objects in Merritt, based on the content files submitted to Merritt.  Currently, the CDL utilizes the `JSTOR/Harvard Object Validation Environment (JHOVE) <http://hul.harvard.edu/jhove/>`_ tool to derive technical metadata for accepted content file types. We plan to move to `JHOVE2 <http://www.jhove2.org/>`_ when it is released.

You may submit any additional technical metadata associated with a particular digital object (such as checksum [MD2, MD5, SHA-1, SHA-256, SHA-384, SHA-512, or CRC-32 ] and byte size values but are not required to do so.  We will store any supplied additional technical metadata with the object. 

Note that all supplied technical metadata should be encoded using valid XML extension schemas as specified by CDL-supported METS profiles (such as in the `NISO Metadata for Images in XML Schema (MIX) <http://www.loc.gov/standards/mix/>`_ format). If a given set of metadata does not conform to a valid XML extension schema, then you should create a schema to embed the metadata and facilitate validation of the METS file. Otherwise, the metadata should be stored independently of the METS file and referred to using the METS <mdRef> Metadata Reference from within the METS file.

3.2.6. Other Metadata (Digital Provenance Administrative Metadata, Source Administrative Metadata, and Behaviors Metadata)
---------------------------------------------------------------------------------------------------------------------------------------

You may submit any additional metadata associated with a particular digital object, but are not required to do so. We will store any supplied additional technical metadata with the object, but may not display the metadata in the OAC/Calisphere interfaces. 

Note that all supplied metadata should be encoded using valid XML extension schemas as specified by CDL-supported METS profiles.  If a given set of metadata does not conform to a valid XML extension schema, then you should create a schema to embed the metadata and facilitate validation of the METS file. Otherwise, the metadata should be stored independently of the METS file and referred to using the METS <mdRef> Metadata Reference from within the METS file.

==================
3.3 Content Files
==================

The following content file types are currently supported in OAC/Calisphere. Consult the appropriate guidelines for preparing these content file types:

STILL NEED TO DUPLICATE THIS TABLE

Each content file should have a file name that is unique to your institution (i.e., not necessarily globally unique); often the unique identifier is used to name the content file itself.
