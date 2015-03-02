---
layout: doc
title: Creating Complex Objects
next_section: dams/edit-objects
prev_section: dams/create-objects
permalink: /docs/dams/complex-objects/
breadcrumbs: DAMS User Guide
---

## Complex objects in the DAMS
As mentioned earlier, complex objects comprise multiple files and even multiple metadata records which are “bundled” together. In the DAMS, these are represented as objects that have both parent-level and child-level components. You might think of them as objects-within-objects.

Any of the document types (Picture, File, Audio, Video) can contain any number of component objects of any document type. While Nuxeo can be used to create a hierarchical component structure, this can present a number of complications for rendering and display in Calisphere and other access systems.  We hence recommend utilizing a flat, single-level hierarchical component structure.  Here is an example of a series of related photographs: 

- UC Davis Oakville Experimental Vineyard photographs (Picture type)
  - Photograph 1 (Picture type)
  - Photograph 2 (Picture type)
  - Photograph 3 (Picture type)

And here is an example of a multi-page item, where the sequence of pages is important to preserve for rendering and display:

- Mondavi Center 2010-2011 season promotional brochure (Text type)
  - Page 1
  - Page 2
  - Page 3
  - Page 4

There is no limit on the number of child-level components for a given complex object, and they are orderable via the 'Summary' tab for the parent-level component.

## Not all components need files
Despite the fact that the parent-level component must have a document type, it does not necessarily have to have a content file. In the hierarchical example above, the "Mondavi Center 2010-2011 season promotional materials" component contains a visual representation of the object's contents, while the "Photographs" and "Documents" child-level components contain no content files, and the components at the bottom of the hierarchical tree (Photograph 1-3, Document 1-2) contain the actual content files. 

<div class="walkthrough">Walkthrough</div>

## Create a Complex Object
For this exercise, you use the following sample files. Download them and place them somewhere easy-to-find.
- A content file for the parent-level: <a href="{{ site.url }}{{ site.baseurl }}/images/Original_complex-flat.jpg" download>Original_complex-flat.jpg</a>
- A content file for a component: <a href="{{ site.url }}{{ site.baseurl }}/images/Original_anr2_UCOP-43.jpg" download>Original_anr2_UCOP-43.jpg</a>
- Another content file for a component: <a href="{{ site.url }}{{ site.baseurl }}/images/Original_anr2_UCOP-44.jpg" download>Original_anr2_UCOP-44.jpg</a>
- Another content file for a component: <a href="{{ site.url }}{{ site.baseurl }}/images/Original_anr2_UCOP-45.jpg" download>Original_anr2_UCOP-45.jpg</a>

1. From within your sample project folder, create a new Picture object. (See [Organizing Objects with Project Folders]({{ site.url }}{{ site.baseurl }}/docs/dams/organization/) to create a sample project folder, if you haven't already.)
2. On the create object form, fill out the following metadata, upload the content file Original_complex-flat.jpg, and press the 'Create' button as described in the [create objects section]({{ site.url }}{{ site.baseurl }}/docs/dams/create-objects/).

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
  <li>On the create object form, add just a title: 'Photograph 1.' Then press 'Create'.</li>
  <li>Navigate back to the 'Complex object (flat)', and repeat steps 3-6 for 'Photograph 2' and 'Photograph 3'.</li>
  <li>Navigate back to the summary tab for Photograph 1, and drag and drop the first sample component file, Original_anr2_UCOP-43.jpg, onto the available drop zone.</li>
  <li>Navigate back to the summary tab for Photograph 2, scroll down to Metadata, and press the 'Edit' button.</li>
  <li>Press the upload button, and select the second sample component file, Original_anr2_UCOP-44.jpg from the files on your computer. Then scroll down to press 'Save'</li>
  <li>Return to the summary tab for Photograph 3, and choose one of the two methods described above for uploading the last component file, Original_anr2_UCOP-45.jpg.</li> 
</ol>

Now the hierarchy sidebar should contain the following under your campus's name:

- Your Sample Project Folder
  - Complex object (flat)
    - Photograph 1
    - Photograph 2
    - Photograph 3

## Reordering Complex Object Sub-Objects

From any given parent object, you can order, reorder, and delete children by navigating to the 'Component Object' section on the Summary tab, selecting the checkbox next to the component object you would like to order or delete, and then pressing the 'Move to top', 'Move up', Move to bottom', 'Move down', or 'Delete' buttons accordingly. (By default, child-level components will appear in the order in which they're added.)

<div class="note">Only the components of a complex object are orderable. Objects within project folders, such as 'Your Sample Project Folder' (your test folder) are not orderable. To delete an object in a Project Folder, navigate to the 'Content' tab on the Project Folder, select the checkbox next to the object you would like to delete, and press the 'Delete' button.</div>
