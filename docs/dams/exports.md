---
layout: dams-doc
title: Exporting Objects
prev_section: dams/publish/
permalink: /docs/dams/exports/
breadcrumbs: DAMS User Guide
---

Objects can be exported from Nuxeo one at a time, or as a batch. Additionally, you can opt to export the metadata records only, or the entire object -- i.e., metadata records plus associated content files.

## Exporting individual objects: Nuxeo XML metadata and content files

To export records for an individual object, select the "Export Options" function from the toolbar.

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/export.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/export.png" alt="Export Options" style="width: 500px">
</a>

You then have the option to select an export format.  The "XML Export" comprises the metadata in the source Nuxeo XML format.  The "ZIP Tree XML Export" and "ZIP Binary Export" include the metadata in Nuxeo XML format, along with associated content files.


## Exporting multiple objects: Nuxeo XML metadata and content files

To export records for multiple objects, select the relevant objects from the content listing.

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/4_bulk-edit.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/4_bulk-edit.png" alt="Screenshot of a content listing" style="width: 500px">
</a>
<br>(click to enlarge)

If there are many objects in your project folder, complex object, or search result set you'll notice that they don't all appear on one page. In order to see all the objects, you will have to paginate through the content listing via the forwards and backwards arrows above and below the content listing. Select a larger number of objects to be shown per page from the drop down at the top right labeled 'Items/page'. The default value is 20. 

Selecting an object is maintained while you paginate - ie, if you select the third object on the first page and the fifth object on the second page, both objects will remain selected for bulk editing. In order to select all objects on a given page, use the select all checkbox - located in the header of the content view next to 'Title'. This checkbox will _only_ select objects on a given page, though. To select _all_ objects in a given project folder, increase the number of objects displayed per page to 50 (the maximum setting) and then paginate through, checking the select all checkbox on each page of 50 objects.

Object are deselected as soon as you navigate to a different project folder, or into an object. 

Once you've selected the objects, select the "Export Options" function from the toolbar.  You then have the option to select an export format.  The "XML Export" comprises the metadata in the source Nuxeo XML format.  The "ZIP Tree XML Export" and "ZIP Binary Export" include the metadata in Nuxeo XML format, along with associated content files.

## Editing metadata in Excel format

You can export metadata for a single object or multiple objects in Excel format.

First, follow the instructions for selecting all of the relevant metadata fields that you'd like to include in the Excel export, using the <a href="https://registry.cdlib.org/documentation/docs/dams/spreadsheet-view/">Spreadsheet View</a> feature.

Once you've selected the fields and they are displaying in the content view, select the "Excel Export" option to generate the Excel file.

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/4_bulk-edit.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/excel.png" alt="Excel export" style="width: 500px">
</a>
<br>(click to enlarge)
