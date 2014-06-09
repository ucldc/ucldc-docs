---
layout: doc
title: Creating Complex Objects
next_section: 
prev_section: dams/edit-objects
permalink: /complex-objects/
---

## Creating Complex Objects

Any of the document types (Picture, File, Audio, Video) can contain any number of component objects of any document type. This structure can be flat: 

- UC Davis Oakville Experimental Vineyard photographs (Picture type)
  - Photograph 1 (Picture type)
  - Photograph 2 (Picture type)
  - Photograph 3 (Picture type)

Or hierarchical:

- Mondavi Center 2010-2011 season promotional materials (Picture type)
  - Photographs (Picture type, no content file)
    - Photograph 1 (Picture type)
    - Photograph 2 (Picture type)
    - Photograph 3 (Picture type)
  - Documents (File type, no content file)
    - Document 1 (File type)
    - Document 2 (File type)

Despite the fact that the parent object must have a document type, the parent object does not necessarily have to have a content file. In the hierarchical example above, the "Modavi Center 2010-2011 season promotional materials" object contains a visual representation of the object's contents, while the "Photographs" and "Documents" sub-objects contain no content files, and the bottom of the hierarchical tree (Photograph 1-3, Document 1-2) contain the actual content files. 

<div class="walkthrough">Banana Slug Walkthrough</div>

#### Create a Complex Object

1. From within your Banana Slug project folder, create a new Picture object. 
2. On the create object form, fill out the following metadata, and upload [this photograph]({{ site.url }}{{ site.baseurl }}/images/Original_complex-flat.jpg), as described in the [create objects section]({{ site.url }}{{ site.baseurl }}/docs/dams/create-objects/).

<table>
  <thead>
    <th>Identifier</th>
    <th>Title</th>
    <th>Alternative Title</th>
    <th class="w-1-3">Date</th>
    <th class="w-1-3">Creator</th>
  </thead>
  <tr>
    <td>ark:/13030/c8c53p1h</td>
    <td>Complex object (flat)</td>
    <td>UC Davis Oakville Experimental Vineyard photographs</td>
    <td>
      Date: 2013 May 13<br/>
      Date Type: created<br/>
      Single 2013-05-13
    </td>
    <td>
      Name: University of California Office of the President Communications<br/>
      Name Type: corpname
    </td>
  </tr>
</table>

<ol start="3">
  <li>Navigate to this object's Summary tab, and scroll down to find the section labeled 'Component Objects'.</li>
  <li>Press the 'New' button.</li>
  <li>Select the Picture document type from the list.</li>
  <li>On the create object form, fill out only the title to 'Photograph 1', then press 'Save'.</li>
  <li>Navigate back to the 'Complex object (flat)', and repeat steps 3-6 for 'Photograph 2' and 'Photograph 3'</li>
  <li>Navigate back to the summary tab for Photograph 1, and drag and drop <a href="{{ site.url }}{{ site.baseurl }}/images/Original_anr2_UCOP-43.jpg">Original_anr2_UCOP-43.jpg</a>.</li>
  <li>Navigate back to the summary tab for Photograph 2, scroll down to Metadata, and press the 'Edit' button.</li>
  <li>Press the upload button, and select wherever you have downloaded <a href="{{ site.url }}{{ site.baseurl }}/images/Original_anr2_UCOP-44.jpg">this photograph</a> to on your computer. Then scroll down to press 'Save'</li>
  <li>Return to the summary tab for Photograph 3, and choose one of the two methods for uploading the <a href="{{ site.url }}{{ site.baseurl }}/images/Original_anr2_UCOP-45.jpg">third content file</a>.</li> 
</ol>

Now the hierarchy sidebar should contain the following under your campus' name:

- Banana Slug
  - Complex object (flat)
    - Photograph 1
    - Photograph 2
    - Photograph 3

## Reordering Complex Object Sub-Objects

From any given parent object, you can order, reorder, and delete children by navigating to the 'Component Object' section on the Summary tab, selecting the checkbox next to the component object you would like to order or delete, and then pressing the 'Move to top', 'Move up', Move to bottom', 'Move down', or 'Delete' buttons accordingly. 

<div class="note">Only the components of a complex object are orderable. Children of project folders, such as Banana Slug, are not orderable. To delete an object in a Project Folder, navigate to the 'Content' tab on the Project Folder, select the checkbox next to the object you would like to delete, and press the 'Delete' button.</div>

<!---
TODO: 
Also need to touch on searching for an object

Also need to touch on this campus/unit registry-hook-up business (and bulk editing?)
--->