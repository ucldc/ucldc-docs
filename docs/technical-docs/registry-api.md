---
layout: technical-doc 
title: Collection Registry API 
prev_section: technical-docs/index/
permalink: /docs/technical-docs/registry-api/
breadcrumbs: Registry API
---

The Collection Registry has a [HATEOAS](http://en.wikipedia.org/wiki/HATEOAS) API powered by [Tasty Pie](http://tastypieapi.org).

HATEOAS APIs attempt to be self describing.  All available endpoints may be discovered from the base URL.

## Format
  The following formats are supported: ['json', 'jsonp', 'xml', 'yaml', 'plist']

## Base 
 * https://registry.cdlib.org/api/v1/?format=json

## Respostiry
 * https://registry.cdlib.org/api/v1/repository/?format=json
   * https://registry.cdlib.org/api/v1/repository/schema/?format=json

## Collection
 * https://registry.cdlib.org/api/v1/collection/?format=json
   * https://registry.cdlib.org/api/v1/collection/schema/?format=json

## Campus
  * https://registry.cdlib.org/api/v1/campus/?format=json
    *  https://registry.cdlib.org/api/v1/campus/schema/?format=json

## Institution JSON
  * join `http://dsc.cdlib.org/institution-json/` with the `"ark":` (no trailing slash) in Repository or Campus to get address, phone number, email etc. from the voro dashboard.

The API is configured in django in [this file](https://github.com/ucldc/avram/blob/master/library_collection/api.py).
