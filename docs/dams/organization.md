---
layout: doc
title: Organizing Objects with Project Folders
next_section: dams/create-objects
prev_section: dams/index
permalink: /docs/dams/organization/
breadcrumbs: DAMS User Guide
---

## Project folders: a paradigm

Project folders are the building blocks for organizing digital objects in the shared DAMS. You might use project folders to define collections and other groupings of objects, as discussed in more detail below.

It is important to understand that the Nuxeo project folder is a purely internal construction, used to organize objects for management purposes, and _will have no bearing on how objects are displayed on Calisphere_ (once publication to Calisphere is enabled). Calisphere will support the grouping of objects into campuses, institutions (such as library departments), and collections--but these associations must be indicated in the item-level metadata for each object.

## Using project folders for collections
We anticipate that a common way of using project folders will be to organize digital objects into collections. Collections might be defined by provenance (as in the case of many archival collections), by topic, or by other characteristics determined by your library. We have demonstrated this use of the project folder with the existing collections we've pre-loaded into the DAMS. You'll notice that for each existing collection, we have created a project folder with the same name of the collection, and all of the digital objects in that collection are contained within the corresponding folder.

<div class="note">In order to show the association of objects with collections in Calisphere, be sure to add the requisite metadata to each object in the '<a href="{{ site.url }}{{ site.baseurl }}/docs/dams/metadata-model/#Collection" class="notelink">Collection</a>' and '<a href="{{ site.url }}{{ site.baseurl }}/docs/dams/metadata-model/#CampusUnit" class="notelink">Campus/Unit</a>' fields. In the future, we plan to enhance this field so you can pull this data directly from the Collection Registry.</div>

## Other use cases
Project folders don't necessarily have to represent collections. Here are a few other ways you might use them:

  - To define a workspace for a group of users on your staff that need limited access to a subset of objects. 
  - To organize objects by specific digitization projects or method of digitization. 
  - To organize objects by completeness of metadata, making it easier to identify and return to projects-in-process. 
  - To organize subsets of a collection for a specific project or staff member to work on.

In short, project folders are flexible in order to accomodate your workflows for creating and managing files and metadata.

## Project folder rules
Project folders can contain both objects and other project folders. Every object must be contained within one, and only one, project folder. In order to contain an object in more than one project folder, the object must be duplicated. The duplicate _does not_ link back to the original in any way, so changes made to the duplicate will not be made to the original, and vice versa. We do not recommend duplicating objects.

<div class="note">To view groups of objects stored in many folders, you can utilize the DAMS search capabilities to retrieve objects based on their metadata. Alternately, if you want to be able to group objects by characteristics not in their metadata, you can use <b>tags</b>, available on the <a href="{{ site.url }}{{ site.baseurl}}/docs/dams/edit-objects" class="notelink">summary tab</a> of an object or project folder.</div>

You can grant read and/or write privileges to project folders as needed.

## Create a project folder
From within your campus folder, you can create as many project folders (and nested project folders) as you need. To create a new project folder, navigate to your campus folder and press the 'New' button. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/2_UCOP-folder.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/2_UCOP-folder.png" alt="Screenshot of UCOP folder contents" style="width: 500px">
</a>
<br>(click to enlarge)

<div class="note">You'll notice that if you navigate to a campus folder for another campus, the 'New' button won't be present. That is because you have read-only access to other campus folders.</div>

<div class="walkthrough">Walkthrough</div>

To create a new project folder 

1. Navigate to your campus folder
2. Click on the 'Content' tab if it is not already selected by default, and press 'New'.
3. There is only one available document type for children of a campus folder - a project folder. Click 'Project Folder'. 
4. For the required 'Title' field, input your name followed by "-Sample Project Folder".
5. For the optional 'Description' field, input "A trial project folder for testing the features of the Nuxeo DAMS." 
6. Then press 'Create'. 

<p>You should then be directed to that project folder's page, with the 'Content' tab selected. In the hierarchy sidebar, you should see your sample project folder underneath your campus's folder.</p>
