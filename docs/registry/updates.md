---
layout: registry-doc
title: Making Updates
next_section: registry/access
prev_section: registry/q-a
permalink: /docs/registry/updates/
breadcrumbs: Calisphere Admin Guide
---
Digital collections evolve; items are added and deleted and metadata changes. Our aim is to reflect local changes to your collections as quickly as possible in the UCLDC platform.

Updates to any data in a given collection--even for a single object--are handled through re-harvesting the complete collection. Collection Administrators should simply [contact us](mailto:ucldc@ucop.edu) in order to initiate a re-harvest. (Eventually, we plan to support a more self-serve, automated process wherein Collection Administrators can initiate a re-harvest directly through the Collection Registry).

At this time, any re-harvested collection will directly replace the previously-harvested version of the collection. We will maintain the same Calisphere BETA URL for an object that is re-harvested, as long as the metadata record for that object maintains the same local identifier (mapped to the "Identifier" or "Local Identifier" fields in <a href="https://registry.cdlib.org/documentation/docs/dams/metadata-model/">Nuxeo</a>; or alternatively mapped to the Common Index's "Identifier" element, if the metadata is provided from a <a href="https://registry.cdlib.org/documentation/docs/dams/metadata-model/">different harvesting source</a>).

<div class="note"><p>"How often do you harvest?" Currently, harvest is on-request. That is, we will harvest (or re-harvest) a given collection only when expressly notified by a Collection Administrator. However, eventually--and if there is interest--we could potentially set up a scheduled, periodic harvest of collections.</p></div>

##Takedown requests
In cases where an institution needs to immediately remove metadata for a given object--for example, to comply with a copyright-related takedown request--Collection Administrators should contact us. We will remove the metadata from the Common Index (and subsequently, remove it from Calisphere) in a timely manner. We will also work with DPLA to do the same.
