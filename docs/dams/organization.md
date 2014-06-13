---
layout: doc
title: Organizational Paradigms for Managing Objects
next_section: dams/create-objects
prev_section: dams/index
permalink: /organization/
---

## Project Folders

Projects folders are the building blocks for organizing digital objects in the DAMS, based on your own internal needs for organizing and accessing objects--as distinct from how these objects appear in the public interface or in Merritt.

Project folders can contain both objects and other project folders, and you can grant read and/or write privileges to them as needed. Every object must be contained within one, and only one, project folder.

<div class="note">In order to contain an object in more than one project folder, the object must be duplicated. The duplicate <b>does not</b> link back to the original in any way, so changes made to the duplicate will not be made to the original, and vice versa. We strongly advise using <a href="">tags</a> to represent the association of your objects within multiple groups or categories.</div>

#### Project folders are flexible.
They can be used for a wide range of use cases, for example:

  - To organize digital objects by collection -- for example, an archival collection defined by provenance, or a curated collection where materials are related by topic.
    Note: for collections we have already loaded into the DAMS, each object is contained in a project folder of the same      name as the collection. 
  - To define a workspace for a group of users on your campus that need limited access to a subset of objects. 
  - To organize objects by specific digitization projects, or method of digitization. 
  - To organize objects by completeness of metadata, to make it easier to identify and return to projects-in-process. 
  - To organize subsets of a collection for a specific project or staff member to work on.
  
<div class="note">A folder does not necessarily have to contain or represent a particular collection. The Nuxeo DAMS is used for object-level metadata entry, so what <i>really</i> matters in publishing a collection to Calisphere, or preserving a collection in Merritt, is that the <a href="" class="notelink">'Collection/Unit'</a> field and access restriction fields in an object's metadata record are filled out accurately.</div>

From within your campus' folder, you can create as many project folders (and nested project folders) as you need. To create new project folders, navigate to your campus folder and press the 'New' button. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/3_UCOP-folder.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/3_UCOP-folder.png" alt="Screenshot of UCOP folder contents" style="width: 500px">
</a>
<br>(click to enlarge)

<div class="note">You'll notice that if you navigate to a campus folder for another campus, the 'New' button won't be present. That is because you have read-only access to other campus folders.</div>

<div class="walkthrough">Banana Slug Walkthrough</div>

To create a new project folder 

1. Navigate to your campus folder
2. Click on the 'Content' tab if it is not already selected by default, and press 'New'.
3. There is only one available document type for children of a campus folder - a project folder. Click 'Project Folder'. 
4. For the required 'Title' field, input "Banana Slug".
5. For the optional 'Description' field, input "A trial project folder for testing the features of the Banana Slug release." 
6. Then press 'Create'. 

<p>You should then be directed to that project folder's page, with the 'Content' tab selected. In the hierarchy sidebar, you should see 'Banana Slug' underneath your campus folder.</p>

## Tags

In order to organize your digital objects in multiple categories, you can create tags and add them to your objects via their [Summary Tab](). 


<!---
### Project Folder Access Restrictions & The Other Tabs
--->
