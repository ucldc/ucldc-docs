---
layout: technical-doc 
title: Common Index API 
prev_section: technical-docs/index/
permalink: /docs/technical-docs/solr-api/
breadcrumbs: Common Index API
---

The UCLDC project is running a harvest of objects in collections in both the Nuxeo DAMS and other external sources such as the OAC. In the upcoming releases, we’ll be releasing an interface to register your collection for harvest. For now, this collection registry is seeded with previously identified collections. All harvested data is stored in a Solr index in a standardized metadata schema, and can be retrieved using the publicly available Solr API.

##Solr Fields
***
This scheme is still undergoing active development. Find the most up-to-date scheme on GitHub: <a href="https://github.com/ucldc/solr_api/blob/master/dc-collection/conf/schema.xml" target="_blank">github.com/ucldc/solr_api/</a>.

<table class="confluenceTable">
  <tbody>
    <tr>
      <th class="confluenceTh">
        Name
      </th>
      <th class="confluenceTh">
        Type
      </th>
      <th class="confluenceTh">
        Comments
      </th>
      <th colspan="1" class="confluenceTh">
        Multi-Valued
      </th>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>text</code>
      </td>
      <td class="confluenceTd">
        text_general
      </td>
      <td class="confluenceTd">
        not stored; catchall text field for keyword search that indexes tokens - for each object, contains the following fields: <code>title</code>, <code>contributor</code>, <code>creator</code>, <code>coverage</code>, <code>date</code>, <code>description</code>, <code>extent</code>, <code>format</code>, <code>identifier</code>, <code>language</code>, <code>publisher</code>, <code>relation</code>, <code>rights</code>, <code>source</code>, <code>subject</code>, and <code>type</code>
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>text_rev</code>
      </td>
      <td class="confluenceTd">
        text_general_rev
      </td>
      <td class="confluenceTd">
        <span>not stored; the same as the <code>text</code> field, but in reverse for efficient leading wildcard queries</span>
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>timestamp</code>
      </td>
      <td class="confluenceTd">
        date
      </td>
      <td class="confluenceTd">
        timestamp on the Solr document - <span>default value is <code>NOW</code>, ie the time of object creation in the Solr index.</span>
      </td>
      <td colspan="1" class="confluenceTd">
        no
      </td>
    </tr>
    <tr>
      <td colspan="4" class="confluenceTd">
        <strong>COLLECTION REGISTRY FIELDS - all multivalued so an object can be related to more than one Campus, Repository, and/or Collection</strong>
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>campus</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        <code>campus</code> stores the URL to the registry API campus object
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>campus_name</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        <code>campus_name</code> stores the name of the campus, so that clients don’t need to look up against the registry API
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>collection_url</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        <code>collection</code> stores the URL to the registry API collection object
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>collection_name</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        <span><code>collection_name</code> stores the name of the collection, so that clients don’t need to look up against the registry API</span>
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <pre>
collection_data
</pre>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        <pre>
collection_url::collection_name
</pre>
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>repository_url</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        <code>repository</code> stores the URL to the registry API repository object
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>repository_name</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        <code>repository_name</code> stores the name of the repository, so that clients don’t need to look up against the registry API
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <pre>
repository_data
</pre>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        <pre>
repository_url::repository_name
</pre>
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="4" class="confluenceTd">
        <strong>METADATA ON THE METADATA</strong>
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>created</code>
      </td>
      <td class="confluenceTd">
        date
      </td>
      <td class="confluenceTd">
        refers to creation of the metadata document, not creation of the Solr document, nor creation of the content object
      </td>
      <td colspan="1" class="confluenceTd">
        no
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>last_modified</code>
      </td>
      <td class="confluenceTd">
        date
      </td>
      <td class="confluenceTd">
        refers to the date the metadata document was last modified
      </td>
      <td colspan="1" class="confluenceTd">
        no
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>created_s</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        string variant of <code>created</code> for wildcard searching
      </td>
      <td colspan="1" class="confluenceTd">
        no
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>last_modified_s</code>
      </td>
      <td class="confluenceTd">
        string
      </td>
      <td class="confluenceTd">
        string variant of <code>last_modified</code> for wildcard searching
      </td>
      <td colspan="1" class="confluenceTd">
        no
      </td>
    </tr>
    <tr>
      <td colspan="4" class="confluenceTd">
        <strong>DUBLIN CORE FIELDS</strong>
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>title</code>
      </td>
      <td class="confluenceTd">
        text_general
      </td>
      <td class="confluenceTd">
        only required field
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>contributor</code>
      </td>
      <td class="confluenceTd">
        text_general
      </td>
      <td class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>coverage</code>
      </td>
      <td class="confluenceTd">
        text_general
      </td>
      <td class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td class="confluenceTd">
        <code>creator</code>
      </td>
      <td class="confluenceTd">
        text_general
      </td>
      <td class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>date</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>description</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>extent</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>format</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>identifier</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>language</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>publisher</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        <span>yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>relation</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>rights</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>source</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>subject</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>type</code>
      </td>
      <td colspan="1" class="confluenceTd">
        text_general
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>date_facet</code>
      </td>
      <td colspan="1" class="confluenceTd">
        date
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="4" class="confluenceTd">
        <strong>IMAGE FIELDS</strong>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>url_item</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        best guess at home url for the item. Filled in by akara? currently indexed to search for items with it filled in, but will likely not be indexed in final release
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>reference_image_md5</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        <p>
          not indexed; holds the md5 of the best image found for image objects this will then be passed to the thumbnail server for nicely sized images. For now you can use md5s3stash to calculate url to image
        </p>
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>payloads</code>
      </td>
      <td colspan="1" class="confluenceTd">
        payloads
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>_version_</code>
      </td>
      <td colspan="1" class="confluenceTd">
        long
      </td>
      <td colspan="1" class="confluenceTd">
        <p>
          &nbsp;
        </p>
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="4" class="confluenceTd">
        <strong>DUBLIN CORE STRING FIELDS - copies of the Dublin Core field by the same name, but stored and indexed as strings, instead of tokenized text</strong>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>title_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>contributor_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>coverage_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>creator_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>date_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>description_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>extent_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>format_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>identifer_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>language_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>publisher_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>relation_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>rights_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>source_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>subject_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <code>type_ss</code>
      </td>
      <td colspan="1" class="confluenceTd">
        string
      </td>
      <td colspan="1" class="confluenceTd">
        &nbsp;
      </td>
      <td colspan="1" class="confluenceTd">
        yes
      </td>
    </tr>
    <tr>
      <td colspan="4" class="confluenceTd">
        <span><strong><span style="color: rgb(128,128,0);">FIELDS COMING SOON - needed for launch</span></strong> <span style="color: rgb(128,128,0);">(finalize this list by the beginning of May)</span></span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <pre>
<span style="color: rgb(128,128,0);">facet_decade</span>
</pre>
      </td>
      <td colspan="1" class="confluenceTd">
        <span style="color: rgb(128,128,0);">string</span>
      </td>
      <td colspan="1" class="confluenceTd">
        <span style="color: rgb(51,204,204);"><a href="https://github.com/ucldc/facet_decade" class="external-link" rel="nofollow"><span style="color: rgb(51,204,204);">https://github.com/ucldc/facet_decade</span></a></span>
      </td>
      <td colspan="1" class="confluenceTd">
        <span style="color: rgb(128,128,0);">yes</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <pre>
<span style="color: rgb(128,128,0);">structmap_url</span>
</pre>
      </td>
      <td colspan="1" class="confluenceTd">
        <span style="color: rgb(128,128,0);">string</span>
      </td>
      <td rowspan="2" class="confluenceTd">
        <p>
          <span style="color: rgb(128,128,0);">Only present for “deep content” (nuxeo harvested items)</span>
        </p>
        <p>
          <span style="color: rgb(51,204,204);"><a href="https://github.com/ucldc/ucldc-docs/wiki/media.json" class="external-link" rel="nofollow"><span style="color: rgb(51,204,204);">https://github.com/ucldc/ucldc-docs/wiki/media.json</span></a></span>
        </p>
      </td>
      <td colspan="1" class="confluenceTd">
        <span style="color: rgb(128,128,0);">no</span>
      </td>
    </tr>
    <tr>
      <td colspan="1" class="confluenceTd">
        <pre>
<span style="color: rgb(128,128,0);">structmap_text</span>
</pre>
      </td>
      <td colspan="1" class="confluenceTd">
        <span style="color: rgb(128,128,0);">string</span>
      </td>
      <td colspan="1" class="confluenceTd">
        <span style="color: rgb(128,128,0);">no</span>
      </td>
    </tr>
  </tbody>
</table>

The Solr API
=================

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
