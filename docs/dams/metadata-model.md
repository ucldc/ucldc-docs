---
layout: doc
title: Metadata Model
permalink: /metadata-model/
---

### Basic Information


<a class="label">Identifier</a> - A globally unique identifier for the resource.

<div class="example">
  <u>Example:</u>
  <br/>ark.cdlib.org/ark:/13030/kt987021sv/
</div>

<a class="label">Local Identifier</a> - A local item or call number for the resource.

<div class="example">
  <u>Example:</u>
  <br/>calb_p3353
  <br/>MSS 0124.144
</div>

<a class="label">Campus/Unit</a> - URL reference to the Campus/Unit that is responsible for maintaining and curating the resource.

<div class="example">
  <u>Example:</u>
  <br/>https://registry.cdlib.org/api/v1/repository/4/
</div>

<a class="label">Title</a> - A formal or supplied title for the resource.

<div class="example">
  <u>Example:</u>
  <br/>Formal titles
  <br/>The Rocky Mountains, emigrants crossing the plains [graphic] / F.F. Palmer, del. 
  <br/>
  <br/>Supplied titles
  <br/>Mitchell Bonner photograph of musicians performing at a cultural program 
  <br/>[Photograph of musicians performing at a cultural program] 
</div>

<a class="label">Alternative Title</a> - Alternative or additional titles for the resource.

<div class="example">
  <u>Example:</u>
  <br/>Formal titles
  <br/>The Rocky Mountains, emigrants crossing the plains [graphic] / F.F. Palmer, del. 
  <br/>
  <br/>Supplied titles
  <br/>Mitchell Bonner photograph of musicians performing at a cultural program 
  <br/>[Photograph of musicians performing at a cultural program]
</div>

<a class="label">Date</a> - A single date or inclusive dates indicating when the resource was created.

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

<a class="label">Type</a> - A high-level characterizes of the resource type.

<div class="example">
  <u>Example:</u>
  <br/>image
  <br/>text
  <br/>audio
</div>

<a class="label">Creator</a> - Names of persons, families, or organizations primarily responsible for creating the resource.

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

<a class="label">Contributor</a> - Names of persons, families, or organizations responsible for contributing to the resource in some significant manner.

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

<a class="label">Publication Information</a> - Publication statements and/or names of persons, families, or organizations responsible for publishing the resource.

<div class="example">
  <u>Example:</u>
  <br/>Corporate name entry
  <br/>American Philosophical Society 
  <br/>Frasher Foto (Firm) 
</div>

### Content and Characteristics

<a class="label">Format/Physical Description</a> - Description or statement indicating the extent, size, or duration of the resource.

<div class="example">
  <u>Example:</u>
  <br/>1 photographic print ; 9 x 14 cm. [Note: derived according to AACR2]
  <br/>14 letters [Note: derived according to DACS]
  <br/>1 leaflet : ill. ; 21.5 x 38.5 cm., folded to 21.5 x 10 cm. [Note: derived according to Graphic Materials]
</div>

<a class="label">Description</a> - A descriptive statement that characterizes more fully the scope or content of the resource.

<div class="example">
  <u>Example:</u>
  <br/>Depicts unknown automobile driver stopping at roadside to add water to engine on all-day drive from Chico to Sacramento. Exact location unknown. Verso stamped with 596; manuscript note indicates car owned by “N.E.R.”
</div>

<a class="label">Temporal Coverage</a> - Temporal characteristics of the resource

<div class="example">
  <u>Example:</u>
  <br/>Surveyed 4/1/1931
</div>

<a class="label">Language</a> - Languages significantly represented in or by the resource

<div class="example">
  <u>Example:</u>
  <br/>eng [Note: use for English]
  <br/>vie [Note: use for Vietnamese]
  <br/>ger [Note: use for German]
</div>

### Conditions of Access and Use

<a class="label">Access Restrictions</a> - Specifies level of access, for viewing resource in the UCLDC discovery/delivery system

<div class="example">
  <u>Example:</u>
  <br/>public
  <br/>UC systemwide
  <br/>UC campus only
</div>

<a class="label">Copyright Status</a> - A coded designation for the copyright status of the resource, at the time the rights statement is recorded.

<div class="example">
  <u>Example:</u>
  <br/>copyrighted
  <br/>public domain
  <br/>unknown
</div>

<a class="label">Copyright Statement</a> - Statement summarizing the copyright status of the resource 

<div class="example">
  <u>Example:</u>
  <br/>Transmission or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user
</div>

<a class="label">Copyright Holder</a> - Names of persons, families, or organizations holding copyright to the resource

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

<a class="label">Copyright Contact</a> - Information on who to contact, to clear copyright permissions

<div class="example">
  <u>Example:</u>
  <br/>Consult Special Collections and Archives
</div>

<a class="label">Copyright Notice</a> - Transcription of any formal copyright notice on the work

<div class="example">
  <u>Example:</u>
  <br/>Copyrighted 1967
</div>

<a class="label">Copyright Determination Date</a> - The date that the copyright status recorded in Copyright Status was determined.

<div class="example">
  <u>Example:</u>
  <br/>4/12/12
</div>

<a class="label">Copyright Start Date</a> - The start date for which the copyright applies or is applied to the resource

<div class="example">
  <u>Example:</u>
  <br/>1/1/32
</div>

<a class="label">Copyright End Date</a> - The end date for which the copyright applies or is applied to the resource

<div class="example">
  <u>Example:</u>
  <br/>12/31/54
</div>

<a class="label">Copyright Jurisdiction</a> - The country whose copyright laws apply.

<div class="example">
  <u>Example:</u>
  <br/>us
</div>

<a class="label">Copyright Note</a> - Additional information about the copyright status of the resource

<div class="example">
  <u>Example:</u>
  <br/>Additional information about the copyright status of the resource
</div>

### Related Materials

<a class="label">Collection</a> - URL reference to associated collections

<div class="example">
  <u>Example:</u>
  <br/>https://registry.cdlib.org/api/v1/collection/10/
</div>

<a class="label">Related Resource</a> - Reference to other related resources (by theme, topic, collection, etc.)

<div class="example">
  <u>Example:</u>
  <br/>Series 1: Personal and Business Correspondence
</div>

<a class="label">Source</a> - Referece to a resource from which the present resource is derived.

<div class="example">
  <u>Example:</u>
  <br/>Selected photograph from page 12 of the Lawrence & Houseworth Photography Album (Item Number #MS R01 042).
</div>

### Access Points

<a class="label">Subject (Name)</a> - Personal, corporate, or family names significantly represented in or by the resource.

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

<a class="label">Subject (Topic, Function, Occupation)</a> - Topics or subjects (including concepts, events, etc.), functions, or occupations significantly represented in or by the resource.

<div class="example">
  <u>Example:</u>
  <br/>Viticulture
  <br/>Surveyors
  <br/>Street railroads
  <br/>Agricultural laborers--Italian Americans
</div>

<a class="label">Place</a> - Names of geographic locations significantly represented in or by the resource.

<div class="example">
  <u>Example:</u>
  <br/>San Mateo (county); California; United States
  <br/>(-121Â° 35' 30"", 36Â° 47' 30"") (-122Â° 25' 00"", 37Â° 37' 00"")
</div>

<a class="label">Form/Genre</a> - Forms or genres of materials significantly represented in or by the resource.

<div class="example">
  <u>Example:</u>
  <br/>Photographs
  <br/>Aerial photographs
  <br/>Tintypes
</div>

### Administrative Information

<a class="label">Provenance</a> - Indicator of ownership and/or custody of the resource since its creation that are significant for its authenticity, integrity and interpretation. 

<div class="example">
  <u>Example:</u>
  <br/>Donated by Harold Grimm, 2004
</div>

<a class="label">Physical Location</a> - Reference to the location of the resource

<div class="example">
  <u>Example:</u>
  <br/>Map Case 1, Drawer 3
</div>
