---
layout: doc
title: Creating Simple Objects
next_section: dams/complex-objects
prev_section: dams/organization
permalink: /create-objects/
---

#### Digital objects: some definitions

For the purposes of documentation, let's define "digital object": a digital object is a content file(s) and affiliated metadata record(s). Simple objects comprise one file and one metadata record. Complex objects comprise multiple files and even multiple metadata records which are "bundled" together; in the DAMS, they are objects with child-level components. We'll discuss [Complex Objects]({{ site.url }}{{ site.url }}/docs/dams/complex-objects/) more in a later section. 


#### Understanding document types

The Nuxeo DAMS allows you to create four different kinds of digital objects, called document types: 

- <b>Picture:</b> use for graphic objects/images
- <b>Video:</b> use for moving images
- <b>Audio:</b> use for sound recordings
- <b>File:</b> use for text and document formats

The document types vary in the type of content file you can upload (see <a href="http://doc.nuxeo.com/display/public/USERDOC/Supported+File+Formats" target="_blank">Supported File Formats - Nuxeo Documentation</a>), and the kinds of derivatives Nuxeo automatically creates. Nuxeo supports most common file types. 

Each document type can function as a complex object and can contain child-level components of any of the four document types. There is no limit on the number of components. Child-level components are viewable and orderable via the Summary tab of their parent-level object. Again, we'll talk more about complex objects later on, but for now it's just important to know that each of the document types can be used to create both simple and complex objects.

#### Metadata model

Each of these document types has the same metadata model. The [metadata model]() follows Dublin Core standards, and includes Descriptive, Technical, and Rights Information. Unicode is supported in metadata. 

<div class="walkthrough">Banana Slug Walkthrough</div>

#### Creating a New Simple Object

We'll start by creating a simple object using the Picture document type.

1. Download <a href="{{ site.url }}{{ site.baseurl }}/images/Medium_uc-davis-student-farm-49.jpg" download>this sample image</a> and put it somewhere easy-to-find on your computer
2. Navigate to the Banana Slug project folder within your campus folder. 
2. Click on the 'Content' tab if it is not already selected by default, and press 'New'.
3. Since our content file is an image, select the Picture document type. 
4. Fill out the Basic Information metadata fields with the following data: 

| Identifier          | Local Identifier | Title               | Alternative Title                | Type  |
|---------------------|------------------|---------------------|----------------------------------|-------|
| ark:/13030/c8w66nzb | 5585817          | Simple image object | UC Davis Student Farm photograph | Image |

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
  <li>Finally, upload the sample content file you downloaded earlier. Select 'Upload', find the file in your filesystem, and then press 'Open'.</li>
  <li>Scroll down and press 'Create'.</li>
</ol>

<p>You should then be directed to that object's page, with the 'Summary' tab selected, as shown in the below screenshot. In the hierarchy sidebar, you should see your new object underneath the Banana Slug folder. Under the metadata section of the Summary tab, you should see the metadata you inputted. The next section discusses editing objects in the DAMS.</p>

<a class="img-popup-tall" href="{{ site.url }}{{ site.baseurl }}/images/3_simple-object.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/3_simple-object.png" alt="Screenshot after logging in" style="width: 500px">
</a>
<br>(click to enlarge)

<div class="note">There are no required fields on an object page, meaning that metadata entry and content upload can happen in any order convenient to your workflow. You could create several objects and only upload their content files, and then go back through and input metadata. Or vice-versa: you could create several objects with complete metadata records, and as you digitize your content, upload the files to the appropriate objects.</div>
