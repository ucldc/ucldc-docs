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
  <p><b>created</b></p>
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
  <p><b>created_s</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>string variant of <b>created</b> for wildcard searching </p>
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
  <p><b>id</b></p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p>Unique identifier assigned by CDL to the
  object, derived from <b>identifier</b> (if the value is an ARK) or otherwise
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
  <p><b>last_modified</b></p>
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
  <p><b>last_modified_s</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>string variant of <b>last_modified</b> for wildcard searching </p>
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
  <p><b>text</b></p>
  </td>
  <td class="confluenceTd">
  <p>text_general</p>
  </td>
  <td class="confluenceTd">
  <p>not stored; catchall
  text field for keyword search that indexes tokens - for each object, contains
  the following fields: <b>title</b>, <b>contributor</b>, <b>creator</b>, <b>coverage</b>, <b>date</b>, <b>description</b>, <b>extent</b>, <b>format</b>, <b>identifier</b>, <b>language</b>, <b>publisher</b>, <b>relation</b>, <b>rights</b>, <b>source</b>, <b>subject</b>, and <b>type</b> </p>
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
  <p><b>text_rev</b></p>
  </td>
  <td class="confluenceTd">
  <p>text_general_rev</p>
  </td>
  <td class="confluenceTd">
  <p>not stored; the same
  as the <b>text</b> field, but in reverse for efficient leading
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
  <p><b>timestamp</b></p>
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
  <p><b>campus</b></p>
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
  <p><b>campus_data</b></p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p><b>campus_name</b>::<b>campus_url</b></p>
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
  <p><b>campus_name</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>Stores the name of the campus, so that
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
  <p><b>campus_url</b></p>
  </td>
  <td class="confluenceTd">
  <p>string</p>
  </td>
  <td class="confluenceTd">
  <p>Stores the URL to the
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
  <p><b>collection_data</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p><b>collection_url</b>::<b>collection_name</b></p>
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
  <p><b>collection_name</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>Stores the name of the collection, so that
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
  <p><b>collection_url</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>Stores the URL to the registry API collection object </p>
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
  <p><b>repository_data</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p><b>repository_url</b>::<b>repository_name</b></p>
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
  <p><b>repository_name</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>Stores the name of the repository, so that
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
  <p><b>repository_url</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>Stores the URL to the registry API repository object </p>
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
  <p><b>sort_collection_data</b></p>
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
 </tr>
 <tr>
  <td class="confluenceTd">
  <p><b>alternative_title</b></p>
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
  <p><b>contributor</b> </p>
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
  <p><b>coverage</b></p>
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
  <p><b>creator</b></p>
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
  <p><b>date</b></p>
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
  <p><b>description</b> </p>
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
  <p><b>extent</b></p>
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
  <p><b>facet_decade</b></p>
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
  <p><b>format</b></p>
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
  <p><b>genre</b></p>
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
  <p><b>identifier</b> </p>
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
  <p><b>language</b></p>
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
  <p><b>location</b></p>
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
  <p><b>provenance</b></p>
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
  <p><b>publisher</b></p>
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
  <p><b>relation</b></p>
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
  <p><b>rights</b></p>
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
  <p><b>rights_holder</b></p>
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
  <p><b>rights_note</b></p>
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
  <p><b>rights_date</b></p>
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
  <p><b>sort_date_start</b></p>
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
  <p><b>sort_date_end</b></p>
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
  <p><b>sort_title</b></p>
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
  <p><b>source</b></p>
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
  <p><b>subject</b></p>
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
  <p><b>temporal</b></p>
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
  <p><b>transcription</b></p>
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
  <p><b>title</b></p>
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
  <p><b>type</b></p>
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
  <p><b>url_item</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>bestguess at home URL
  for the item. Filled in at time of harvesting, currently indexed
  to search for items with it filled in</p>
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
  <p><b>reference_image_dimensions</b></p>
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
  <p><b>reference_image_md5</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>not indexed; holds the md5 of the best image found for image
  objects this will then be passed to the thumbnail server for nicely sized
  images. For now you can use <b>md5s3stash</b> to calculate the URL
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
  <p><b>structmap_text</b></p>
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
  <p><b>structmap_url</b></p>
  </td>
  <td class="confluenceTd">
  <p>string </p>
  </td>
  <td class="confluenceTd">
  <p>Only present for objects harvested from Nuxeo </p>
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
  <p><b>alternative_title_ss</b></p>
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
  <p><b>contributor_ss</b></p>
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
  <p><b>coverage_ss</b></p>
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
  <p><b>creator_ss</b></p>
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
  <p><b>date_ss</b></p>
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
  <p><b>description_ss</b></p>
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
  <p><b>extent_ss</b></p>
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
  <p><b>format_ss</b></p>
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
  <p><b>genre_ss</b></p>
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
  <p><b>identifier_ss</b></p>
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
  <p><b>language_ss</b></p>
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
  <p><b>location_ss</b></p>
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
  <p><b>provenance_ss</b></p>
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
  <p><b>publisher_ss</b></p>
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
  <p><b>relation_ss</b></p>
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
  <p><b>rights_ss</b></p>
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
  <p><b>rights_holder_ss</b></p>
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
  <p><b>rights_note_ss</b></p>
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
  <p><b>rights_date_ss</b></p>
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
  <p><b>source_ss</b></p>
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
  <p><b>subject_ss</b></p>
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
  <p><b>temporal_ss</b></p>
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
  <p><b>transcription_ss</b></p>
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
  <p><b>title_ss</b></p>
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
  <p><b>type_ss</b></p>
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
