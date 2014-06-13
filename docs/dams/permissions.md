---
layout: doc
title: Project Folder Access Restrictions & Other Tabs
next_section: 
prev_section: dams/edit-objects/
permalink: /permissions/
---

Now that we have a sample project folder with some content, let's return to the Project Folder to take a closer look at its Content, Manage, and other tabs: 

## Content Tab

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/banana-slug-content.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/banana-slug-content.png" alt="Banana Slug Project Folder - Content Tab" style="width: 500px">
</a>
<br>(click to enlarge)

The content tab lists the contents of a project folder. From here you can create new objects in your project folder, filter the project folder contents by title, and select objects to copy, paste, delete, or add to your worklist. 

- Filtering: Filtering only works on the current contents of the project folder - it does not traverse the hierarchy. Press on the ellipsis next to the filter button to additionally filter by modification date. 
- Copy/Paste: Select the checkbox next to the items you'd like to copy and press the 'Copy' button. In the sidebar, select 'Clipboard' to see the objects you've selected to copy. Navigate to another project folder's content tab, and select 'Paste'. 
- Add to Worklist: The Worklist is a persistent, user-specific list displayed in the bottom part of the sidebar. Use this to keep track of objects you're currently working on.

## Summary Tab

A project folder's summary tab reveals common folder metadata such as Created and Modified dates, and Author, Contributor, and Last Contributor user information. On the summary tab, you can also add a tag to the project folder. 

<div class="note">Like on an object's summary tab, The State and Workflow Process are also included here. These are built-in Nuxeo features we see as potentially useful, though we haven't fully built out their functionality just yet. For now, you can mostly ignore those sections, but they may provide useful functionality in future releases.</div>

## Manage Tab

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/ucop-manage-tab.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/ucop-manage-tab.png" alt="UCOP Campus Folder - Manage Tab" style="width: 500px">
</a>
<br>(click to enlarge)

<div class="note">In the above screenshot, I've used the UCOP folder rather than the Banana Slug folder to provide a more robust example of permissions.</div>

The manage tab enables users with management rights to set and modify user permissions for that project folder. For any given user or user group, a user with management rights can grant or deny 'Read', 'Write', 'Remove', and 'Manage everything' permissions. 

- Read: users can view and download metadata and content files, copy objects to a project folder they own, and add objects to their worklist. Experiment with what read permissions allow you to do by looking at the contents of a different campus folder than your own. 
- Write: users have read privileges, and can create, edit, and delete metadata and upload content files.
- Delete: users denied this permission cannot delete objects or project folders. 
- Manage everything: users have write privileges and have management privileges on a project folder. 

### Permissions Inheritance

Permissions are inherited down the hierarchy. Anyone that has permissions for a parent-level folder automatically gets permissions for a child-level folder when it is created. When you create a new project folder within your campus folder other users from your campus can manage everything, while users from other campuses have read-only rights. This happens automatically, without you having to specify any rights for that project folder. 

You can see in the above screenshot that the Administrator user has full rights, and the Members group has read-only permissions on the UCOP folder. Since these rights are inherited, we know that the Administrator user has full rights on the Asset Library as well, and the Members group has read-only permissions on the Asset Library. 

### Local Rights

The administrator has granted local rights to just the UCOP folder, as well, so that specific members of the Members group have not just read permissions, but manage everything permissions. These users will have manage everything permissions on all project folders created within the UCOP campus folder due to permissions inheritance. 

To grant or deny permissions, begin typing a username or group name in the autocomplete box under 'Add a new security rule'. Select the action (grant or deny), and the permission level (read, write, delete, manage everything), and then press 'Add permission'. Permissions are not saved until you press the 'Save local rights' button, so you can continue adding permissions for other users in this way. When you are ready to save your changes, press 'Save local rights'.

### Blocking Inherited Permissions

You can block inherited permissions by selecting the checkbox 'block permissions inheritance'. That folder, and all children-level folders, will cease to inherit permissions specified higher up in the hierarchy. Any local rights you specify, however, will continue to be inherited by child-level objects and project folders. Since all users have read-only permissions to all objects and project folders in the DAMS, a project folder that contains objects that shouldn't be read by users other than the ones specified is a good candidate for blocking permissions inheritance. 