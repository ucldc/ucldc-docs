---
layout: doc
title: Creating a Simple Object
next_section: dams/complex-objects
prev_section: dams/organization
permalink: /create-objects/
---

The Nuxeo DAMS allows you to create objects of four different document types of digital objects: 

- Picture: use for graphic image-based objects (JPG, PNG, GIF, JPG2000, TIF, etc.)
- File: use for moving images (OGG, AVI, MP4, FLV, etc.)
- Audio: use for sound recordings (MP3, WAV, M4A, etc.)
- File: use for text and other document formats (PDF, RTF, etc.)

For the purpose of this documentation an object is a content file and its affiliated metadata record. Each of these document types has the same metadata model. The [metadata model]() follows Dublin Core standards, and includes Descriptive, Technical, and Rights Information. Unicode is supported in metadata. 

The document types vary in the type of content file you can upload (<a href="http://doc.nuxeo.com/display/public/USERDOC/Supported+File+Formats" target="_blank"> Supported File Formats - Nuxeo Documentation</a>), and the kinds of derivatives Nuxeo automatically creates. Most common file types are supported. 

Each document type can function as a complex object and can contain child-level components of any of the four document types. There is no limit on the number of components. Child-level components are viewable and orderable via the Summary tab of their parent-level object. 

In the documentation, we'll use Simple Object to refer to objects that are just a single content file and metadata record and Complex Object to refer to objects that have child-level components. We'll discuss [Complex Objects]({{ site.url }}{{ site.url }}/docs/dams/complex-objects/) more in the next section. 

<div class="walkthrough">Banana Slug Walkthrough</div>

#### Creating a New Simple Object

We'll start by creating a simple object using the Picture document type. A sample image is available <a href="{{ site.url }}{{ site.baseurl }}/images/Medium_uc-davis-student-farm-49.jpg" download>here</a>, and some basic metadata is available below:

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

<a class="img-popup-tall" href="{{ site.url }}{{ site.baseurl }}/images/3_simple-object.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/3_simple-object.png" alt="Screenshot after logging in" style="width: 500px">
</a>
<br>(click to enlarge)

<div class="note">There are no required fields on an object page, meaning that metadata entry and content upload can happen in any order convenient to your workflow. You could create a bunch of objects and only upload their content files, and then go back through and input metadata. Or vice-versa: you could create a bunch of objects with complete metadata records, and as you digitize your content, upload the files to the appropriate objects.</div>