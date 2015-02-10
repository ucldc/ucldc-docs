---
layout: doc
title: DAMS Overview
next_section: dams/organization
permalink: /docs/dams/index/
breadcrumbs: DAMS User Guide
---

## What is the DAMS?
The digital asset management system (or DAMS) is a tool for creating and managing object-level metadata and content files. You can use it to build out digital objects (such as images, texts, audio, and video), create metadata, and upload content files. Our shared DAMS for the UC Libraries is a customized implementation of [Nuxeo](http://www.nuxeo.com/), a platform that is used by a variety of organizations--from media companies to the U.S. Navy--for their content management needs.

The DAMS will also provide workflows for publishing digital objects to Calisphere for public access and depositing them in Merritt for preservation. These features will be rolled out at a later date.

<div class="walkthrough new">New in Bruin</div>

In our most recent release, named after UCLA's bruin, we primarily upgraded the underlying Nuxeo software from version 5.8 to version 6. This upgrade included a refreshed UI, an 'Import' button, and a [spreadsheet-style editor]({{ site.url }}{{ site.baseurl }}/docs/dams/spreadsheet-view/).  

## Getting in
You need an account to access the DAMS. If you have an account already, use your Single Sign-On account to login at [https://nuxeo.cdlib.org/nuxeo/](https://nuxeo.cdlib.org/nuxeo/). If you do not already have an account, please [create one]({{ site.url }}{{ site.baseurl }}/docs/create-account/).

## Navigation
Upon logging in to the DAMS, you will see a screen that looks like this: 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/1_on-login.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/1_on-login.png" alt="Screenshot after logging in" style="width: 500px">
</a>
<br>(click to enlarge)

The first thing you'll notice is that the DAMS is organized hierarchically. We are at the root of the hierarchy, looking at a list of its contents. From here, click on 'Asset Library' to navigate to the spaces where we will be creating and managing objects in the DAMS.

Now you should see a list of all 10 campuses (plus UCOP). These are <b>campus folders</b>, which are the spaces where we'll be getting to work.

Navigate to your campus folder. You may see a list of project folders, named for collections that we have pre-loaded into the DAMS. (We'll talk more about [project folders]({{ site.url }}{{ site.baseurl }}/docs/dams/organization/) in the next section.) Notice how the sidebar reflects where you are in the hierarchy. Feel free to explore the folders of your campus and those of the other campuses. 

<a class="img-popup" href="{{ site.url }}{{ site.baseurl }}/images/asset-library.png">
  <img src="{{ site.url }}{{ site.baseurl }}/images/asset-library.png" alt="Screenshot after logging in" style="width: 500px">
</a>
<br>(click to enlarge)

## The DAMS interface
Take a moment to familiarize yourself with the DAMS interface. Here are some of its key elements:

- Navigation Bar
  - Home: use this to return to the default landing page for the DAMS.
  - Workspace: this is the primary, functional area of the DAMS for creating and managing digital objects.
  - Search: this is the search module of the DAMS and is discussed further in the [search]({{ site.url }}{{ site.baseurl }}/docs/dams/search/) documentation. 
- Sidebar
  - Digital objects within the DAMS are hierarchically organized. By default, the sidebar displays this hierarchy.
- Current object or project folder and its tabs: These tabs change depending on the kind of object or folder you are viewing and will be discussed in subsequent sections for [project folders]({{ site.url }}{{ site.baseurl }}/docs/dams/organization/) and [objects]({{ site.url }}{{ site.baseurl }}/docs/dams/edit-objects/).

You'll notice there are other elements of the interface we have not mentioned, and this is because we have not yet customized them fully. You can feel free to explore these features as well, but just be advised they might not work perfectly right now.
