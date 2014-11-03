---
layout: doc
title: Search

next_section: dams/delete
prev_section: dams/bulk-edit
permalink: /docs/dams/search/
breadcrumbs: DAMS User Guide
---

The DAMS supports many different kinds of searching: 

- **Quick Search**: Allows you to quickly find objects throughout the DAMS using only keywords. 
- **Filter Search**: Restricts searching to the current campus folder, project folder, or complex object. A filter search only searches against the title of an object. 
- **Faceted Search**: Searches on keyword, like quick search, as well as a variety of other fields. Faceted Search, like Filter Search, also allows you to limit the search to a particular campus folder, project folder, or complex object. 
- **Advanced Search**: Allows you to perform a very precise search by searching against more metadata elements than those available in faceted search. Advanced Search also allows you to customize the way search results are displayed. 

<div class="note">The walkthroughs in this section assume you've completed the walkthroughs in <a class="notelink" href="{{ site.url }}{{ site.baseurl }}/docs/dams/clipboard/">Using the Clipboard and Worklist</a>. </div>

## Quick Search

Search the entire Nuxeo DAMS by keyword using the Quick Search in the top right corner of the DAMS. This keyword search is performed over an index of all the metadata fields for an object, so this could potentially generate a lot of noise for ambiguous search terms. 

<div class="walkthrough new">Bear Walkthrough</div>

1. Try entering the email address you use to sign in into the quick search text box. Click the magnifying glass or press enter to search. 
2. You should see all the objects you have created in Nuxeo. 
3. Try searching 'UC Berkeley Bears' by quick search. 
4. You should see the two Golden Bear objects with the alternative title 'UC Berkeley Bears', one from your sample project folder and one your Bear Collection project folder. 

## Filter Search

From within a given campus folder, project folder, or complex object, Filter Search allows you to filter the contents by a [full text search]() on the title field. 

<div class="walkthrough new">Bear Walkthrough</div>

1. From within your sample folder in your campus folder, type 'Golden' into the filter box, and then press Filter. 
2. You should see your 'Golden Bear' object in the content listing. 
3. Click the 'Clear Filter' button to see all the objects in your sample folder again. 

## Faceted Search

The faceted search is located in the sidebar. Navigate to it by clicking the magnifying glass icon to the right of the hierarchy icon. Faceted search includes a small subset of fields to search on: 

- **Keyword Search**: Keyword search behaves just like Quick Search. This searches a full-text index of all objects in the DAMS by keyword. 
- **Field Search**: Field search is a [full text search]() on the following fields: Identifier, Local Identifier, Title, Creator Name, Contributor Name, Date, and Description. 
- **Project Folder**: Constrains the search to one or more campus or project folders in the DAMS. 
- **Metadata Record History**: Username is an autocomplete field and allows you to search for objects a particular user has modified or created. Creation Date and Date Modified search by a date range for objects created or modified, respectively, in the given date range. 

<div class="walkthrough new">Bear Walkthrough</div>

1. From anywhere within the Asset Library, shown in the breadcrumbs, select the faceted search by clicking the magnifying glass icon in the sidebar, next to the hierarchy icon. 
2. Next to 'Alternative Title', click the 'Add' button. 
3. In the field that appears, type 'UC Berkeley'
4. Next to 'Project Folder', click the 'Add' button. 
5. In the hierarchy overlay that appears, navigate to your sample project folder, within your campus folder, by clicking the + and - buttons to the left of the folder names. 
6. Click the name of your sample project folder. If the faceted search is still visible behind the overlay, you should see the name of your sample project folder appear there. 
7. Click the 'x' in the top right corner of the overlay to close it. 
8. Click the 'Filter' button. 
9. You should see your Golden Bear object in the search results. 

## Advanced Search

Find a link to advanced search in the top right corner, just to the right of quick search. Advanced search includes a keyword search, like quick search, the ability to constrain a search to one or more campus or project folders, like filter search and faceted search, and a search on the metadata record history, like faceted search. 

Additionally, you can search for deleted documents, and perform a [full text search]() on all of the following fields: 

* Basic Information: Identifier, Local Identifier, Title, Alternative Title, Date, Creator Name, Contributor Name, Type
* Content and Characteristics: Description, Language
* Conditions of Access and Use: Access Restrictions, Copyright Status, Copyright Holder
* Access Points: Subject (Name), Subject (Topic), Place Name, and Form/Genre 

Copyright End Date is the only field on advanced search that is not a full text search, but is an exact match search, instead. 

Advanced search also allows you to customize which fields are displayed in the results listing. All of the following fields are selected by default. To remove a field from the search results listing, navigate to the 'Search Results' box below the 'Metadata Record History' box on the advanced search form, select the fields you don't want displayed in the search results under 'Selected Columns', and then press the left arrow button to move them out of 'Selected Columns' and into 'Available Columns'. Move a field back using the right arrow button. Reorder the columns using the up and down arrow buttons. 

TODO: SCREENSHOT

## Full Text Search

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