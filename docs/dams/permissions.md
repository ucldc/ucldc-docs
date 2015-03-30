---
layout: dams-doc
title: Setting User Permissions
next_section: dams/delete/
prev_section: dams/search/
permalink: /docs/dams/permissions/
breadcrumbs: DAMS User Guide
---

## Manage Tab

The manage tab of an object or project folder enables users with management rights to set and modify user permissions for that object or project folder. For any given user or user group, a user with management rights can grant or deny 'Read', 'Write', 'Remove', and 'Manage everything' permissions. Users without management rights for a given object or project folder will not see the 'manage' tab. 

- Read: users can view and download metadata and content files, copy objects to a project folder they own, and add objects to their worklist. You can experiment with what read permissions allow you to do by looking at the contents of any campus folder other than your own. For users denied read privileges on an object or project folder, it will appear as though that object or project folder does not exist. 
- Write: users have read privileges, and can create, edit, and delete objects and project folders. Users denied write privileges cannot create, edit, or delete objects or projects folders. 
- Remove: users with remove permissions on an object or project folder can delete that object or project folder. Users denied remove permissions cannot delete that object or project folder. 
- Manage everything: users have write privileges and have management rights on an object or project folder. 

<div class="note">The remove permission is mainly intended to be denied, so as to restrict the actions available to users with write permissions.</div>

On the manage tab, there are two ways permissions are defined: inherited permissions and local permissions. Local permissions have priority over inherited permissions, and granted permissions have priority over denied permissions. We'll be referring to the screenshot below in the following sections on permissions inheritance and local rights. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/perms1.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/perms1-cropped.png" alt="Bobcat Project Folder - Manage Tab" style="width: 500px">
</a>
<br>(click to enlarge)

## Permissions Inheritance

Permissions are inherited down the project folder hierarchy. Anyone with permissions for a given campus folder, project folder, or object will automatically get those same permissions for all child project folders and objects. Unless otherwise specified when the account is requested, all new users of the DAMS are created with read-only permissions. Each campus has a DAMS user with manage everything permissions at the campus folder level that will grant user permissions on that campus as necessary. 

In the above screenshot you can see that the Administrator user has full rights, and the Members group has read-only rights on the Bobcat project folder. Since these rights are inherited, we know that the Administrator user has full rights on the UCOP campus folder as well, while the Members group has read-only permissions on the UCOP campus folder. Furthermore, all project folders and objects within the Bobcat project folder will inherit these same rights.

<div class="note">You can block inherited permissions on a project folder or object by selecting the checkbox 'block permissions inheritance'. The project folder or object, and all child project folders and objects, will cease to inherit permissions specified higher up in the hierarchy. Any local rights you specify, however, will continue to be inherited by child objects and project folders. Since all users have read-only permissions to all objects and project folders in the DAMS, a project folder that contains objects that shouldn't be read by users other than ones specified is a good candidate for blocking permissions inheritance.</div>

## Local Rights

Local rights are defined on a project folder or object on top of any inherited rights. When a user wants to begin working in the DAMS, the DAMS user with manage rights for that campus must define local rights on the relevant campus folder, project folders, or objects. 

In the above screenshot the administrator has granted local rights to just the Bobcat project folder, so that specific members of the Members group have not just read permissions (defined via permissions inheritance), but also write permissions. These users will have write permissions on all project folders and objects created within the Bobcat project folder due to permissions inheritance. 

To grant or deny permissions, begin typing a username or group name in the autocomplete box under 'Add a new security rule'. Select the action (grant or deny), and the permission level (read, write, delete, manage everything), and then press 'Add permission'. Permissions are not saved until you press the 'Save local rights' button, so you can continue adding permissions for other users in this way. When you are ready to save your changes, press 'Save local rights'.

<div class="note">While the remove permission is intended to be denied so as to restrict users with write permissions, granted permissions have precedence over denied permissions, so a user granted write permissions on the Bobcat project folder but denied remove permissions on the Bobcat project folder <b>will</b> be able to delete objects in the Bobcat project folder. The <i>granted</i> write permission - which includes the ability to delete objects, overwrites the <i>denied</i> remove permission. Local permissions have precedence over inherited permissions, however, so to restrict a user with write permissions on the Bobcat project folder, create a Bobcat (Protected) project folder within the Bobcat project folder, and locally deny remove permissions on the Bobcat (Protected) project folder.</div>

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/perms2.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/perms2.png" alt="Bobcat (Protected) Project Folder - Manage Tab" style="width: 500px">
</a>
<br>(click to enlarge)
