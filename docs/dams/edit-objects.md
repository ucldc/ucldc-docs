---
layout: doc
title: Viewing and Editing Objects
next_section: 
prev_section: dams/complex-objects
permalink: /edit-objects/
---

## Viewing objects

Once an object is created, if you have read/write access to the object, you should see the following tabs: Summary, Publish, Comments, History, and Manage. You may also see the View and Picture Metadata tabs (if looking at a Picture object) or the Files tab (if looking at a File object). 

### Get to know your tabs

- **Summary** - On this tab, you can view a representation of the uploaded content file, create child objects, and view and edit object-level metadata. The Summary tab also includes process metadata such as relevant dates, users, and tags. Currently, all registered users have read access to all the objects in the DAMS. However, only registered users from a given campus will see edit buttons to modify metadata for objects in their campus folder. 

<div class="note">The State and Workflow Process for an object are also included on the Summary tab. These are built-in Nuxeo features we see as potentially useful, but we haven't fully built them out just yet. For now, you can mostly ignore those sections, but they may provide useful functionality in future releases.</div>

- **Publish** - The publish tab is a built-in Nuxeo feature. Currently, no accounts are set up to allow publishing to any sections. We anticipate this tab will allow you to publish content to Merritt for preservation, and/or to the new Calisphere interface. This tab will be developed in future releases. 

- **Comments** - The comment tab is a place to view and write comments on an object. 

- **History** - An ongoing record of the object's history: when it was created, when it was modified, and who performed the action. 

- **Manage** - On the Manage tab, you'll be able to see who has what level of access to your object. Access restrictions are inherited, unless the 'Block permissions inheritance' checkbox is checked, so these same restrictions apply for all children in the hierarchy.

- **View (Picture objects only)** - This tab shows the various derivatives of an image content file: Medium, Original, Small, Thumbnail, and OriginalJpeg. The derivatives produced are all JPEGs in various sizes.
  - 'Original' is the original file's size and file format.
  - 'OriginalJpeg' is the JPEG version of the original file, maintaining width and height values.
  - 'Medium', 'Small' and 'Thumbnail' are all JPEG derivatives of specific width and height values.
You can select a derivative and press the download button to download the content file to your computer. Any user with a minimum of Read permissions for an object can download the associated content file. If the user has write access, the View tab provides 90° rotation options for the image file. 

- **Picture Metadata (Picture objects only)** - This tab shows any metadata that was embedded in the image content file on upload. 

<div class="walkthrough">Banana Slug Features Walkthrough</div>

## Editing an Object

Let's navigate through the hierarchy back to the first image object we created: Root > Asset Library > Your campus folder > Banana Slug > Simple image object. 

1. On the Summary tab, scroll down to 'Metadata' and press the 'Edit' button. 
2. Under the Content and Characteristics heading, input the following metadata. 

<table>
  <thead>
    <th class="w-1-3">Format/Physical Description</th>
    <th>Description</th>
  </thead>
  <tr>
    <td>JPEG image, 3872 x 2592 pixels (16.13 x 10.8 in.)</td>
    <td>Photograph of two students packaging beets and other vegetables at the UC Davis Student Farm.</td>
  </tr>
</table>

<ol start="3">
  <li>Under Conditions of Access and Use, input the following:</li>
</ol>

<table>
  <thead>
    <th>Access Restrictions</th>
    <th>Copyright Status</th>
    <th class="w-1-3">Copyright Holder</th>
    <th>Copyright Determination Date</th>
    <th>Copyright Jurisdiction</th>
  </thead>
  <tr>
    <td>Public</td>
    <td>Copyrighted</td>
    <td>
      Name: UC Regents<br>
      Name Type: Corporate
    </td>
    <td>
      May 29, 2014
    </td>
    <td>US</td>
  </tr>
</table>

<table>
  <thead>
    <th>Copyright Statement</th>
  </thead>
  <tr>
    <td>
      Transmission or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user. 
    </td>
  </tr>
</table>

<table>
  <thead>
    <th>Copyright Contact</th>
  </thead>
  <tr>
    <td>
      University of California Office of the President Communications, External Relations. 1111 Franklin St., 12th Floor, Oakland, CA 94607. Phone: (510) 987-9200. Web: http://www.ucop.edu/communications/
    </td>
  </tr>
</table>

<ol start="4">
  <li>Scroll down to the bottom to press the 'Save' button.</li>
  <li>You should remain on the Summary tab of the object with the additional metadata fields filled in.</li>
</ol>

<div class="note">At any time, while in 'edit' mode on the 'Summary' tab, you can press the 'Cancel' button to cancel all changes.</div>
