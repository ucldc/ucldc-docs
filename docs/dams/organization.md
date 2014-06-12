---
layout: doc
title: Organizational Paradigms for Managing Objects
next_section: dams/create-objects
prev_section: dams/index
permalink: /organization/
---

## Project Folders

Projects folders are for your own internal organizational and access restriction needs. They can be used to encapsulate objects and other project folders, and you can grant read and write privileges to project folders as needed. Every object must be contained within one, and only one, project folder.

<div class="note">In order to contain an object in more than one project folder, the object must be duplicated. The duplicate <b>does not</b> link back to the original in any way, so changes made to the duplicate will not be made to the original, and vice versa. We strongly advise using <a href="">tags</a> to organize your objects in multiple categories.</div>

#### Project folders can be used for a wide range of use cases:

  - To organize digital objects by collection. For collections we have loaded into the DAMS, each object in a collection is encapsulated in a project folder of the same name as the collection. 
  - To define a particular workspace for a group of users with limited access rights to a subset of digital objects. 
  - For organizing objects by specific digitization projects. 
  - For organizing digital objects by particular subsets of a collection that have been digitized. 
  - For organizing digital objects by completeness of metadata records in the DAMS or method of digitization. 
  - For organizing subsets of a collection for a specific project or staff member.
  
<div class="note">A folder does not necessarily have to encapsulate a particular collection - for example, an archival collection defined by provenance, or a curated collection where materials are related by topic or other valence. The Nuxeo DAMS are used for object-level metadata entry, so what <i>really</i> matters in publishing a collection to Calisphere, or preserving a collection in Merritt, is that the <a href="" class="notelink">'Collection/Unit'</a> field and access restriction fields in an object's metadata record are filled out accurately.</div>

From within your campus' folder, you can create as many project folders (and nested project folders) as you need. In order to create new project folders, navigate to your campus' folder, and press the 'New' button. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/2_UCOP-folder.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/2_UCOP-folder.png" alt="Screenshot of UCOP folder contents" style="width: 500px">
</a>
<br>(click to enlarge)

<div class="note">You'll notice if you navigate to another campus' folder, the 'New' button won't be present. That is because you have read-only access to other campus' folders.</div>

<div class="walkthrough">Banana Slug Walkthrough</div>

To create a new project folder 

1. Navigate to your campus's folder
2. Click on the 'Content' tab if it is not already selected by default, and press 'New'.
3. There is only one available document type for children of a campus' folder - a project folder. Click 'Project Folder'. 
4. For the required 'Title' field, input "Banana Slug".
5. For the optional 'Description' field, input "A trial project folder for testing the features of the Banana Slug release." 
6. Then press 'Create'. 

<p>You should then be directed to that project folder's page, with the 'Content' tab selected. In the hierarchy sidebar, you should see 'Banana Slug' underneath your campus' folder.</p>

## Tags

In order to organize your digital objects in multiple categories, you can create tags and add them to your objects via their [Summary Tab](). 