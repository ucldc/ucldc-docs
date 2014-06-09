---
layout: doc
title: Creating Objects in the DAMS
next_section: dams/edit-objects
prev_section: dams/organization
permalink: /create-objects/
---

The Nuxeo DAMS allows you to create objects of four different document types: 

- Picture
- File
- Video 
- Audio

For the purpose of this documentation an object is a content file and its affiliated metadata record. Each of these document types have the same metadata model. The [metadata model]() follows Dublin Core standards, and includes Descriptive, Technical, and Rights Information. Unicode is supported in metadata. 

The document types vary in the type of content file you can upload ([Supported File Formats - Nuxeo Documentation](http://doc.nuxeo.com/display/public/USERDOC/Supported+File+Formats)), and the kinds of derivatives Nuxeo automatically creates. Most common filetypes are supported. 

Each document type can contain sub-objects of any of the four document types. There is no limit on the number of child objects. Child objects are viewable and orderable via the Summary tab of their parent object. 

<div class="walkthrough">Banana Slug Walkthrough</div>

#### Creating a New Object

We'll start by creating a picture object. A sample image is available [here]({{ site.url }}{{ site.baseurl }}/images/Medium_uc-davis-student-farm-49.jpg), and some basic metadata is available below:

| Identifier          | Local Identifier | Title               | Alternative Title                | Type  |
|---------------------|------------------|---------------------|----------------------------------|-------|
| ark:/13030/c8w66nzb | 5585817          | Simple image object | UC Davis Student Farm photograph | Image |

1. Navigate to the Banana Slug project folder within your campus' folder. 
2. Click on the 'Content' tab if it is not already selected by default, and press 'New'.
3. Since our content file is an image, select the Picture document type. 
4. Fill out the Basic Information metadata fields with the above data. 

<div class="note"><p><b>Local Identifier</b> and <b>Alternative Title</b> are both repeatable fields, meaning there can be multiple per object. Press the plus button to add a Local Identifier and an Alternative Title.</p><p><b>Date</b> and <b>Creator</b> are both repeatable groups of fields, these are denoted by a light grey border. Press the plus button to see the fields in a group.</p></div>

<ol start="5">
  <li>Add the date and creator data to the object:</li>
</ol>

<table>
  <thead>
    <tr>
      <th class="w-1-3">Date</th>
      <th>Creator</th>
    </tr>
  </thead>
  <tr>
    <td>
      Date: 2011 October 3<br>
      Date Type: Created<br>
      Single: 2011-10-03
    </td>
    <td>
      Creator Name: University of California Office of the President Communications
      Name Type: Corporation
    </td>
  </tr>
</table>

<ol start="6">
  <li>Finally, upload the content file. Press 'Choose File', find the file in your filesystem, and then press 'Open'.</li>
  <li>Press 'Create'.</li>
</ol>

<p>You should then be directed to that object's page, with the 'Summary' tab selected, as shown in the below screenshot. In the hierarchy sidebar, you should see your new object underneath the Banana Slug folder. Under the metadata section of the Summary tab, you should see the metadata you inputted. The next section discusses editing objects in the DAMS.</p>

<div class="note">There are no required fields on an object page, meaning that metadata entry and content upload can happen in any order convenient to your workflow. You could create a bunch of objects and only upload their content files, and then go back through and input metadata. Or vice-versa: you could create a bunch of objects with complete metadata records, and as you digitize your content, upload the files to the appropriate objects.</div>