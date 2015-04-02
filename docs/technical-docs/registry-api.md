---
layout: technical-doc 
title: Regsitry API 
prev_section: technical-docs/index/
permalink: /docs/technical-docs/registry-api/
breadcrumbs: Registry API
---

The Collection Registry has a [HATEOAS](http://en.wikipedia.org/wiki/HATEOAS) API powered by [Tasty Pie](http://tastypieapi.org)

HATEOAS APIs attempt to be self describing.  All available endpoints may be discovered from the base URL: https://registry.cdlib.org/api/v1/

```bash
curl --silent "https://registry.cdlib.org/api/v1/?format=json" | jq .
```

```json
{
  "repository": {
    "schema": "/api/v1/repository/schema/",
    "list_endpoint": "/api/v1/repository/"
  },
  "collection": {
    "schema": "/api/v1/collection/schema/",
    "list_endpoint": "/api/v1/collection/"
  },
  "campus": {
    "schema": "/api/v1/campus/schema/",
    "list_endpoint": "/api/v1/campus/"
  }
}
```

The API is configured in django in [this file](https://github.com/ucldc/avram/blob/master/library_collection/api.py)
