---
layout: dams-doc
title: DAMS Metadata Scheme
permalink: /docs/dams/metadata-model/
breadcrumbs: DAMS Appendix
---

<a href="{{ site.url }}{{ site.baseurl }}/docs/dams/ucldc-schema/">
  <span class="glyphicon glyphicon-file"></span> View the DAMS metadata scheme's xsd file.
</a><br>


##Required Metadata
***

The following data elements must be present in each metadata record for harvest into the UCLDC Common Index. These elements are also denoted using an asterisk in the metadata scheme summary:

* <a class="label">Main Content File</a>
* <a class="label">Title</a>
* <a class="label">Type</a>
* <a class="label">Campus/Unit</a>
* <a class="label">Rights status</a>
* <a class="label">Rights statement</a>


##The Metadata Scheme
***

### Content Files

\* <a class="label" id="MainContentFile">Main Content File</a> - The main resource file. Used to generate display files (main file, thumbnail, etc.) in the index and Calisphere once you "publish" the object.

<a class="label" id="AuxiliaryFiles">Auxiliary Files</a> - Additional resource files including variant formats and derivative copies of the main content file. These files will not be published to the index or Calisphere.

<!-- <div style="position: relative"><span class="badge">New <br/>Field</span></div> -->

<a class="label" id="AuxiliaryFileType">Auxiliary File Type</a> - Qualifier identifying the kind of auxiliary file.


### Basic Information

\* <a class="label" id="Title">Title</a> - A formal or supplied title for the resource.

<div class="example">
  <u>Example:</u>
  <br/>Formal titles
  <br/>The Rocky Mountains, emigrants crossing the plains [graphic] / F.F. Palmer, del. 
  <br/>
  <br/>Supplied titles
  <br/>Mitchell Bonner photograph of musicians performing at a cultural program 
  <br/>[Photograph of musicians performing at a cultural program] 
</div>

<a class="label" id="AlternativeTitle">Alternative Title</a> - Alternative or additional titles for the resource.

<div class="example">
  <u>Example:</u>
  <br/>Formal titles
  <br/>The Rocky Mountains, emigrants crossing the plains [graphic] / F.F. Palmer, del. 
  <br/>
  <br/>Supplied titles
  <br/>Mitchell Bonner photograph of musicians performing at a cultural program 
  <br/>[Photograph of musicians performing at a cultural program]
</div>

<a class="label" id="Identifier">Identifier</a> - A globally unique identifier for the resource.

<div class="example">
  <u>Example:</u>
  <br/>ark.cdlib.org/ark:/13030/kt987021sv/
</div>

<a class="label" id="LocalIdentifier">Local Identifier</a> - A local item or call number for the resource.

<div class="example">
  <u>Example:</u>
  <br/>calb_p3353
  <br/>MSS 0124.144
</div>

\* <a class="label" id="Type">Type</a> - A high-level characterizes of the resource type.

<div class="example">
  <u>Example:</u>
  <br/>image
  <br/>text
  <br/>audio
</div>

\* <a class="label" id="CampusUnit">Campus/Unit</a> - URL reference to the Campus/Unit that is responsible for maintaining and curating the resource.

<div class="example">
  <u>Example:</u>
  <br/>https://registry.cdlib.org/api/v1/repository/4/
</div>

<div class="note">
  The contents of the Campus/Unit field are <em>crucial</em> to how an object will appear in Calisphere. Both campuses and units will have a unique URL assigned to each via the Collection Registry. Populating an object's Campus/Unit field with this URL is how an object will be linked to a campus or unit and displayed appropriately in Calisphere. In subsequent releases, this field will be integrated with the Collection Registry. For now, if you are adding new objects to the DAMS, please consult with <a href="mailto:ucldc@ucop.edu" class="notelink">ucldc@ucop.edu</a> and we can work with you to populate this field.
</div>

<a class="label" id="Date">Date</a> - A single date or inclusive dates indicating when the resource was created.

<div class="example">
  <u>Example:</u>
  <br/>Single dates 
  <br/>1901 = 1901
  <br/>1901 January 3 = 19010103 
  <br/>
  <br/>Date spans 
  <br/>1900-1950 = 1900-1950
  <br/>1956 January-July = 19560100-19560700
  <br/>1980s = 1980-1989 [Note: use an interval to indicate every year of the decade]
  <br/>19th century = 1801-1900 
  <br/>
  <br/>Broken date spans
  <br/>1924, 1956-1975 = 1924, 1956-1975 [Note: separate by a comma]
  <br/>
  <br/>Open date spans 
  <br/>1911- = 1911-
  <br/>-1911 = -1911
  <br/>
  <br/>Approximate dates
  <br/>circa 1950 = 1950~ 
  <br/>undated: circa mid 20th century = 1935~-1965~ [Note: if a resource is undated this can be stated but provide an estimate if possible; normalize as an interval, perhaps using the dates of the life of creator, etc.]
</div>

<a class="label" id="PublicationInformation">Publication Information</a> - Publication statements and/or names of persons, families, or organizations responsible for publishing the resource.

<div class="example">
  <u>Example:</u>
  <br/>Corporate name entry
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
</div>

<a class="label" id="Creator">Creator</a> - Names of persons, families, or organizations primarily responsible for creating the resource.

<div class="example">
  <u>Example:</u>
  <br/>Personal name entry
  <br/>Yamada, Mitsuye 
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>White, Ira Johnson
  <br/>
  <br/>Corporate name entry
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
  <br/>
  <br/>Families
  <br/>Robinson family
</div>

<a class="label" id="Contributor">Contributor</a> - Names of persons, families, or organizations responsible for contributing to the resource in some significant manner.

<div class="example">
  <u>Example:</u>
  <br/>Personal name entry
  <br/>Yamada, Mitsuye 
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>White, Ira Johnson
  <br/>
  <br/>Corporate name entry
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
  <br/>
  <br/>Families
  <br/>Robinson family
</div>


### Content and Characteristics

<a class="label" id="FormatPhysicalDescription">Format/Physical Description</a> - A description of the physical or digital manifestation of the resource. Typically, this may include an indicator of the size and duration.

<div class="example">
  <u>Example:</u>
  <br/>1 photographic print ; 9 x 14 cm. [Note: derived according to AACR2]
  <br/>14 letters [Note: derived according to DACS]
  <br/>1 leaflet : ill. ; 21.5 x 38.5 cm., folded to 21.5 x 10 cm. [Note: derived according to Graphic Materials]
</div>

<a class="label" id="Description">Description</a> - Descriptive statements that characterize more fully the scope or content of the resource.

<div class="example">
  <u>Example:</u>
  <br/>Depicts unknown automobile driver stopping at roadside to add water to engine on all-day drive from Chico to Sacramento. Exact location unknown. Verso stamped with 596; manuscript note indicates car owned by “N.E.R.”
</div>

<a class="label" id="DescriptionType">Description Type</a> - Qualifier identifying the kind of description

<a class="label" id="Extent">Extent</a> - A more specific statement of the size or duration of the resource (if not specified in Format/Physical Description)

<div class="example">
  <u>Example:</u>
  <br/>9 x 14 cm.
  <br/>21.5 x 38.5 cm., folded to 21.5 x 10 cm.
</div>

<a class="label" id="Language">Language</a> - Languages significantly represented in or by the resource

<div class="example">
  <u>Example:</u>
  <br/>eng [Note: use for English]
  <br/>vie [Note: use for Vietnamese]
  <br/>ger [Note: use for German]
</div>

<a class="label" id="TemporalCoverage">Temporal Coverage</a> - Temporal characteristics of the resource

<div class="example">
  <u>Example:</u>
  <br/>Surveyed 4/1/1931
</div>

<a class="label" id="Transcription">Transcription</a> - A transcription of textual information, for resources that are text-based or document formats

<div class="example">
  <u>Example:</u>
  <br/>Martinez California December 31, 1893. My dear Sister Mary, I wish you a happy New Year, You and all yours. Heaven bless you all. Ever affectionately Your brother John Muir.
</div>


### Conditions of Access and Use

<a class="label" id="AccessRestrictions">Access Restrictions</a> - Specifies level of access, for viewing resource in the UCLDC discovery/delivery system

<div class="example">
  <u>Example:</u>
  <br/>public
  <br/>UC systemwide
  <br/>UC campus only
</div>

\* <a class="label" id="CopyrightStatus">Copyright Status</a> - A coded designation for the copyright status of the resource, at the time the rights statement is recorded.

<div class="example">
  <u>Example:</u>
<br/>unknown
<br/>public domain
<br/>copyrighted
</div>

\* <a class="label" id="CopyrightStatement">Copyright Statement</a> - Statement summarizing the copyright status of the resource 

<div class="example">
  <u>Example (status "unknown"):</u>
  <br/>Some materials in these collections may be protected by the U.S. Copyright Law (Title 17, U.S.C.). In addition, the reproduction, and/or commercial use, of some materials may be restricted by gift or purchase agreements, donor restrictions, privacy and publicity rights, licensing agreement(s), and/or trademark rights. Distribution or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. To the extent other restrictions apply, permission for distribution or reproduction from the applicable rights holder is also required. Responsibility for obtaining permissions, and for any use rests exclusively with the user.
  <br/>
  <br/> <u>Example (status "public domain"):</u>
  <br/>Material in the public domain. No restrictions on use.
  <br/>
  <br/><u>Example (status "copyrighted"):</u>
  <br/>Transmission or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user
</div>

<a class="label" id="CopyrightHolder">Copyright Holder</a> - Names of persons, families, or organizations holding copyright to the resource

<div class="example">
  <u>Example:</u>
  <br/>Personal name entry
  <br/>Yamada, Mitsuye 
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>White, Ira Johnson
  <br/>
  <br/>Corporate name entry
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
  <br/>
  <br/>Families
  <br/>Robinson family 
</div>

<a class="label" id="CopyrightContact">Copyright Contact</a> - Information on who to contact, to clear copyright permissions

<div class="example">
  <u>Example:</u>
  <br/>Consult Special Collections and Archives
</div>

<a class="label" id="CopyrightNotice">Copyright Notice</a> - Transcription of any formal copyright notice on the work

<div class="example">
  <u>Example:</u>
  <br/>Copyrighted 1967
</div>

<a class="label" id="CopyrightDeterminationDate">Copyright Determination Date</a> - The date that the copyright status recorded in Copyright Status was determined.

<div class="example">
  <u>Example:</u>
  <br/>4/12/12
</div>

<a class="label" id="CopyrightStartDate">Copyright Start Date</a> - The start date for which the copyright applies or is applied to the resource

<div class="example">
  <u>Example:</u>
  <br/>1/1/32
</div>

<a class="label" id="CopyrightEndDate">Copyright End Date</a> - The end date for which the copyright applies or is applied to the resource

<div class="example">
  <u>Example:</u>
  <br/>12/31/54
</div>

<a class="label" id="CopyrightJurisdiction">Copyright Jurisdiction</a> - The country whose copyright laws apply.

<div class="example">
  <u>Example:</u>
  <br/>us
</div>

<a class="label" id="CopyrightNote">Copyright Note</a> - Additional information about the copyright status of the resource

<div class="example">
  <u>Example:</u>
  <br/>Rights transferred to UC Regents by Dane Jo in 1980.
</div>


### Related Materials

<a class="label" id="Collection">Collection</a> - URL reference to associated collections

<div class="example">
  <u>Example:</u>
  <br/>https://registry.cdlib.org/api/v1/collection/10/
</div>

<div class="note">
  The contents of the Collection field are <em>crucial</em> to how an object will appear in Calisphere. You will be able to define collections in the Collection Registry, which will assign each collection a unique URL. Populating an object's Collection field with this URL is how an object will be linked to a collection and displayed appropriately in Calisphere. In subsequent releases, this field will be integrated with the Collection Registry. For now, if you are adding new objects to the DAMS, please consult with <a href="mailto:ucldc@ucop.edu" class="notelink">ucldc@ucop.edu</a> and we can work with you to populate this field.
</div>

<a class="label" id="RelatedResource">Related Resource</a> - Reference to other related resources (by theme, topic, collection, etc.)

<div class="example">
  <u>Example:</u>
  <br/>Series 1: Personal and Business Correspondence
</div>

<a class="label" id="Source">Source</a> - Reference to a resource from which the present resource is derived.

<div class="example">
  <u>Example:</u>
  <br/>Selected photograph from page 12 of the Lawrence & Houseworth Photography Album (Item Number #MS R01 042).
</div>


### Access Points

<a class="label" id="SubjectName">Subject (Name)</a> - Personal, corporate, or family names significantly represented in or by the resource.

<div class="example">
  <u>Example:</u>
  <br/>Personal name entry
  <br/>Yamada, Mitsuye 
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>White, Ira Johnson
  <br/>
  <br/>Corporate name entry
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
  <br/>
  <br/>Families
  <br/>Robinson family 
</div>

<a class="label" id="SubjectTopicFunctionOccupation)">Subject (Topic, Function, Occupation)</a> - Topics or subjects (including concepts, events, etc.), functions, or occupations significantly represented in or by the resource.

<div class="example">
  <u>Example:</u>
  <br/>Viticulture
  <br/>Surveyors
  <br/>Street railroads
  <br/>Agricultural laborers--Italian Americans
</div>

<a class="label" id="Place">Place</a> - Names of geographic locations significantly represented in or by the resource.

<div class="example">
  <u>Example:</u>
  <br/>San Mateo (county); California; United States
  <br/>(-121Â° 35' 30"", 36Â° 47' 30"") (-122Â° 25' 00"", 37Â° 37' 00"")
</div>

<a class="label" id="FormGenre">Form/Genre</a> - Forms or genres of materials significantly represented in or by the resource.

<div class="example">
  <u>Example:</u>
  <br/>Photographs
  <br/>Aerial photographs
  <br/>Tintypes
</div>


### Administrative Information

<a class="label" id="Provenance">Provenance</a> - Indicator of ownership and/or custody of the resource since its creation that are significant for its authenticity, integrity and interpretation. 

<div class="example">
  <u>Example:</u>
  <br/>Donated by Harold Grimm, 2004
</div>

<a class="label" id="PhysicalLocation">Physical Location</a> - Reference to the location of the resource

<div class="example">
  <u>Example:</u>
  <br/>Map Case 1, Drawer 3
</div>


### Content Files

<table class="confluenceTable">
    <tbody>
        <tr>
            <th class="confluenceTh">
                Field Label
            </th>
            <th class="confluenceTh">
                Required (Calisphere)?
            </th>
            <th class="confluenceTh">
		Summary
            </th>
        </tr>

        <tr>
            <td class="confluenceTd">
                <a class="label" id="MainContentFile">Main Content File</a>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
            <td class="confluenceTd">
                The main resource file. Used to generate display files (main file, thumbnail, etc.) in the index and Calisphere once you “publish” the object.
            </td>
        </tr>
  
          <tr>
            <td class="confluenceTd">
                <a class="label" id="AuxiliaryFiles">Auxiliary Files</a>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Additional resource files including variant formats and derivative copies of the main content file. These files will not be published to the index or Calisphere.
            </td>
        </tr>
		
		        <tr>
            <td class="confluenceTd">
                <a class="label" id="AuxiliaryFileType">Auxiliary File Type</a>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Qualifier identifying the kind of auxiliary file.
            </td>
        </tr>
    </tbody>
</table>


### Basic Information

<table class="confluenceTable">
    <tbody>
        <tr>
            <th class="confluenceTh">
                Field Label
            </th>
            <th class="confluenceTh">
                Subfield Label
            </th>
            <th class="confluenceTh">
                Required (Calisphere)?
            </th>
            <th class="confluenceTh">
		Summary
            </th>
            <th class="confluenceTh">
		Examples
            </th>
            <th class="confluenceTh">
                Vocabularies
            </th>
            <th class="confluenceTh">
                Repeatable?
            </th>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Title">Title</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A formal or supplied title for the resource.
            </td>
            <td class="confluenceTd">
                <u>Formal titles</u>
                <br/>
                The Rocky Mountains, emigrants crossing the plains [graphic] / F.F. Palmer, del.
                <br/>
                <br/>
                <u>Supplied titles</u>
                <br/>
                Mitchell Bonner photograph of musicians performing at a cultural program
                <br/>
                [Photograph of musicians performing at a cultural program]
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="AlternativeTitle">Alternative Title</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Alternative or additional titles for the resource.
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Identifier">Identifier</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                An ARK identifier for the resource
            </td>
            <td class="confluenceTd">
                ark.cdlib.org/ark:/13030/kt987021sv/
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="LocalIdentifier">Local Identifier</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A local item or call number for the resource.
            </td>
            <td class="confluenceTd">
                MSS 0124.144
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Type">Type</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A high-level characterizes of the resource type.
            </td>
            <td class="confluenceTd">
                Image
            </td>
            <td class="confluenceTd">
                Audio
                <br/>
                Dataset
                <br/>
                Image
                <br/>
                Software
                <br/>
                Text
                <br/>
                Video
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CampusUnit">Campus/Unit</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                URL reference to the Campus/Unit that is responsible for maintaining and curating the resource. The contents of the Campus/Unit field are <em>crucial</em> to how an object will appear in Calisphere. Both campuses and units will have a unique URL assigned to each via the Collection Registry. Populating an object's Campus/Unit field with this URL is how an object will be linked to a campus or unit and displayed appropriately in Calisphere. In subsequent releases, this field will be integrated with the Collection Registry. For now, if you are adding new objects to the DAMS, please consult with <a href="mailto:ucldc@ucop.edu" class="notelink">ucldc@ucop.edu</a> and we can work with you to populate this field.
            </td>
            <td class="confluenceTd">
                <a href="https://registry.cdlib.org/api/v1/repository/4/">https://registry.cdlib.org/api/v1/repository/4/ </a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Date">Date</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Date
            </td>
            <td class="confluenceTd">
                Date
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A single date or inclusive dates indicating when the resource was created.
            </td>
            <td class="confluenceTd">
  <u>Example:</u>
  <br/>Single dates 
  <br/>1901 = 1901
  <br/>1901 January 3 = 19010103 
  <br/>
  <br/>Date spans 
  <br/>1900-1950 = 1900-1950
  <br/>1956 January-July = 19560100-19560700
  <br/>1980s = 1980-1989 [Note: use an interval to indicate every year of the decade]
  <br/>19th century = 1801-1900 
  <br/>
  <br/>Broken date spans
  <br/>1924, 1956-1975 = 1924, 1956-1975 [Note: separate by a comma]
  <br/>
  <br/>Open date spans 
  <br/>1911- = 1911-
  <br/>-1911 = -1911
  <br/>
  <br/>Approximate dates
  <br/>circa 1950 = 1950~ 
  <br/>undated: circa mid 20th century = 1935~-1965~ [Note: if a resource is undated this can be stated but provide an estimate if possible; normalize as an interval, perhaps using the dates of the life of creator, etc.]
			
			
			
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Date
            </td>
            <td class="confluenceTd">
                Date Type
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Use to qualify date, for unpublished (created) vs. published (issued) materials
            </td>
            <td class="confluenceTd">
                Created
				<br/>
            </td>
            <td class="confluenceTd">
                Created
                <br/>
                Issued
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Date
            </td>
            <td class="confluenceTd">
                Single
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                ISO-8601 normalized single date
            </td>
            <td class="confluenceTd">
                1979-05-14<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Date
            </td>
            <td class="confluenceTd">
                Inclusive Start
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                ISO-8601 normalized start date (for date ranges)
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Date
            </td>
            <td class="confluenceTd">
                Inclusive End
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                ISO-8601 normalized end date (for date ranges)
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="PublicationInformation">Publication Information</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Publication statements and/or names of persons, families, or organizations responsible for publishing the resource.
            </td>
            <td class="confluenceTd">
                  American Philosophical Society 
				  <br/>
 				  Frasher Foto (Firm) 
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Creator">Creator</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Creator
            </td>
            <td class="confluenceTd">
                Name
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Names of persons, families, or organizations primarily responsible for creating the resource.
            </td>
            <td class="confluenceTd">
                  <u>Personal name entry</u>
  <br/>Yamada, Mitsuye 
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>White, Ira Johnson
  <br/>
  <br/>
  <u>Corporate name entry</u>
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
  <br/>
   <br/>
  <u>Families</u>
  <br/>Robinson family
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Creator
            </td>
            <td class="confluenceTd">
                Name Type
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the identity type
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Creator
            </td>
            <td class="confluenceTd">
                Role
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the role of the identity
            </td>
            <td class="confluenceTd">
                Photographer<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Creator
            </td>
            <td class="confluenceTd">
                Source
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify if the name heading was taken from one of these authority files
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Creator
            </td>
            <td class="confluenceTd">
                Authority ID
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Contributor">Contributor</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Contributor
            </td>
            <td class="confluenceTd">
                Name
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Names of persons, families, or organizations responsible for contributing to the resource in some significant manner.
            </td>
            <td class="confluenceTd">
                  <u>Personal name entry</u>
  <br/>Yamada, Mitsuye 
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>White, Ira Johnson
  <br/>
  <br/>
  <u>Corporate name entry</u>
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
  <br/>
   <br/>
  <u>Families</u>
  <br/>Robinson family
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Contributor
            </td>
            <td class="confluenceTd">
                Name Type
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the identity type
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Contributor
            </td>
            <td class="confluenceTd">
                Role
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the role of the identity
            </td>
            <td class="confluenceTd">
                Editor<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Contributor
            </td>
            <td class="confluenceTd">
                Source
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify if the name heading was taken from one of these authority files
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Contributor
            </td>
            <td class="confluenceTd">
                Authority ID
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
    </tbody>
</table>

### Content and Characteristics

<table class="confluenceTable">
    <tbody>
        <tr>
            <th class="confluenceTh">
                Field Label
            </th>
            <th class="confluenceTh">
                Subfield Label
            </th>
            <th class="confluenceTh">
                Required (Calisphere)?
            </th>
            <th class="confluenceTh">
		Summary
            </th>
            <th class="confluenceTh">
		Examples
            </th>
            <th class="confluenceTh">
                Vocabularies
            </th>
            <th class="confluenceTh">
                Repeatable?
            </th>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="FormatPhysicalDescription">Format/Physical Description</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A description of the physical or digital manifestation of the resource. Typically, this may include an indicator of the size and duration.
            </td>
            <td class="confluenceTd">
                1 photographic print
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Description">Description</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Description
            </td>
            <td class="confluenceTd">
                (Note)
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Descriptive statements that characterize more fully the scope or content of the resource.
            </td>
            <td class="confluenceTd">
                Depicts unknown automobile driver stopping at roadside to add water to engine on all-day drive from Chico to Sacramento. Exact location unknown. Verso stamped with 596; manuscript note indicates car owned by “N.E.R.”<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr height="360">
            <td height="360">
                <a class="label" id="DescriptionType">Description Type</a>
            </td>
            <td class="confluenceTd">
                Type
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Indicate the description type
            </td>
            <td class="confluenceTd">
                Scope/Content<br/>
            </td>
            <td class="confluenceTd">
                Scope/Content
                <br/>
                Acquisition
                <br/>
                Bibliography
                <br/>
                Biography/History
                <br/>
                Citation/Reference
                <br/>
                Conservation History
                <br/>
                Creation/Production Credits
                <br/>
                Date Note
                <br/>
                Exhibitions
                <br/>
                Funding
                <br/>
                Annotations/Markings
                <br/>
                Language
                <br/>
                Performers
                <br/>
                Preferred Citation
                <br/>
                Venue
                <br/>
                Condition
                <br/>
                Medium
                <br/>
                Technique
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Extent">Extent</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A more specific statement of the size or duration of the resource (if not specified in Format/Physical Description)
            </td>
            <td class="confluenceTd">
                9 x 14 cm.
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Language">Language</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Language
            </td>
            <td class="confluenceTd">
                Language
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Languages significantly represented in or by the resource
            </td>
            <td class="confluenceTd">
                English<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Language
            </td>
            <td class="confluenceTd">
                Language Code
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                ISO-632b language code
            </td>
            <td class="confluenceTd">
                eng<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="TemporalCoverage">Temporal Coverage</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Temporal characteristics of the resource
            </td>
            <td class="confluenceTd">
                Surveyed 4/1/1931
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Transcription">Transcription</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A transcription of textual information, for resources that are text-based or document formats
            </td>
            <td class="confluenceTd">
                Martinez California December 31, 1893. My dear Sister Mary, I wish you a happy New Year, You and all yours. Heaven bless you all. Ever affectionately Your brother John Muir.<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
    </tbody>
</table>

### Conditions of Access and Use

<table class="confluenceTable">
    <tbody>
        <tr>
            <th class="confluenceTh">
                Field Label
            </th>
            <th class="confluenceTh">
                Subfield Label
            </th>
            <th class="confluenceTh">
                Required (Calisphere)?
            </th>
            <th class="confluenceTh">
		Summary
            </th>
            <th class="confluenceTh">
		Examples
            </th>
            <th class="confluenceTh">
                Vocabularies
            </th>
            <th class="confluenceTh">
                Repeatable?
            </th>
        </tr>
        <tr>
            <td>
                <a class="label" id="AccessRestrictions">Access Restrictions</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specifies level of access, for viewing resource in the UCLDC discovery/delivery system
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Public
                <br/>
                UC systemwide
                <br/>
                UC campus only
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightStatus">Copyright Status</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                A coded designation for the copyright status of the resource, at the time the rights statement is recorded.
            </td>
            <td class="confluenceTd">
                Copyrighted<br/>
            </td>
            <td class="confluenceTd">
                Copyrighted
                <br/>
                Public domain
                <br/>
                Copyright unknown
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightStatement">Copyright Statement</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Statement summarizing the copyright status of the resource
            </td>
            <td class="confluenceTd">
                 <u>Example (status "unknown"):</u>
  <br/>Some materials in these collections may be protected by the U.S. Copyright Law (Title 17, U.S.C.). In addition, the reproduction, and/or commercial use, of some materials may be restricted by gift or purchase agreements, donor restrictions, privacy and publicity rights, licensing agreement(s), and/or trademark rights. Distribution or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. To the extent other restrictions apply, permission for distribution or reproduction from the applicable rights holder is also required. Responsibility for obtaining permissions, and for any use rests exclusively with the user.
  <br/>
  <br/> <u>Example (status "public domain"):</u>
  <br/>Material in the public domain. No restrictions on use.
  <br/>
  <br/><u>Example (status "copyrighted"):</u>
  <br/>Transmission or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightHolder">Copyright Holder</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Copyright Holder
            </td>
            <td class="confluenceTd">
                Name
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Names of persons, families, or organizations holding copyright to the resource
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Copyright Holder
            </td>
            <td class="confluenceTd">
                Name Type
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the identity type
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Copyright Holder
            </td>
            <td class="confluenceTd">
                Source
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify if the name heading was taken from one of these authority files
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Copyright Holder
            </td>
            <td class="confluenceTd">
                Authority ID
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightContact">Copyright Contact</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Information on who to contact, to clear copyright permissions
            </td>
            <td class="confluenceTd">
                Consult Special Collections and Archives<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightNotice">Copyright Notice</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Transcription of any formal copyright notice on the work
            </td>
            <td class="confluenceTd">
                Copyright 1975<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightDeterminationDate">Copyright Determination Date</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                The date that the copyright status recorded in Copyright Status was determined.
            </td>
            <td class="confluenceTd">
                4/12/12<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightStartDate">Copyright Start Date</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                The start date for which the copyright applies or is applied to the resource
            </td>
            <td class="confluenceTd">
                1/1/32<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightEndDate">Copyright End Date</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                The end date for which the copyright applies or is applied to the resource
            </td>
            <td class="confluenceTd">
                12/31/21<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightJurisdiction">Copyright Jurisdiction</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                The country whose copyright laws apply.
            </td>
            <td class="confluenceTd">
                us<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="CopyrightNote">Copyright Note</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Additional information about the copyright status of the resource
            </td>
            <td class="confluenceTd">
                Rights transferred to UC Regents by Dane Jo in 1980<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
     </tbody>
</table>

### Content and Characteristics


### Related Materials

<table class="confluenceTable">
    <tbody>
        <tr>
            <th class="confluenceTh">
                Field Label
            </th>
            <th class="confluenceTh">
                Subfield Label
            </th>
            <th class="confluenceTh">
                Required (Calisphere)?
            </th>
            <th class="confluenceTh">
		Summary
            </th>
            <th class="confluenceTh">
		Examples
            </th>
            <th class="confluenceTh">
                Vocabularies
            </th>
            <th class="confluenceTh">
                Repeatable?
            </th>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Collection">Collection</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                URL reference to associated collections. The contents of the Collection field are <em>crucial</em> to how an object will appear in Calisphere. You will be able to define collections in the Collection Registry, which will assign each collection a unique URL. Populating an object's Collection field with this URL is how an object will be linked to a collection and displayed appropriately in Calisphere. In subsequent releases, this field will be integrated with the Collection Registry. For now, if you are adding new objects to the DAMS, please consult with <a href="mailto:ucldc@ucop.edu" class="notelink">ucldc@ucop.edu</a> and we can work with you to populate this field.
            </td>
            <td class="confluenceTd">
                https://registry.cdlib.org/api/v1/collection/10/<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="RelatedResource">Related Resource</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Reference to other related resources (by theme, topic, collection, etc.)
            </td>
            <td class="confluenceTd">
                Series 1: Personal and Business Correspondence<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Source">Source</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Reference to a resource from which the present resource is derived.
            </td>
            <td class="confluenceTd">
                Selected photograph from page 12 of the Lawrence & Houseworth Photography Album (Item Number #MS R01 042)<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
		</tbody>
</table>

### Access Points

<table class="confluenceTable">
    <tbody>
        <tr>
            <th class="confluenceTh">
                Field Label
            </th>
            <th class="confluenceTh">
                Subfield Label
            </th>
            <th class="confluenceTh">
                Required (Calisphere)?
            </th>
            <th class="confluenceTh">
		Summary
            </th>
            <th class="confluenceTh">
		Examples
            </th>
            <th class="confluenceTh">
                Vocabularies
            </th>
            <th class="confluenceTh">
                Repeatable?
            </th>
        </tr>

        <tr>
            <td class="confluenceTd">
                <a class="label" id="SubjectName">Subject (Name)</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Subject (Name)
            </td>
            <td class="confluenceTd">
                Name
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Personal, corporate, or family names significantly represented in or by the resource.
            </td>
            <td class="confluenceTd">
                                  <u>Personal name entry</u>
  <br/>Yamada, Mitsuye 
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>White, Ira Johnson
  <br/>
  <br/>
  <u>Corporate name entry</u>
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
  <br/>
   <br/>
  <u>Families</u>
  <br/>Robinson family
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Subject (Name)
            </td>
            <td class="confluenceTd">
                Name Type
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the identity type
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Subject (Name)
            </td>
            <td class="confluenceTd">
                Role
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the role of the identity
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Subject (Name)
            </td>
            <td class="confluenceTd">
                Source
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify if the name heading was taken from one of these authority files
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Subject (Name)
            </td>
            <td class="confluenceTd">
                Authority ID
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="Place">Place</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Place
            </td>
            <td class="confluenceTd">
                Name
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Names of geographic locations significantly represented in or by the resource.
            </td>
            <td class="confluenceTd">
                San Mateo (county); California; United States<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Place
            </td>
            <td class="confluenceTd">
                Coordinates
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Geographic coordinates
            </td>
            <td class="confluenceTd">
                (-121Â° 35' 30"", 36Â° 47' 30"") (-122Â° 25' 00"", 37Â° 37' 00"")<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr height="100">
            <td height="100">
                Place
            </td>
            <td class="confluenceTd">
                Source
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify if the name heading was taken from one of these authority files
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                LCSH
                <br/>
                TGN
                <br/>
                Geonames
                <br/>
                Local
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Place
            </td>
            <td class="confluenceTd">
                Authority ID
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="SubjectTopicFunctionOccupation)">Subject (Topic, Function, Occupation)</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Subject
            </td>
            <td class="confluenceTd">
                Heading
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Topics or subjects (including concepts, events, etc.), functions, or occupations significantly represented in or by the resource.
            </td>
            <td class="confluenceTd">
                  <br/>Viticulture
  <br/>Surveyors
  <br/>Street railroads
  <br/>Agricultural laborers--Italian Americans
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr height="80">
            <td height="80">
                Subject
            </td>
            <td class="confluenceTd">
                Heading Type
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify the type of subject heading
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Topic
                <br/>
                Function
                <br/>
                Occupation
                <br/>
                Title
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr height="80">
            <td height="80">
                Subject
            </td>
            <td class="confluenceTd">
                Source
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify if the name heading was taken from one of these authority files
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                LCSH
                <br/>
                AAT
                <br/>
                TGM
                <br/>
                Local
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Subject
            </td>
            <td class="confluenceTd">
                Authority ID
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="FormGenre">Form/Genre</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Form/Genre
            </td>
            <td class="confluenceTd">
                Heading
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Forms or genres of materials significantly represented in or by the resource.
            </td>
            <td class="confluenceTd">
  <br/>Photographs
  <br/>Aerial photographs
  <br/>Tintypes
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr height="80">
            <td height="80">
                Form/Genre
            </td>
            <td class="confluenceTd">
                Source
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Specify if the name heading was taken from one of these authority files
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                LCSH
                <br/>
                AAT
                <br/>
                TGM
                <br/>
                Local
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                Form/Genre
            </td>
            <td class="confluenceTd">
                Authority ID
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
    </tbody>
</table>

### Administrative Information

<table class="confluenceTable">
    <tbody>
        <tr>
            <th class="confluenceTh">
                Field Label
            </th>
            <th class="confluenceTh">
                Subfield Label
            </th>
            <th class="confluenceTh">
                Required (Calisphere)?
            </th>
            <th class="confluenceTh">
		Summary
            </th>
            <th class="confluenceTh">
		Examples
            </th>
            <th class="confluenceTh">
                Vocabularies
            </th>
            <th class="confluenceTh">
                Repeatable?
            </th>
        </tr>

        <tr>
            <td class="confluenceTd">
                <a class="label" id="Provenance">Provenance</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Indicator of ownership and/or custody of the resource since its creation that are significant for its authenticity, integrity and
                interpretation.
            </td>
            <td class="confluenceTd">
                Donated by Harold Grimm, 2004<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                Yes
            </td>
        </tr>
        <tr>
            <td class="confluenceTd">
                <a class="label" id="PhysicalLocation">Physical Location</a>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
            <td class="confluenceTd">
                Reference to the location of the resource
            </td>
            <td class="confluenceTd">
                Map Case 1, Drawer 3<br/>
            </td>
            <td class="confluenceTd">
                <br/>
            </td>
            <td class="confluenceTd">
                No
            </td>
        </tr>
    </tbody>
</table>
