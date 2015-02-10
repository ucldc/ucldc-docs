---
layout: doc
title: Bulk Importing Content Files
next_section: dams/bulk-edit
prev_section: dams/edit-objects
permalink: /docs/dams/bulk-import/
breadcrumbs: DAMS User Guide
---

The bulk importer allows you to import multiple files at a time via a drag-and-drop interface, input common metadata, and select a project folder for all objects to be imported to. Press the 'Import' button in the top left of the sidebar on any page within the Workspace module to launch the importer. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/import-button.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/import-button.png" alt="Screenshot highlighting the import button" style="width: 500px">
</a>
<br>(click to enlarge)

## Some Notes on Uploading Files

The number and size of the files you can import in bulk is constrained by the limits of your internet speed and browser timeouts. You may try to run a bulk import, only to receive an error message that the browser timed out because the files could not be uploaded fast enough. At this point, you'll have to run the upload again, in smaller batches. 

Nuxeo could cap the **_number_** of files you can import, or cap the **_size_** of the files you can import (or some combination thereof), in order to give you an error message when dragging and dropping files into the bulk importer. Since we cannot know the speed of your internet connection though, this cap would be arbitrary. An arbitrary programatic cap on the _number_ of files you can import could prevent an otherwise successful upload of, say, 30 small files on a fast internet connection. Likewise, an arbitrary programatic cap on the _size_ of files you can import could prevent an otherwise successful upload of 2 large files. Rather than place these arbitrary programatic caps, which would not allow you to even begin an upload of more or larger files than the cap allows, it's up to you to test the boundaries of your internet connection. This may mean starting with a very small number of files and working your way up to test how much you can load at any given time. If you have a fairly consistent internet connection and speed, the number and size of files you find you can upload before the browser times out should stay fairly consistent. 

<div class="walkthrough new">New in Bruin</div>

## Creating Objects in Bulk

1. Select at least two image files on your computer that you would like to upload. You will need to keep them displayed some place on your screen, which may mean making your browser window smaller so you can see them on your Desktop, or in an open Folder. 
2. Make sure you have created either an example project folder like the one created in the walkthrough in the <a href="{{ site.url }}{{ site.baseurl}}/docs/dams/organization">Organizing Objects with Project Folders</a> document, or another other project folder you would like to upload to. 
3. In Nuxeo, press the Import button at the top left of the sidebar to launch the importer. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/import-form.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/import-form.png" alt="Screenshot showing the import form" style="width: 500px">
</a>
<br>(click to enlarge)

<ol start="4">
  <li>In the importer form that pops up, click inside the form where it says 'Folder name' next to the label 'Where' at the top of the form. </li>
  <li>Type in the name of the project folder you identified in step 2. </li>
</ol>

<div class="note"><p>The location to import objects to is <b>required</b>, and you cannot create a new project folder from within the importer workflow, so be sure this project folder exists beforehand.</p></div>

<ol start="6">
<li>Select your files from your Desktop or open Folder window, either as a group, or one at a time, and drag and drop them into the drop zone next to the 'Files' label. </li>
</ol>

<div class="note"><p>If you drag and drop more than three files, the first three will appear immediately in the drop zone, but the remaining files will appear one-by-one only after all prior files have been uploaded successfully. Even though a file may be successfully uploaded in the importer, you still have to press the 'Import' button at the bottom of the form before the browser times out to successfully import an object.</p></div>

<ol start="7"> <li>In the 'Title' field, type 'bulk-import'.</li></ol>

<div class="note"><p>You'll notice the full metadata form is provided with the importer, so you can provide any information that is common across all the objects you're uploading.</p></div>

<ol start="8">
<li>Press the 'Import' button at the bottom of the form. </li>
<li>You should be redirected to the project folder you chose in step 2, with your objects displayed under the title 'bulk-import'. If you have many objects in your project folder, click the arrow next to the 'Title' column header to sort the objects by name, or the arrow next to 'Modified' to sort the objects by Modification date.</li>
</ol>
