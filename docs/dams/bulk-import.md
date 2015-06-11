---
layout: dams-doc
title: Bulk Importing Content Files
next_section: dams/bulk-edit/
prev_section: dams/edit-objects/
permalink: /docs/dams/bulk-import/
breadcrumbs: DAMS User Guide
---

You have two general options for bulk importing multiple content files into Nuxeo:

* Install and use the Nuxeo File Uploader client
* Use the Nuxeo drag-and-drop feature, within the web interface


## Upload Multiple Files with the Nuxeo File Uploader

### Initial Setup

<ol>
<li>Download the client:</li>

<ul>
<li>Windows: <a href="http://dscl-dev.cdlib.org/nuxeo_client/uclNuxeoUpload.zip">download</a> and unzip the contents of the to a folder on your workstation</li>
<li>Mac: <a href="http://dscl-dev.cdlib.org/nuxeo_client/uclNuxeoUpload.dmg">download</a> and install the .dmg file into your Applications folder</li>
</ul>

<li>Run the client:</li>

<ul>
<li>Windows: launch <b>uclNuxeoUpload.exe</b>.  Note that it may take a few moments for the client to open.</li>
<li>Mac: launch <b>uclNuxeoUpload</b> from Applications.</li>
</ul>

<li>Select the wrench icon in the upper right ("Setup Nuxeo Connection"), for a one-time configuration of the client.  This will launch an Application Configuration window.</li>
<li>First, ensure that the following URL is in the Nuxeo Server field (note the https): <b>https://nuxeo.cdlib.org/nuxeo</b></li>
<li>Next, you'll need to obtain a Nuxeo Token, to allow the client to authenticate and connect to Nuxeo.</li>
 <ul>
 <li>Click "Sign-in and get a Nuxeo Access Token for this computer".</li>  
 <li>You will then be prompted to login, using your single sign-on account.</li>  
 <li>Once you login, you will receive a pop-up window indicating the Nuxeo Token.  Right-click and copy the alphanumeric string.</li>
 <li>Close the pop-up window.</li>
 </ul>

<li>In the Application Configuration window, paste the alphanumeric string into the Nuxeo Token field.	Optionally, in the Path Filter field, append your campus folder name (e.g., "asset-library/UCM").  Once you begin using the client, this will limit your upload target locations to Project Folders associated only with your campus.</li>
<li>Last, double-check the Application Configuration window settings:</li>

<ul>
<li><b>Nuxeo Server</b>:		<b>https://nuxeo.cdlib.org/nuxeo</b></li>
<li><b>Nuxeo Token</b>: 		<b>(alphanumeric string)</b></li>
<li><b>Path Filter</b>:		<b>/asset-library/</b>  (optionally, campus folder name appended to the end)</li>
</ul>
</ol>

### Using the Client

<ul>
<li><b>Choose Files button</b>: click the Choose Files button to browse to and select files to upload to Nuxeo.  By default, uploaded files will result in the creation of simple objects in the target Project Folder.</li>
<li><b>Select Project Folder pull-down</b>: select the target Project Folder for uploading the files.</li>
<li><b>Start Upload button</b>: hit this button to once you've chosen files and selected a target Project Folder.
<li>Clear file and Project Folder selections using the reset button in the upper right corner.</li>
</ul>

## Upload Multiple Files through the Nuxeo Interface

The bulk importer allows you to upload multiple files at a time via a drag-and-drop interface, input common metadata, and select a project folder for all objects to be imported to. Press the 'Import' button in the top left of the sidebar on any page within the Workspace module to launch the importer. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/import-button.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/import-button.png" alt="Screenshot highlighting the import button" style="width: 500px">
</a>
<br>(click to enlarge)

## Some Notes on Uploading Files

We recommend using the Nuxeo File Uploader client, for the purpose of uploading large batches of files.  The client is optimized to maintain a dedicated connection to the Nuxeo server, and lacks some of the constraints with importing files through a web browser.

In the case of the Nuxeo interface, the number and size of the files you can upload in bulk is constrained by the limits of your internet speed and Shibboleth. You may try to run a bulk import, only to receive an error message that your Shibboleth session timed out because the files could not be uploaded fast enough. At this point, you'll have to run the upload again, in smaller batches. We encourage you to test the importer with various files to guage your local capactiy. If you have a fairly consistent internet connection and upload speed, the amount of files you can upload before Shibboleth times out should stay fairly consistent. 

If you drag and drop more than three files, the first three will appear immediately in the drop zone, but the remaining files will appear one-by-one only after all prior files have been uploaded successfully. Even though a file may be successfully uploaded in the importer, you still have to press the 'Import' button at the bottom of the form <b><i>before your Shibboleth session times out</i></b> to successfully import an object. For all of the above reasons, we generally suggest you use the importer for small batches of files.

<div class="walkthrough new">New in Bruin</div>

## Creating Objects in Bulk

1. Select at least two image files on your computer that you would like to upload. You will need to keep them displayed some place on your screen, which may mean making your browser window smaller so you can see them on your Desktop, or in an open Folder. 
2. Make sure you have created either an example project folder like the one created in the walkthrough in the <a href="{{ site.url }}{{ site.baseurl}}/docs/dams/organization/">Organizing Objects with Project Folders</a> document, or another other project folder you would like to upload to. 
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

<div class="note"><p>As mentioned above in <a href="{{ site.url }}{{ site.baseurl }}/docs/dams/bulk-import/#some-notes-on-uploading-files" class="notelink">Some Notes on Uploading Files</a>, if you upload more than three files, the first three will immediately appear in the drop zone, and the remaining files will appear one-by-one after all prior files have been uploaded. Additionally, you still have to press the 'Import' button at the bottom of the form <b><i>before your Shibboleth session times out</i></b>!</p></div>

<ol start="7"> <li>In the 'Title' field, type 'bulk-import'.</li></ol>

<div class="note"><p>You'll notice the full metadata form is provided with the importer, so you can provide any information that is common across all the objects you're uploading.</p></div>

<ol start="8">
<li>Press the 'Import' button at the bottom of the form. </li>
<li>You should be redirected to the project folder you chose in step 2, with your objects displayed under the title 'bulk-import'. If you have many objects in your project folder, click the arrow next to the 'Title' column header to sort the objects by name, or the arrow next to 'Modified' to sort the objects by Modification date.</li>
</ol>
