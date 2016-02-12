---
title: Getting Stats
prev_section: registry/access
---

## Usage Stats
We are using Google Analytics for tracking usage of objects on the new Calisphere beta site.

##What's supported
We are able to support contributor statistics through Google Analytics as follows:

+ Filtering usage data by institution (e.g. library department), within a given report. Data is collected on each institution's digital objects, collection landing pages, and institution landing pages.
+ Filtering usage data by collection, within a given report.

CDL does not plan to engineer any custom events for content owners’ usage reports, unless this is surfaced as a need. This means that the typical (but extensive!) suite of usage data from Google Analytics will be reported in the areas of Audience, Acquisition, and Behavior. Please let us know if you have additional requirements and we will try to accommodate them.

##How to set up stats
In order to collect usage statistics, the UCLDC Collection Administrator or other designated staff member at your institution will need to complete 4 steps.

1. Create a new Google Analytics property for Calisphere BETA
2. Provie CDL with your property's tracker ID
3. Tell us which institutions should have the tracker ID applied
4. Create "custom dimensions" for collections and institutions
 
These steps are described in more detail below.

###1. Create a new Google Analytics "property" for Calisphere BETA

A new property in Google Analytics correlates to a new report. We highly recommend that you "start fresh" and create a new property for Calisphere BETA, so your stats on your content in Calisphere BETA are separate from your stats on other sites. To learn how to set up a new property, [read the instructions here.](https://support.google.com/analytics/answer/1042508?hl=en&vid=1-635768324944661236-1858192804) The URL for your new property should be http://calisphere.cdlib.org. Note that you will automatically create a new property if you choose to create a whole separate account.

###2. Provide CDL with your property's tracker ID

A Google Analytics tracker ID will be generated when you create a new property and click "get tracker ID." The tracker ID will be a 9-character string beginning with the letters "UA." Please copy this tracker ID and send it to us at [ucldc@ucop.edu](mailto:ucldc@ucop.edu). We will place it in the Collection Registry, on the institutions to which it should apply (see next bullet).

###3. Tell us which institutions should have the tracker ID applied

We need to know to what institution(s) the tracker ID should be applied. Please send this information with the tracker ID.

In making this decision, it is best to remember that one tracker ID correlates with one report in Google Analytics. Do you want to get stats for multiple institutions (for example different library departments) within a single report? If so, you should tell us to apply that one tracker ID to those institutions. Do you have some institutions on campus (e.g. a museum or affiliated library) that will want its own, separate report? In those cases, separate tracker IDs should be created and then applied to the different institutions.

###4. Create "custom dimensions" for collections and institutions

This last step is very important for allowing you to filter your Calisphere BETA stats by collection and institution.

You will need to create something called "custom dimensions" in your property. Google Analytics has laid this out very nicely in [this help documentation](https://support.google.com/analytics/answer/2709829?vid=1-635766362504332403-2648225428). Follow the eight steps under "Set up custom dimensions," first for collections. When you get to Step 5, name the dimension "collections." Then, if you have applied this tracker ID to multiple institutions, go through the steps one more time. This time, name your dimension "institutions." **Please note that it is important that you create your dimensions in this order: dimension 1 should be collections, and dimension 2 should be institutions. This matches the code we have engineered on our side and will ensure your data comes through.**

##How to view your stats
Now comes the exciting part: getting your data!

###Filter by collection/institution

To filter by collection and/or institution, you'll be making use of something called "custom dimensions." Dimensions are really just "things you can filter on," and these happen to be custom because you created them back in setup step #4. [Read more about dimensions here.](https://support.google.com/analytics/answer/1033861?vid=1-635768343290685965-123999013) You can make use of your custom dimensions anytime you're given the option in your report, but a particularly handy one is in the "site content" view:

- Using the left-side navigation, click on Behavior to expand your report options
- Click on Site Content
- Click on All Pages
- In the table in the bottom half of the report, find the button called "Secondary Dimension"
- Click on "Custom Dimension"
- Click on "collections" or "institutions" 

You should now see all of the collections and/or institutions with which a given page is affiliated. You can then do fancy things like sort your pages by collection (click on the "collections" or "institutions" column), or create an advanced filter using a collection name to see all your stats for a given collection (click on the "advanced" link next to the magnifying glass on the right side).

###Additional stats support

Generally speaking, we will not be providing additional support in navigating and interpreting your usage reports, as Google Analytics already provides [extensive help documentation](https://support.google.com/analytics?vid=1-635768324944661236-1858192804#topic=3544906). That said, we are happy to consult to the extent we can, especially if need more information about Calisphere BETA in order to understand your stats. Please feel free to contact us.


## Extent Stats

Extent statistics for the number of objects published in Calisphere are available at <a href="https://voro.cdlib.org/calisphere.org/">https://voro.cdlib.org/calisphere.org/</a>. 
