---
layout: doc
title: Organizing Objects with Project Folders
next_section: dams/create-objects
prev_section: dams/index
permalink: /organization/
---

### Project folders

Our shared DAMS makes heavy use of something called project folders. Project folders are the building blocks for organizing digital objects in the DAMS.

We anticipate that a common way of using folders will be to organize digital objects into collections. Collections might be defined by provenance (as in the case of many archival collections), by topic, or by other characteristics determined by your library. We have demonstrated this use of the project folder with the existing collections we've pre-loaded into the DAMS. You'll notice that for each existing collection, we have created a project folder with the same name of the collection, and all of the digital objects in that collection are contained within the corresponding folder.

<div class="note">It is important to understand that the Nuxeo project folder is a purely internal construction--meaning creating a collection-level project folder will not alone translate to the display of a collection on Calisphere (once publication to Calisphere is enabled). In order to associate objects with collections in the public interface, you must add the requisite metadata to <i>each object</i> in the <a href="" class="notelink">'Collection/Unit'</a> field.</div>

### Beyond collections: other use cases
As explained in the info box above, the organization of objects into project folders within the DAMS is a separate construct from how objects will appear to be organized on Calisphere. What this means is that project folders don't necessarily have to represent collections. In fact, you might use them to internally organize and access objects within the DAMS in ways that may differ from how you want end-users to view them on the web.

Here are a few ways that you might use project folders, beyond defining collections:

  - To define a workspace for a group of users on your staff that need limited access to a subset of objects. 
  - To organize objects by specific digitization projects or method of digitization. 
  - To organize objects by completeness of metadata, making it easier to identify and return to projects-in-process. 
  - To organize subsets of a collection for a specific project or staff member to work on.

In short, project folders are flexible in order to accomodate your workflows for creating and managing files and metadata.

### Project folder rules
Project folders can contain both objects and other project folders. Every object must be contained within one, and only one, project folder.

As you might have suspected from reading through the above use cases, you can grant read and/or write privileges to project folders as needed.

<div class="note">In order to contain an object in more than one project folder, the object must be duplicated. The duplicate <b>does not</b> link back to the original in any way, so changes made to the duplicate will not be made to the original, and vice versa. In order to view groups of similar objects that are contained in disparate folders, we strongly recommend utilizing the DAMS search capabilities to retrieve objects based on their metadata. Alternately, if you want to retrieve like objects that do not have common metadata, you can use <b>tags</b>, available on the <a href="{{ site.url }}{{ site.baseurl}}/docs/dams/edit-objects" class="notelink">summary tab</a> of an object or project folder.</div>

### Create a project folder
From within your campus folder, you can create as many project folders (and nested project folders) as you need. To create a new project folder, navigate to your campus folder and press the 'New' button. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/2_UCOP-folder.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/2_UCOP-folder.png" alt="Screenshot of UCOP folder contents" style="width: 500px">
</a>
<br>(click to enlarge)

<div class="note">You'll notice that if you navigate to a campus folder for another campus, the 'New' button won't be present. That is because you have read-only access to other campus folders.</div>

<div class="walkthrough">Banana Slug Features Walkthrough</div>

To create a new project folder 

1. Navigate to your campus folder
2. Click on the 'Content' tab if it is not already selected by default, and press 'New'.
3. There is only one available document type for children of a campus folder - a project folder. Click 'Project Folder'. 
4. For the required 'Title' field, input "Banana Slug".
5. For the optional 'Description' field, input "A trial project folder for testing the features of the Banana Slug release." 
6. Then press 'Create'. 

<p>You should then be directed to that project folder's page, with the 'Content' tab selected. In the hierarchy sidebar, you should see 'Banana Slug' underneath your campus's folder.</p>
