---
layout: registry-doc
title: Metadata Harvesting Scheme and Crosswalk
permalink: /docs/registry/metadata-harvest/
breadcrumbs: Calisphere Admin Guide
---

All data harvested into the common index must adhere to the [UCLDC Metadata Harvesting Scheme and Crosswalk](https://docs.google.com/spreadsheets/d/1u2RE9PD0N9GkLQTFNJy3HiH9N5IbKDG52HjJ6JomC9I/edit#gid=265758929), which was adapted from the <a href="http://dp.la/info/wp-content/uploads/2013/04/DPLAMetadataPolicy.pdf">DPLA Metadata Application Profile.</a></p>

##Required Metadata
***
<p>The following table summarizes data elements that must be present in each metadata record for harvest into the UCLDC Common Index. Note that default values for <b>Type</b>, <b>Rights (Status)</b>, and <b>Rights (Statement)</b> can optionally be supplied and applied to individual metadata records at the time they are harvested, using the Registry:</p>


<table>
  <thead>
    <th><b>Element Label</b></th>
    <th><b>Property</b></th>
    <th><b>Summary</b></th>
    <th><b>Vocabulary Terms/Syntax</b></th>
    <th><b>Example</b></th>
  </thead>
  <tr>
    <td><b>Title</b></td>
    <td>dc:title</td>
    <td>Primary name given to the described resource.</td>
    <td></td>
    <td>Lee (Roger) Residence, Berkeley, CA, 1950 </td>
  </tr>
  <tr>
    <td><b>Type</b></td>
    <td>dc:type</td>
    <td>Nature or genre of source resource.</td>
    <td>Use DCMI Type Vocabulary (http://dublincore.org/documents/2000/07/11/dcmi-type-vocabulary/)</td>
    <td>image</td>
  </tr>
  <tr>
    <td><b>Rights (Status)</b></td>
    <td>dc:rights</td>
    <td>Information about rights held in and over described resource.</td>
    <td>Use PREMIS 2.3 values to denote rights status (with a corresponding rights statement): copyrighted, publicdomain, unknown</td>
    <td>copyrighted</td>
  </tr>
  <tr>
    <td><b>Rights (Statement)</b></td>
    <td>dc:rights</td>
    <td>The name of the rights holder of this digital representation if possible or for more general rights (and access) information.</td>
    <td></td>
    <td>Transmission or reproduction of materials protected by copyright beyond that allowed by fair use requires the written permission of the copyright owners. Works not in the public domain cannot be commercially exploited without permission of the copyright owner. Responsibility for any use rests exclusively with the user.</td>
  </tr>
  <tr>
    <td><b>Is Shown At (URL to object view)</b></td>
    <td>edm:isShownAt</td>
    <td>Unambiguous URL reference to digital object in its full information context.</td>
    <td></td>
    <td>https://library.ucsd.edu/dc/object/bb0035097z</td>
  </tr>
  <tr>
    <td><b>Object (URL to object view)</b></td>
    <td>edm:object</td>
    <td>The URL of a suitable source object in the best resolution available on the website of the Data Provider from which a preview could be generated for use in a portal.</td>
    <td></td>
    <td>http://library.ucsd.edu/dc/object/bb39601295/_2.jpg</td>
  </tr>
</table>