---
layout: technical-doc 
title: Common Index API 
prev_section: technical-docs/index/
permalink: /docs/technical-docs/solr-api/
breadcrumbs: Common Index API
---

The UCLDC project is running a harvest of objects in collections in both the Nuxeo DAMS and other external sources such as the OAC. In the upcoming releases, we’ll be releasing an interface to register your collection for harvest. For now, this collection registry is seeded with previously identified collections. All harvested data is stored in a Solr index in a standardized metadata schema, and can be retrieved using the publicly available Solr API.

##Using the API

In order to access the Solr API, you will have to obtain an API Authentication Token. Request a token by emailing <a href="mailto:ucldc@ucop.edu">ucldc@ucop.edu</a> or your [campus contact]({{ site.url }}{{ site.baseurl }}/docs/collection-admins/). 

Queries can be made using curl, or any Solr library that supports authentication tokens: <br/>
<code>curl -H 'X-Authentication-Token: xxxx-xxxx-xxxx-xxxx' "https://registry.cdlib.org/solr/query/?q=fred"</code> 

We're using solrpy - a python library with Solr bindings - to hit Solr: [https://github.com/edsu/solrpy](https://github.com/edsu/solrpy).

The following are common query parameters. Consult the Solr documentation for a complete list of available query parameters. 

<p>
<b>q</b> - default query parameter, searches the text field by default unless a different field is otherwise specified. Takes a comma separated list of field: search_string pairs:

<ul>
  <li><code>q=*:*</code> - returns all objects in the index<br/>
      https://registry.cdlib.org/solr/query/?q=*:*&wt=json&indent=true
  </li>
  <li><code>q=mosswood park</code> - returns all objects in the index with an instance of mosswood park in their metadata<br/>
      https://registry.cdlib.org/solr/query/?q=mosswood+park&wt=json&indent=true
  </li>
  <li><code>q=title: "mosswood park", collection_name: "Parks in Oakland, California - Views"</code> - returns all objects with mosswood park in the title and a collection name of "Parks in Oakland, California - Views"<br/>
    https://registry.cdlib.org/solr/query/?q=title: "mosswood park", collection_name: "Parks in Oakland, California - Views"&wt=json&indent=true
  </li>
</ul>
</p>

<p>
<b>rows</b> - number of objects to return, default value is 10
<ul>
  <li><code>rows=6</code> - returns the first six objects in the index<br/>
      https://registry.cdlib.org/solr/query/?q=*:*&rows=6&wt=json&indent=true
  </li>
</ul>
</p>

<p>
<b>start</b> - object to start on, default value is 0 - specifying start and rows together can create pagination
<ul>
  <li><code>start=2</code> - returns the third object through the 13th in the index<br/>
      https://registry.cdlib.org/solr/query/?q=*:*&start=2&wt=json&indent=true
  </li>
</ul>
</p>

<p>
<b>fq</b> - filter the query by specifying a value for a field. Filter on the string (_ss) version of the field to avoid tokenization and provide exact matches
<ul>
  <li><code>fq=type_ss: image</code> - returns all objects with a type of 'image'<br/>
      https://registry.cdlib.org/solr/query/?q=*:*&fq=type_ss: image&wt=json&indent=true
  </li>
</ul>
</p>

<p>
<b>facet</b> - true|false
</p>

<p>
<b>facet_limit</b> - number of facets to return (set to -1 to display all facets)
</p>

<p>
<b>facet_field</b> - fields to return facets for (ex: collection_name)
</p>

##The Solr Fields
***
This scheme is still undergoing active development. Find the most up-to-date scheme on GitHub: <a href="https://github.com/ucldc/solr_api/blob/master/dc-collection/conf/schema.xml" target="_blank">github.com/ucldc/solr_api/</a>.

* <b>Name</b>: indicates the field name
* <b>Type</b>: indicates the field type
* <b>Comments</b>: notes regarding use of the field
* <b>Multi-valued</b>: indicates if field is repeatable
* <b>Indexed</b>: indicates if the value of the field can be used in queries to retrieve matching documents
* <b>Stored</b>: indicates if the value of the field is stored in the index, and the value of the field can be retrieved by queries

<table class="confluenceTable">
 <tr>
  <th class="confluenceTh">
  <p><b>Name </b></p>
  </th>
  <th class="confluenceTh">
  <p><b>Type </b></p>
  </th>
  <th class="confluenceTh">
  <p><b>Comments </b></p>
  </th>
  <th class="confluenceTh">
  <p><b>Multi-Valued </b></p>
  </th>
  <th class="confluenceTh">
  <p><b>Indexed?</b></p>
  </th>
  <th class="confluenceTh">
  <p><b>Stored?</b></p>
  </th>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p><b>General and administrative fields</b></p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>created</p>
  </td>
  <td class="confluenceTd">
  <p>date </p>
  </td>
  <td class="confluenceTd">
  <p>refers to creation
  of the metadata document, not creation of the Solr
  document, nor creation of the content object </p>
  </td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>created_s</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>string variant of created for wildcard searching </p>
  </td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>id</p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p>Unique identifier assigned by CDL to the
  object, derived from identifier (if the value is an ARK) or otherwise
  auto-generated. This value also is also used within the context of the URL
  for the object in Calisphere.</p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>last_modified</p>
  </td>
  <td class="confluenceTd">
  <p>date </p>
  </td>
  <td class="confluenceTd">
  <p>refers to the date
  the metadata document was last modified </p>
  </td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6'>
  <td class="confluenceTd">
  <p>last_modified_s</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>string variant of last_modifiedfor wildcard searching </p>
  </td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7'>
  <td class="confluenceTd">
  <p>text</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>not stored; catchall
  text field for keyword search that indexes tokens - for each object, contains
  the following fields: title, contributor, creator, coverage, date, description, extent, format, identifier, language, publisher, relation, rights, source, subject, and type </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8'>
  <td class="confluenceTd">
  <p>text_rev</p>
  </td>
  <td class="confluenceTd">
  <p>text_general_rev</p>
  </td>
  <td class="confluenceTd">
  <p>not stored; the same
  as the textfield, but in reverse for efficient leading
  wildcard queries </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9'>
  <td class="confluenceTd">
  <p>timestamp</p>
  </td>
  <td class="confluenceTd">
  <p>date </p>
  </td>
  <td class="confluenceTd">
  <p>timestampon the Solr
  document - default value is NOW, ie the time of
  object creation in the Solr index. </p>
  </td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p><b>Metadata fields (supplied
  through the Collection Registry; all multivalued so an object can be related
  to more than one Campus, Repository, and/or Collection</b>)</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>campus</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>campus stores the URL to the registry API campus object </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>campus_data</p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p>campus_name::campus_url</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>campus_name</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>campus_namestores the name of the campus, so that
  clients don’t need to look up against the registry API </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:14'>
  <td class="confluenceTd">
  <p>campus_url</p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p>campus_url stores the URL to the
  registry API campus object</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>collection_data</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>collection_url::collection_name</p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>collection_name</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>collection_namestores the name of the collection, so that
  clients don’t need to look up against the registry API </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>collection_url</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>collection stores the URL to the registry API collection object </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>repository_data</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>repository_url::repository_name</p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>repository_name</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>repository_namestores the name of the repository, so that
  clients don’t need to look up against the registry API </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>repository_url</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>repository stores the URL to the registry API repository object </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>sort_collection_data</p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p>collection
  data with a normalized collection name for sorting</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p><b>Metadata fields
  (stored and indexed as tokenized text</b>)</p>
  </td>
  <td class="confluenceTd">
  <p><b></b></p>
  </td>
  <td class="confluenceTd">
  <p><b></b></p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>alternative_title</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>contributor </p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>coverage</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>creator</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>date</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>description </p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>extent</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>facet_decade</p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>format</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>genre</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>identifier </p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>language</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>location</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>provenance</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>publisher</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>relation</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights_holder</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights_note</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights_date</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>sort_date_start</p>
  </td>
  <td class="confluenceTd">
  <p>date</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>sort_date_end</p>
  </td>
  <td class="confluenceTd">
  <p>date</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>sort_title</p>
  </td>
  <td class="confluenceTd">
  <p>alphaSpaceSort</p>
  </td>
  <td class="confluenceTd">
  <p>Version of title
  used for lexical ordering</p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>source</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>subject</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>temporal</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>transcription</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>title</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>only required field </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>type</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p><b>Content file fields</b></p>
  </td>
 
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>url_item</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>bestguess at home url
  for the item. Filled in by akara? currently indexed
  to search for items with it filled in, but will likely not be indexed in
  final release </p>
  </td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>reference_image_dimensions</p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p>Pixel width:height.</p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>reference_image_md5</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>not indexed; holds the md5 of the best image found for image
  objects this will then be passed to the thumbnail server for nicely sized
  images. For now you can use md5s3stash to calculate url
  to image </p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>structmap_text</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd"></td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>no</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>structmap_url</p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>Only present for
  “deep content” (nuxeo harvested items) </p>
  <p><a
  href="https://github.com/ucldc/ucldc-docs/wiki/media.json">https://github.com/ucldc/ucldc-docs/wiki/media.json</a></p>
  </td>
  <td class="confluenceTd">
  <p>no </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p><b>Metadata fields
  (stored and indexed as strings, instead of tokenized text</b>)</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>alternative_title_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>contributor_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>coverage_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>creator_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>date_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>description_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>extent_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>format_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>genre_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>identifier_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>language_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>location_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>provenance_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>publisher_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>relation_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights_holder_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights_note_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>rights_date_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>source_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>subject_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>temporal_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>transcription_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p></p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>title_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>only required field </p>
  </td>
  <td class="confluenceTd">
  <p>yes </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
 <tr>
  <td class="confluenceTd">
  <p>type_ss</p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>&nbsp; </p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
  <td class="confluenceTd">
  <p>yes</p>
  </td>
 </tr>
</table>
