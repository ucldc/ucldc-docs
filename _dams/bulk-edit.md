---
title: Bulk Edit Objects
next_section: dams/spreadsheet-view/
prev_section: dams/bulk-import/
---

Simple and complex objects of any type can be edited in bulk as long as they exist in the same project folder, are children of the same parent complex object, or appear in the same search result set. 

In each of these cases, there is a **_content listing_** displaying the contents of the project folder, complex object, or search result set. From this content listing, select the relevant objects for editing. The bulk edit form includes all the fields in the metadata scheme for an object.

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/4_bulk-edit.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/4_bulk-edit.png" alt="Screenshot of a content listing" style="width: 500px">
</a>
<br>(click to enlarge)

## Some Notes on Selecting Objects and Pagination

If there are many objects in your project folder, complex object, or search result set you'll notice that they don't all appear on one page. In order to see all the objects, you will have to paginate through the content listing via the forwards and backwards arrows above and below the content listing. Select a larger number of objects to be shown per page from the drop down at the top right labeled 'Items/page'. The default value is 20. 

Selecting an object is maintained while you paginate - ie, if you select the third object on the first page and the fifth object on the second page, both objects will remain selected for bulk editing. In order to select all objects on a given page, use the select all checkbox - located in the header of the content view next to 'Title'. This checkbox will _only_ select objects on a given page, though. To select _all_ objects in a given project folder, increase the number of objects displayed per page to 50 (the maximum setting) and then paginate through, checking the select all checkbox on each page of 50 objects.

Object are deselected as soon as you navigate to a different project folder, or into an object. 

<div class="walkthrough">Walkthrough</div>

## Editing Objects in Bulk

1. Navigate to your example project folder within your campus folder that you created in the walkthrough in the <a href="{{ site.url }}{{ site.baseurl}}/docs/dams/organization/">Organizing Objects with Project Folders</a> document. 
2. Create three simple objects in your example project folder as described in the walkthrough in the <a href="{{ site.url }}{{ site.baseurl }}/docs/dams/create-objects/">Creating Simple Objects</a> document. Give these simple objects an ID, but no title. 

<div class="note"><p>If you don't give your objects a title, in your project folder you will see your objects referred to by the 36 character unique alpha-numeric string used internally by the Nuxeo system. </p></div>

<ol start="3">
  <li>From within the project folder, select objects for bulk edit by checking the checkboxes to the left of the objects you just created.</li>
  <li>After selecting the objects for bulk edit, select the 'edit' button just below the object listing, on the left-hand side. A pop-up should appear displaying the same form you see for object creation and editing.</li>
  <li>Modify the title in the Bulk Edit form. Input 'Golden Bear' in the title field and 'Bear Objects' in the alternative title field.</li>
</ol>

<div class="note">You'll notice a checkbox next to each field that is automatically checked when the corresponding field is modified. Any field with a checked checkbox next to it will be modified for all the selected objects. Check a field's checkbox without entering anything into the field to delete that field's contents for multiple objects.<br><br>It is important to note that the process does not add information to pre-existing metadata within a given field.  It instead replaces the existing field (as well as any repeated instances of the field, or subfields) with the new metadata provided.</div>

<ol start="6">
  <li>Press the save button. You should see the content listing update to display the title 'Bear Objects' for all the objects you just bulk edited.</li>
</ol>
