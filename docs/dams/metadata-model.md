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

<p>The following table summarizes data elements that must be present in each metadata record for harvest into the Common Index. Note that default values for <b>Type</b>, <b>Copyright Status</b>, and <b>Copyright Statement</b> can optionally be supplied and applied to individual metadata records at the time they are harvested, using the Collection Registry:</p>

* <a class="label">Main Content File</a>
* <a class="label">Title</a>
* <a class="label">Type</a>
* <a class="label">Copyright Status</a>
* <a class="label">Copyright Statement</a>


##The Metadata Scheme
***

### Content Files

<table>
    <tbody>
        <tr style="background-color:LightGray">
            <th>
                Field Label
            </th>
            <th>
                Required (Calisphere)?
            </th>
            <th>
		Summary
            </th>
        </tr>

        <tr>
            <td>
                <a class="label" id="MainContentFile">Main Content File</a>
            </td>
            <td>
                Yes
            </td>
            <td>
                The main resource file. Used to generate display files (main file, thumbnail, etc.) in the index and Calisphere once you “publish” the object.
            </td>
        </tr>
  
          <tr>
            <td>
                <a class="label" id="AuxiliaryFiles">Auxiliary Files</a>
            </td>
            <td>
                No
            </td>
            <td>
                Additional resource files including variant formats and derivative copies of the main content file. These files will not be published to the index or Calisphere.
            </td>
        </tr>
		
		        <tr>
            <td>
                <a class="label" id="AuxiliaryFileType">Auxiliary File Type</a>
            </td>
            <td>
                No
            </td>
            <td>
                Qualifier identifying the kind of auxiliary file.
            </td>
        </tr>
    </tbody>
</table>


### Basic Information

<table>
    <tbody>
        <tr style="background-color:LightGray">
            <th>
                Field Label
            </th>
            <th>
                Subfield Label
            </th>
            <th>
                Required (Calisphere)?
            </th>
            <th>
		Summary
            </th>
            <th>
		Examples
            </th>
            <th>
                Vocabularies
            </th>
            <th>
                Repeatable?
            </th>
        </tr>
        <tr>
            <td>
                <a class="label" id="Title">Title</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                A formal or supplied title for the resource.
            </td>
            <td>
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
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="AlternativeTitle">Alternative Title</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Alternative or additional titles for the resource.
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="Identifier">Identifier</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                An ARK identifier for the resource
            </td>
            <td>
                ark.cdlib.org/ark:/13030/kt987021sv/
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="LocalIdentifier">Local Identifier</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                A local item or call number for the resource.
            </td>
            <td>
                MSS 0124.144
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="Type">Type</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                A high-level characterizes of the resource type.
            </td>
            <td>
                Image
            </td>
            <td>
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
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CampusUnit">Campus/Unit</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                URL reference to the Campus/Unit that is responsible for maintaining and curating the resource. This unique URL is assigned via the Collection Registry. In subsequent releases, this field will be integrated with the Collection Registry. For now, if you are adding new objects to the DAMS, please consult with us and we can work with you to populate this field.
            </td>
            <td>
                <a href="https://registry.cdlib.org/api/v1/repository/4/">https://registry.cdlib.org/api/v1/repository/4/ </a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="Date">Date</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                Date
            </td>
            <td>
                No
            </td>
            <td>
                A single date or inclusive dates indicating when the resource was created.
            </td>
            <td>
  <u>Example:</u>
  <br/>Single dates 
  <br/>1901
  <br/>1901 January 3
  <br/><br/>
  <u>Date spans</u>
  <br/>1900-1950
  <br/>1956 January-July
  <br/>1980s
  <br/>19th century 
  <br/><br/>
  <u>Broken date spans</u>
  <br/>1924, 1956-1975
  <br/><br/>
  <u>Open date spans</u>
  <br/>1911-
  <br/>-1911
  <br/><br/>
  <u>Approximate dates</u>
  <br/>circa 1950 
  <br/>undated: circa mid 20th century [Note: if a resource is undated this can be stated but provide an estimate if possible; normalize as an interval, perhaps using the dates of the life of creator, etc.]
			
			
			
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                Date Type
            </td>
            <td>
                No
            </td>
            <td>
                Use to qualify date, for unpublished (created) vs. published (issued) materials
            </td>
            <td>
                Created
				<br/>
            </td>
            <td>
                Created
                <br/>
                Issued
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                Single
            </td>
            <td>
                No
            </td>
            <td>
                ISO-8601 normalized single date
            </td>
            <td>
                1979-05-14<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                Inclusive Start
            </td>
            <td>
                No
            </td>
            <td>
                ISO-8601 normalized start date (for date ranges)
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                Inclusive End
            </td>
            <td>
                No
            </td>
            <td>
                ISO-8601 normalized end date (for date ranges)
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="PublicationInformation">Publication Information</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Publication statements and/or names of persons, families, or organizations responsible for publishing the resource.
            </td>
            <td>
                  American Philosophical Society 
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="Creator">Creator</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Creator
            </td>
            <td>
                Name
            </td>
            <td>
                No
            </td>
            <td>
                Names of persons, families, or organizations primarily responsible for creating the resource.
            </td>
            <td>
                  <u>Personal name entry</u>
  <br/>Yamada, Mitsuye 
  <br/>
  <br/>
  <u>Corporate name entry</u>
  <br/>Frasher Foto
  <br/>
   <br/>
  <u>Families</u>
  <br/>Robinson family
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Creator
            </td>
            <td>
                Name Type
            </td>
            <td>
                No
            </td>
            <td>
                Specify the identity type
            </td>
            <td>
                <br/>
            </td>
            <td>
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Creator
            </td>
            <td>
                Role
            </td>
            <td>
                No
            </td>
            <td>
                Specify the role of the identity
            </td>
            <td>
                Photographer<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Creator
            </td>
            <td>
                Source
            </td>
            <td>
                No
            </td>
            <td>
                Specify if the name heading was taken from one of these authority files
            </td>
            <td>
                <br/>
            </td>
            <td>
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Creator
            </td>
            <td>
                Authority ID
            </td>
            <td>
                No
            </td>
            <td>
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="Contributor">Contributor</a>
            </td>
            <td>
                <br/>
            </td>
        </tr>
        <tr>
            <td>
                Contributor
            </td>
            <td>
                Name
            </td>
            <td>
                No
            </td>
            <td>
                Names of persons, families, or organizations responsible for contributing to the resource in some significant manner.
            </td>
            <td>
                  <u>Personal name entry</u>
  <br/>Chase, Alexander W. (Alexander Wells), 1843-1888 
  <br/>
  <br/>
  <u>Corporate name entry</u>
  <br/>Prescott Foundation
  <br/>
   <br/>
  <u>Families</u>
  <br/>Thompson family
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Contributor
            </td>
            <td>
                Name Type
            </td>
            <td>
                No
            </td>
            <td>
                Specify the identity type
            </td>
            <td>
                <br/>
            </td>
            <td>
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Contributor
            </td>
            <td>
                Role
            </td>
            <td>
                No
            </td>
            <td>
                Specify the role of the identity
            </td>
            <td>
                Editor<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Contributor
            </td>
            <td>
                Source
            </td>
            <td>
                No
            </td>
            <td>
                Specify if the name heading was taken from one of these authority files
            </td>
            <td>
                <br/>
            </td>
            <td>
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Contributor
            </td>
            <td>
                Authority ID
            </td>
            <td>
                No
            </td>
            <td>
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
    </tbody>
</table>

### Content and Characteristics

<table>
    <tbody>
        <tr style="background-color:LightGray">
            <th>
                Field Label
            </th>
            <th>
                Subfield Label
            </th>
            <th>
                Required (Calisphere)?
            </th>
            <th>
		Summary
            </th>
            <th>
		Examples
            </th>
            <th>
                Vocabularies
            </th>
            <th>
                Repeatable?
            </th>
        </tr>
        <tr>
            <td>
                <a class="label" id="FormatPhysicalDescription">Format/Physical Description</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                A description of the physical or digital manifestation of the resource. Typically, this may include an indicator of the size and duration.
            </td>
            <td>
                1 photographic print
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="Description">Description</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Description
            </td>
            <td>
                (Note)
            </td>
            <td>
                No
            </td>
            <td>
                Descriptive statements that characterize more fully the scope or content of the resource.
            </td>
            <td>
                Depicts unknown automobile driver stopping at roadside to add water to engine on all-day drive from Chico to Sacramento<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr height="360">
            <td height="360">
                <a class="label" id="DescriptionType">Description Type</a>
            </td>
            <td>
                Type
            </td>
            <td>
                No
            </td>
            <td>
                Indicate the description type
            </td>
            <td>
                Scope/Content<br/>
            </td>
            <td>
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
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="Extent">Extent</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                A more specific statement of the size or duration of the resource (if not specified in Format/Physical Description)
            </td>
            <td>
                9 x 14 cm.
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="Language">Language</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Language
            </td>
            <td>
                Language
            </td>
            <td>
                No
            </td>
            <td>
                Languages significantly represented in or by the resource
            </td>
            <td>
                English<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Language
            </td>
            <td>
                Language Code
            </td>
            <td>
                No
            </td>
            <td>
                ISO-632b language code
            </td>
            <td>
                eng<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="TemporalCoverage">Temporal Coverage</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Temporal characteristics of the resource
            </td>
            <td>
                Surveyed 4/1/1931
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="Transcription">Transcription</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                A transcription of textual information, for resources that are text-based or document formats
            </td>
            <td>
                Martinez California December 31, 1893. My dear Sister Mary, I wish you a happy New Year, You and all yours. Heaven bless you all. Ever affectionately Your brother John Muir
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
    </tbody>
</table>

### Conditions of Access and Use

<table>
    <tbody>
        <tr style="background-color:LightGray">
            <th>
                Field Label
            </th>
            <th>
                Subfield Label
            </th>
            <th>
                Required (Calisphere)?
            </th>
            <th>
		Summary
            </th>
            <th>
		Examples
            </th>
            <th>
                Vocabularies
            </th>
            <th>
                Repeatable?
            </th>
        </tr>
        <tr>
            <td>
                <a class="label" id="AccessRestrictions">Access Restrictions</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Specifies level of access, for viewing resource in the UCLDC discovery/delivery system
            </td>
            <td>
                <br/>
            </td>
            <td>
                Public
                <br/>
                UC systemwide
                <br/>
                UC campus only
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightStatus">Copyright Status</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                A coded designation for the copyright status of the resource, at the time the rights statement is recorded.
            </td>
            <td>
                Copyrighted<br/>
            </td>
            <td>
                Copyrighted
                <br/>
                Public domain
                <br/>
                Copyright unknown
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightStatement">Copyright Statement</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Statement summarizing the copyright status of the resource
            </td>
            <td>
                 <u>Example (status "unknown"):</u>
  <br/>Some materials in these collections may be protected by the U.S. Copyright Law (Title 17, U.S.C.). In addition, the reproduction, and/or commercial use, of some materials may be restricted by gift or purchase agreements, donor restrictions, privacy and publicity rights, licensing agreement(s), and/or trademark rights. Distribution or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. To the extent other restrictions apply, permission for distribution or reproduction from the applicable rights holder is also required. Responsibility for obtaining permissions, and for any use rests exclusively with the user.
  <br/>
  <br/> <u>Example (status "public domain"):</u>
  <br/>Material in the public domain. No restrictions on use.
  <br/>
  <br/><u>Example (status "copyrighted"):</u>
  <br/>Transmission or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="CopyrightHolder">Copyright Holder</a>
            </td>
            <td>
                <br/>
            </td>
        </tr>
        <tr>
            <td>
                Copyright Holder
            </td>
            <td>
                Name
            </td>
            <td>
                No
            </td>
            <td>
                Names of persons, families, or organizations holding copyright to the resource
            </td>
            <td>
                Boe, Janet<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Copyright Holder
            </td>
            <td>
                Name Type
            </td>
            <td>
                No
            </td>
            <td>
                Specify the identity type
            </td>
            <td>
                <br/>
            </td>
            <td>
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Copyright Holder
            </td>
            <td>
                Source
            </td>
            <td>
                No
            </td>
            <td>
                Specify if the name heading was taken from one of these authority files
            </td>
            <td>
                <br/>
            </td>
            <td>
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Copyright Holder
            </td>
            <td>
                Authority ID
            </td>
            <td>
                No
            </td>
            <td>
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightContact">Copyright Contact</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Information on who to contact, to clear copyright permissions
            </td>
            <td>
                Consult Special Collections and Archives<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightNotice">Copyright Notice</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Transcription of any formal copyright notice on the work
            </td>
            <td>
                Copyright 1975<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightDeterminationDate">Copyright Determination Date</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                The date that the copyright status recorded in Copyright Status was determined.
            </td>
            <td>
                4/12/12<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightStartDate">Copyright Start Date</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                The start date for which the copyright applies or is applied to the resource
            </td>
            <td>
                1/1/32<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightEndDate">Copyright End Date</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                The end date for which the copyright applies or is applied to the resource
            </td>
            <td>
                12/31/21<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightJurisdiction">Copyright Jurisdiction</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                The country whose copyright laws apply.
            </td>
            <td>
                us<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="CopyrightNote">Copyright Note</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Additional information about the copyright status of the resource
            </td>
            <td>
                Rights transferred to UC Regents by Dane Jo in 1980<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
     </tbody>
</table>


### Related Materials

<table>
    <tbody>
        <tr style="background-color:LightGray">
            <th>
                Field Label
            </th>
            <th>
                Subfield Label
            </th>
            <th>
                Required (Calisphere)?
            </th>
            <th>
		Summary
            </th>
            <th>
		Examples
            </th>
            <th>
                Vocabularies
            </th>
            <th>
                Repeatable?
            </th>
        </tr>
        <tr>
            <td>
                <a class="label" id="Collection">Collection</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                URL reference to associated collections. This unique URL is assigned via the Collection Registry. In subsequent releases, this field will be integrated with the Collection Registry. For now, if you are adding new objects to the DAMS, please consult with us and we can work with you to populate this field.
            </td>
            <td>
                https://registry.cdlib.org/api/v1/collection/10/<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="RelatedResource">Related Resource</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Reference to other related resources (by theme, topic, collection, etc.)
            </td>
            <td>
                Series 1: Personal and Business Correspondence<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="Source">Source</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Reference to a resource from which the present resource is derived.
            </td>
            <td>
                Selected photograph from page 12 of the Lawrence & Houseworth Photography Album (Item Number #MS R01 042)<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
		</tbody>
</table>

### Access Points

<table>
    <tbody>
        <tr style="background-color:LightGray">
            <th>
                Field Label
            </th>
            <th>
                Subfield Label
            </th>
            <th>
                Required (Calisphere)?
            </th>
            <th>
		Summary
            </th>
            <th>
		Examples
            </th>
            <th>
                Vocabularies
            </th>
            <th>
                Repeatable?
            </th>
        </tr>

        <tr>
            <td colspan="6">
                <a class="label" id="SubjectName">Subject (Name)</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Subject (Name)
            </td>
            <td>
                Name
            </td>
            <td>
                No
            </td>
            <td>
                Personal, corporate, or family names significantly represented in or by the resource.
            </td>
            <td>
                                  <u>Personal name entry</u>
  <br/>White, Ira Johnson
  <br/>
  <br/>
  <u>Corporate name entry</u>
  <br/>Glacier Ice, Inc.
  <br/>
   <br/>
  <u>Families</u>
  <br/>Swiss family
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Subject (Name)
            </td>
            <td>
                Name Type
            </td>
            <td>
                No
            </td>
            <td>
                Specify the identity type
            </td>
            <td>
                <br/>
            </td>
            <td>
                Corporate name
                <br/>
                Family name
                <br/>
                Personal name
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Subject (Name)
            </td>
            <td>
                Role
            </td>
            <td>
                No
            </td>
            <td>
                Specify the role of the identity
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Subject (Name)
            </td>
            <td>
                Source
            </td>
            <td>
                No
            </td>
            <td>
                Specify if the name heading was taken from one of these authority files
            </td>
            <td>
                <br/>
            </td>
            <td>
                LCNAF
                <br/>
                Local
                <br/>
                ULAN
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Subject (Name)
            </td>
            <td>
                Authority ID
            </td>
            <td>
                No
            </td>
            <td>
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="Place">Place</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Place
            </td>
            <td>
                Name
            </td>
            <td>
                No
            </td>
            <td>
                Names of geographic locations significantly represented in or by the resource.
            </td>
            <td>
                San Mateo (county); California; United States<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Place
            </td>
            <td>
                Coordinates
            </td>
            <td>
                No
            </td>
            <td>
                Geographic coordinates
            </td>
            <td>
                (-121Â° 35' 30"", 36Â° 47' 30"") (-122Â° 25' 00"", 37Â° 37' 00"")<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr height="100">
            <td height="100">
                Place
            </td>
            <td>
                Source
            </td>
            <td>
                No
            </td>
            <td>
                Specify if the name heading was taken from one of these authority files
            </td>
            <td>
                <br/>
            </td>
            <td>
                LCSH
                <br/>
                TGN
                <br/>
                Geonames
                <br/>
                Local
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Place
            </td>
            <td>
                Authority ID
            </td>
            <td>
                No
            </td>
            <td>
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="SubjectTopicFunctionOccupation)">Subject (Topic, Function, Occupation)</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Subject
            </td>
            <td>
                Heading
            </td>
            <td>
                No
            </td>
            <td>
                Topics or subjects (including concepts, events, etc.), functions, or occupations significantly represented in or by the resource.
            </td>
            <td>
                  <br/>Viticulture
  <br/>Surveyors
  <br/>Street railroads
  <br/>Agricultural laborers--Italian Americans
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr height="80">
            <td height="80">
                Subject
            </td>
            <td>
                Heading Type
            </td>
            <td>
                No
            </td>
            <td>
                Specify the type of subject heading
            </td>
            <td>
                <br/>
            </td>
            <td>
                Topic
                <br/>
                Function
                <br/>
                Occupation
                <br/>
                Title
            </td>
            <td>
                No
            </td>
        </tr>
        <tr height="80">
            <td height="80">
                Subject
            </td>
            <td>
                Source
            </td>
            <td>
                No
            </td>
            <td>
                Specify if the name heading was taken from one of these authority files
            </td>
            <td>
                <br/>
            </td>
            <td>
                LCSH
                <br/>
                AAT
                <br/>
                TGM
                <br/>
                Local
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Subject
            </td>
            <td>
                Authority ID
            </td>
            <td>
                No
            </td>
            <td>
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td colspan="6">
                <a class="label" id="FormGenre">Form/Genre</a>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                Form/Genre
            </td>
            <td>
                Heading
            </td>
            <td>
                No
            </td>
            <td>
                Forms or genres of materials significantly represented in or by the resource.
            </td>
            <td>
  <br/>Photographs
  <br/>Aerial photographs
  <br/>Tintypes
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
        <tr height="80">
            <td height="80">
                Form/Genre
            </td>
            <td>
                Source
            </td>
            <td>
                No
            </td>
            <td>
                Specify if the name heading was taken from one of these authority files
            </td>
            <td>
                <br/>
            </td>
            <td>
                LCSH
                <br/>
                AAT
                <br/>
                TGM
                <br/>
                Local
            </td>
            <td>
                No
            </td>
        </tr>
        <tr>
            <td>
                Form/Genre
            </td>
            <td>
                Authority ID
            </td>
            <td>
                No
            </td>
            <td>
                If the name heading was taken from an authority file, specify the identifier
            </td>
            <td>
                <br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
    </tbody>
</table>

### Administrative Information

<table>
    <tbody>
        <tr style="background-color:LightGray">
            <th>
                Field Label
            </th>
            <th>
                Subfield Label
            </th>
            <th>
                Required (Calisphere)?
            </th>
            <th>
		Summary
            </th>
            <th>
		Examples
            </th>
            <th>
                Vocabularies
            </th>
            <th>
                Repeatable?
            </th>
        </tr>

        <tr>
            <td>
                <a class="label" id="Provenance">Provenance</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Indicator of ownership and/or custody of the resource since its creation that are significant for its authenticity, integrity and
                interpretation.
            </td>
            <td>
                Donated by Harold Grimm, 2004<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                Yes
            </td>
        </tr>
        <tr>
            <td>
                <a class="label" id="PhysicalLocation">Physical Location</a>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
            <td>
                Reference to the location of the resource
            </td>
            <td>
                Map Case 1, Drawer 3<br/>
            </td>
            <td>
                <br/>
            </td>
            <td>
                No
            </td>
        </tr>
    </tbody>
</table>
