---
title: Search
next_section: dams/permissions
prev_section: dams/bulk-edit
---

The DAMS supports many different kinds of searching. 

Search from anywhere in the DAMS Workspace: 

- <b><a href="{{ site.url }}{{ site.baseurl }}/docs/dams/search/#quick-search">Quick Search</a></b>: Allows you to quickly find objects throughout the DAMS using only keywords. 
- <b><a href="{{ site.url }}{{ site.baseurl }}/docs/dams/search/#filter-search">Filter Search</a></b>: Restricts searching to the current campus folder, project folder, or complex object. A filter search only searches against the title of an object. 

Search from the Search Module - Allows you to choose from a few different custom search forms:

- <b><a href="{{ site.url }}{{ site.baseurl }}/docs/dams/search/#custom-faceted-search">Custom Faceted Search</a></b>: Searches on keyword, like quick search, as well as a variety of other fields. Custom Faceted Search, like Filter Search, also allows you to limit the search to a particular campus folder, project folder, or complex object. 
- <b><a href="{{ site.url }}{{ site.baseurl }}/docs/dams/search/#custom-advanced-search">Custom Advanced Search</a></b>: Allows you to perform a very precise search by searching against more metadata elements than those available in faceted search. 

Click the image to see where each of these search options are located. Each search method is described in more depth below. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/search.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/search.png" alt="Screenshot of where to find search" style="width: 500px">
</a>
<br>(click to enlarge)

## Search from Anywhere

### Quick Search

Search the entire Nuxeo DAMS by keyword using the Quick Search in the top right corner of the DAMS. This keyword search is performed over an index of all the metadata fields for an object, so this could potentially generate a lot of noise for ambiguous search terms. 

### Filter Search

From within a given campus folder, project folder, or complex object, Filter Search allows you to filter the contents by a [full text search]({{ site.url }}{{ site.baseurl }}/docs/dams/search/#FullTextSearch) on the title field. 

## Search Module

Enter the Search Module by clicking 'Search' in the main navigation bar. Select a search form from the drop down at the top of the sidebar. We have created two custom search forms: Custom Faceted Search and Custom Advanced Search - Custom Advanced Search is the default. 

<div class="note">Nuxeo 6 introduced the new 'Search' module, which combines Faceted Search (previously in the 'Document Management' module's sidebar) and Advanced Search (previously a link next to Quick Search) on one page by listing both search forms in a drop down in the new 'Search' module.</div>

### Custom Faceted Search

Select 'customFacetedSearch' from the drop down at the top of the sidebar in the Search Module to show the Custom Faceted Search form. Custom Faceted Search includes a small subset of fields to search on: 

- **Keyword Search**: Keyword search behaves just like Quick Search. This searches a full-text index of all objects in the DAMS by keyword. 
- **Field Search**: Field search is a [full text search]({{ site.url }}{{ site.baseurl }}/docs/dams/search/#FullTextSearch) on the following fields: Identifier, Local Identifier, Title, Creator Name, Contributor Name, Date, and Description. 
- **Project Folder**: Constrains the search to one or more campus or project folders in the DAMS. 
- **Metadata Record History**: Username is an autocomplete field and allows you to search for objects a particular user has modified or created. Creation Date and Date Modified search by a date range for objects created or modified, respectively, in the given date range. 

<div class="walkthrough new">Walkthrough - Custom Faceted Search</div>

1. From any page, navigate to the Search Module by clicking 'Search' in the navigation bar. 
2. Select the Custom Faceted Search form in the drop down in the sidebar by selecting 'customFacetedSearch'
3. Next to 'Project Folder', click the 'Add' button. 
4. In the hierarchy overlay that appears, navigate to a project folder, within your campus folder, by clicking the + and - buttons to the left of the folder names. 
5. Click the name of the project folder. If the faceted search is still visible behind the overlay, you should see the name of the project folder appear there. 
7. Click the 'x' in the top right corner of the overlay to close it. 
8. Click the 'Filter' button. 
9. You should see the contents of the project folder in the search results. 

### Custom Advanced Search

Select 'customAdvancedSearch' from the drop down at the top of the sidebar in the Search Module to show the Custom Advanced Search form. Custom Advanced Search includes a keyword search, like quick search, the ability to constrain a search to one or more campus or project folders, like filter search and custom faceted search, and a search on the metadata record history, like custom faceted search. 

Additionally, you can search for deleted documents, and perform a [full text search]({{ site.url }}{{ site.baseurl }}/docs/dams/search/#FullTextSearch) on all of the following fields: 

* Basic Information: Identifier, Local Identifier, Title, Alternative Title, Date, Creator Name, Contributor Name, Type
* Content and Characteristics: Description, Language
* Conditions of Access and Use: Access Restrictions, Copyright Status, Copyright Holder
* Access Points: Subject (Name), Subject (Topic), Place Name, and Form/Genre 

Copyright End Date is the only field on advanced search that is not a full text search, but is an exact match search, instead. 

<h2><a id="FullTextSearch" style="color: black">Full Text Search</a></h2>

Objects are indexed using their full metadata record. Nuxeo's full text search uses stemming - a process used to reduce words to their word stem, or root form. Full text search will return objects with the same stem as the word entered in the search form, so searching for 'jogging' will return objects with 'jog', 'jogged', 'jogs', and 'jogging'. Additionally, full text searches are not case-specific - searching for 'submarine', 'SUBMARINE', or 'Submarine' will return the same results. 

Full text search also supports boolean operators and wildcards. 

* **AND**: all the words separated by AND must be in the found objects. This is the default operator of all full-text search fields, so you actually just need your keywords and the AND operator is implied. 

* **-**: The keyword after this symbol must not be in the found documents. You need to keep the - stuck to the word to be excluded. If you put a space between the - and the word after it, the - is ignored. 

* **OR**: any of the words before 'OR' or the word after it must be in the found documents

* **double quotes ("")**: the exact expression between quotes must be in the found documents. 

* **%**: this symbol replaces zero or more characters. it works like the more commonly used * (asterisk). 

To avoid noise in the search results, some words are ignored. Typically words like 'the' or 'no' are not taken into account. Some characters are also ignored if they are used in the search forms: 

<div class="example" style="font-size: 16px;">
  <pre><code>!#$%&'()*+,./\\\\:-@{|}`^~</code></pre>
</div>
