---
title: Nuxeo API 
prev_section: technical/index/
---

*See also the [Nuxeo documentation for more information on the Nuxeo REST API](http://doc.nuxeo.com/display/NXDOC/REST+API).*

## UCLDC Code using the Nuxeo APIs

 * [pynux](https://github.com/ucldc/pynux) Python wrapper for REST API
 * [nuxeo uploader](https://github.com/ucldc/nuxeo_uploader) Desktop bulk uploader uses [Nuxeo's javascript client](https://github.com/nuxeo/nuxeo-js-client)
 * [scripts for ETL loading](https://github.com/ucldc/nuxeo-load)
 * [Merritt Atom Feed](https://github.com/ucldc/ucldc-merritt)
 * UCSC's [NuxeoLink](https://github.com/UCSCLibrary/NuxeoLink) Omeka plugin

## Authentication

It is hard to work with the API over shibboleth, so we have set up rewrite rules to bypass shibboleth.

Base `https://nuxeo.cdlib.org`

 * `/Nuxeo/site/api/v1`
 * `/Nuxeo/site/automation`
 * `/Nuxeo/nxpicsfile`
 * `/Nuxeo/nxbigfile`
 * `/Nuxeo/nxdoc`
 * `/Nuxeo/restAPI`

### Basic Authentication
Please contact `ucldc@ucop.edu` to set up a nuxeo account with a password for use with Basic Authentication.

### Token Authentication
Nuxeo also supports token authentication.  [More information from Nuxeo](https://github.com/nuxeo/nuxeo-platform-login/tree/master/nuxeo-platform-login-token).

The base URL for creating a token is `https://nuxeo.cdlib.org/nuxeo/authentication/token`.

The following parameters must be supplied:

  * `applicationName` -- name of the application using the token.
  * `deviceId` -- id of the computer or device that will be using the token.
  * `permission` -- permissions granted to the token, such as `r` or `rw`.
  * A `deviceDescription` is optional.

The token is sent as plain text in the response body.

An error response will be sent with a 400 status code if one of the required parameters is null or empty. 

You can create as many tokens as you need.  Tokens can be individually turned off by you in the Nuxeo interface.

#### Using the token

Supply the token as the value of the `X-Authentication-Token` http header when making https requests to `https://nuxeo.cdlib.org/Nuxeo/*` URLs.


 


