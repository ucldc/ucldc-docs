---
layout: doc
title: Spreadsheet Editor
next_section: dams/clipboard/
prev_section: dams/bulk-edit/
permalink: /docs/dams/spreadsheet-view/
breadcrumbs: DAMS User Guide
---

Simple and complex objects of any type can be edited in spreadsheet view as long as they exist in the same project folder, are children of the same parent complex object, or appear in the same search result set. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/spreadsheet-view.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/spreadsheet-view.png" alt="Screenshot of the spreadsheet view" style="width: 500px">
</a>
<br>(click to enlarge)

In each of these cases, there is a **_content listing_** displaying the contents of the project folder, complex object, or search result set. From this content listing, you can select relevant metadata fields to view and edit in the spreadsheet editor, then open the spreadsheet editor. Do this by using the Edit Result Columns button, then open the spreadsheet by pressing the Spreadsheet button. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/spreadsheet-buttons.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/spreadsheet-buttons.png" alt="Screenshot of the spreadsheet buttons" style="width: 500px">
</a>
<br>(click to enlarge)

## Selecting Metadata Fields to Edit in Spreadsheet View

Only non-repeating metadata fields can be edited in spreadsheet view, since these are the only fields that can be represented in a single spreadsheet row per object. In the UCLDC metadata schema, the following fields are non-repeating: 

- **Basic Information**: Title, Identifier, Type 
- **Content and Characteristics**: Format/Physical Description, Extent, Transcription
- **Conditions of Access and Use**: Access Restrictions, Copyright Status, Copyright Statement, Copyright Contact, Copyright Notice, Copyright Determination Date, Copyright Start Date, Copyright End Date, Copyright Jurisdiction, Copyright Note
- **Related Materials**: Source
- **Administrative Information**: Physical Location

<div class="walkthrough new">Walkthrough - Spreadsheet Editor</div>

## Editing Objects in the Spreadsheet Editor

1. Navigate to your example project folder within your campus folder that you created in the walkthrough in the <a href="{{ site.url }}{{ site.baseurl}}/docs/dams/organization/">Organizing Objects with Project Folders</a> document. 
2. If there are no objects in your example project folder, create at least two objects and return to the project folder. 
3. You'll notice the default columns listed in the content view are 'Title', 'Local Identifier', and 'Modified'. Click the Edit Result Columns button on the top right of the content listing to add more columns. 
4. In the overlay that pops up, under 'Available Columns' find and select 'Identifier'. 
5. Click the right single arrow to move 'Identifier' from the 'Available Columns' to 'Selected Columns' list. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/edit-results-columns.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/edit-results-columns.png" alt="Screenshot of the edit result columns interface" style="width: 500px">
</a>
<br>(click to enlarge)

<ol start="6">
<li>Repeat steps 4 and 5 for 'Type'. </li>
<li>Press the 'Save' button. </li>
<li>You'll notice 'Identifier' and 'Type' columns appear in the content listing. </li>
<li>Click the Spreadsheet button. </li>
<li>You should see a spreadsheet with the columns 'Title', 'Modified', 'Identifier', and 'Type'. You'll notice that even though 'Local Identifier' was included in the content listing, it is not in the spreadsheet because it is a repeating field. </li>
<li>In the first row, under the 'Type' column, type 'image'. The cell will turn a darker color blue to indicate it has been modified. </li>
<li>With the cell you just modified selected, click on the square located in the bottom right corner, and drag down one row. You should see the second row populated with the value 'image'. </li>
<li>In the first row, under the 'Identifier' column, type '1'. </li>
<li>In the second row, under the 'Identifier' column, type '2'. </li>
<li>You should now have four modified cells. </li>
<li>Press the 'Save' button. You should see the content listing update to display values in the columns for 'Identifier' and 'Type'. </li>
</ol>
