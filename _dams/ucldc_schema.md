---
title: Metadata Schema XSD
---

##Document Types and Schemas

Each object type (Picture, Audio, Video, File, Complex) in the DAMS is referred to in Nuxeo as a **document type** under the hood. Nuxeo document types can have many schemas associated with them. In this case, the document types defining Picture, Audio, Video, File, and Complex objects all use the `ucldc_schema` to store metadata fields and the `extra_files` schema to store auxiliary content files and auxiliary file metadata. These document types also each use a schema defined to store their respective content file - a picture schema, audio schema, video schema, and file schema. The `ucldc_schema` and `extra_files` schema are described below:

##`ucldc_schema` - used to store metadata

<a href="{{ site.url }}{{ site.baseurl }}/docs/dams/ucldc_schema.xsd" download><span class="glyphicon glyphicon-download"></span> Download the ucldc\_schema.xsd</a>

{% highlight xml+cheetah linenos %}
<?xml version="1.0" encoding="UTF-8"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:nxs="http://www.nuxeo.org/ecm/project/schemas/tingle-california-digita/ucldc_schema" targetNamespace="http://www.nuxeo.org/ecm/project/schemas/tingle-california-digita/ucldc_schema">  
  <!-- helper XSD definitions for list types -->  
  <xs:complexType name="content"> 
    <xs:sequence> 
      <xs:element name="encoding" type="xs:string"/>  
      <xs:element name="mime-type" type="xs:string"/>  
      <xs:element name="data" type="xs:base64Binary"/>  
      <xs:element name="name" type="xs:string"/>  
      <xs:element name="length" type="xs:long"/>  
      <xs:element name="digest" type="xs:string"/> 
    </xs:sequence> 
  </xs:complexType>  
  <xs:simpleType name="stringList"> 
    <xs:list itemType="xs:string"/> 
  </xs:simpleType>  
  <xs:simpleType name="doubleList"> 
    <xs:list itemType="xs:double"/> 
  </xs:simpleType>  
  <xs:simpleType name="dateList"> 
    <xs:list itemType="xs:date"/> 
  </xs:simpleType>  
  <xs:simpleType name="integerList"> 
    <xs:list itemType="xs:integer"/> 
  </xs:simpleType>  
  <xs:simpleType name="booleanList"> 
    <xs:list itemType="xs:boolean"/> 
  </xs:simpleType>  
  <xs:complexType name="blobList"> 
    <xs:sequence> 
      <xs:element name="item" type="nxs:content" minOccurs="0" maxOccurs="unbounded"/> 
    </xs:sequence> 
  </xs:complexType>  
  <xs:element name="accessrestrict" type="xs:string"/>
  <xs:element name="alternativetitle" type="nxs:stringList"/>
  <xs:element name="campusunit" type="nxs:stringList"/>
  <xs:element name="collection" type="nxs:stringList"/>
  <xs:element name="contributor" type="nxs:ucldc_schema_contributorListType"/>
  <xs:complexType name="ucldc_schema_contributorListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_contributorType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_contributorType">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="nametype" type="xs:string"/>
      <xs:element name="role" type="xs:string"/>
      <xs:element name="source" type="xs:string"/>
      <xs:element name="authorityid" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="creator" type="nxs:ucldc_schema_creatorListType"/>
  <xs:complexType name="ucldc_schema_creatorListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_creatorType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_creatorType">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="nametype" type="xs:string"/>
      <xs:element name="role" type="xs:string"/>
      <xs:element name="source" type="xs:string"/>
      <xs:element name="authorityid" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="date" type="nxs:ucldc_schema_dateListType"/>
  <xs:complexType name="ucldc_schema_dateListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_dateType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_dateType">
    <xs:sequence>
      <xs:element name="date" type="xs:string"/>
      <xs:element name="datetype" type="xs:string"/>
      <xs:element name="inclusivestart" type="xs:string"/>
      <xs:element name="inclusiveend" type="xs:string"/>
      <xs:element name="single" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="description" type="nxs:ucldc_schema_descriptionListType"/>
  <xs:complexType name="ucldc_schema_descriptionListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_descriptionType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_descriptionType">
    <xs:sequence>
      <xs:element name="type" type="xs:string" default="scopecontent"/>
      <xs:element name="item" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="extent" type="xs:string"/>
  <xs:element name="formgenre" type="nxs:ucldc_schema_formgenreListType"/>
  <xs:complexType name="ucldc_schema_formgenreListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_formgenreType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_formgenreType">
    <xs:sequence>
      <xs:element name="heading" type="xs:string"/>
      <xs:element name="source" type="xs:string"/>
      <xs:element name="authorityid" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="identifier" type="xs:string"/>
  <xs:element name="language" type="nxs:ucldc_schema_languageListType"/>
  <xs:complexType name="ucldc_schema_languageListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_languageType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_languageType">
    <xs:sequence>
      <xs:element name="language" type="xs:string"/>
      <xs:element name="languagecode" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="localidentifier" type="nxs:stringList"/>
  <xs:element name="physdesc" type="xs:string"/>
  <xs:element name="physlocation" type="xs:string"/>
  <xs:element name="place" type="nxs:ucldc_schema_placeListType"/>
  <xs:complexType name="ucldc_schema_placeListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_placeType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_placeType">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="source" type="xs:string"/>
      <xs:element name="coordinates" type="xs:string"/>
      <xs:element name="authorityid" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="provenance" type="nxs:stringList"/>
  <xs:element name="publisher" type="nxs:stringList"/>
  <xs:element name="relatedresource" type="nxs:stringList"/>
  <xs:element name="rightscontact" type="xs:string"/>
  <xs:element name="rightsdeterminationdate" type="xs:date"/>
  <xs:element name="rightsenddate" type="xs:date"/>
  <xs:element name="rightsholder" type="nxs:ucldc_schema_rightsholderListType"/>
  <xs:complexType name="ucldc_schema_rightsholderListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_rightsholderType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_rightsholderType">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="nametype" type="xs:string"/>
      <xs:element name="source" type="xs:string"/>
      <xs:element name="authorityid" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="rightsjurisdiction" type="xs:string"/>
  <xs:element name="rightsnote" type="xs:string"/>
  <xs:element name="rightsnotice" type="xs:string"/>
  <xs:element name="rightsstartdate" type="xs:date"/>
  <xs:element name="rightsstatement" type="xs:string"/>
  <xs:element name="rightsstatus" type="xs:string"/>
  <xs:element name="source" type="xs:string"/>
  <xs:element name="subjectname" type="nxs:ucldc_schema_subjectnameListType"/>
  <xs:complexType name="ucldc_schema_subjectnameListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_subjectnameType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_subjectnameType">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="nametype" type="xs:string"/>
      <xs:element name="role" type="xs:string"/>
      <xs:element name="source" type="xs:string"/>
      <xs:element name="authorityid" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="subjecttopic" type="nxs:ucldc_schema_subjecttopicListType"/>
  <xs:complexType name="ucldc_schema_subjecttopicListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:ucldc_schema_subjecttopicType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ucldc_schema_subjecttopicType">
    <xs:sequence>
      <xs:element name="heading" type="xs:string"/>
      <xs:element name="headingtype" type="xs:string"/>
      <xs:element name="source" type="xs:string"/>
      <xs:element name="authorityid" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="temporalcoverage" type="nxs:stringList"/>
  <xs:element name="transcription" type="xs:string"/>
  <xs:element name="type" type="xs:string"/>
</xs:schema>

{% endhighlight %}

##`extra_files` - used to store auxiliary files and their metadata

<a href="{{ site.url }}{{ site.baseurl }}/docs/dams/extra_files.xsd" download><span class="glyphicon glyphicon-download"></span> Download the extra\_files.xsd</a>

{% highlight xml+cheetah linenos %}
<?xml version="1.0" encoding="UTF-8"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:nxs="http://www.nuxeo.org/ecm/project/schemas/tingle-california-digita/extra_files" targetNamespace="http://www.nuxeo.org/ecm/project/schemas/tingle-california-digita/extra_files">  
  <!-- helper XSD definitions for list types -->  
  <xs:complexType name="content"> 
    <xs:sequence> 
      <xs:element name="encoding" type="xs:string"/>  
      <xs:element name="mime-type" type="xs:string"/>  
      <xs:element name="data" type="xs:base64Binary"/>  
      <xs:element name="name" type="xs:string"/>  
      <xs:element name="length" type="xs:long"/>  
      <xs:element name="digest" type="xs:string"/> 
    </xs:sequence> 
  </xs:complexType>  
  <xs:simpleType name="stringList"> 
    <xs:list itemType="xs:string"/> 
  </xs:simpleType>  
  <xs:simpleType name="doubleList"> 
    <xs:list itemType="xs:double"/> 
  </xs:simpleType>  
  <xs:simpleType name="dateList"> 
    <xs:list itemType="xs:date"/> 
  </xs:simpleType>  
  <xs:simpleType name="integerList"> 
    <xs:list itemType="xs:integer"/> 
  </xs:simpleType>  
  <xs:simpleType name="booleanList"> 
    <xs:list itemType="xs:boolean"/> 
  </xs:simpleType>  
  <xs:complexType name="blobList"> 
    <xs:sequence> 
      <xs:element name="item" type="nxs:content" minOccurs="0" maxOccurs="unbounded"/> 
    </xs:sequence> 
  </xs:complexType>  
  <xs:element name="file" type="nxs:extra_files_fileListType"/>
  <xs:complexType name="extra_files_fileListType">
    <xs:sequence>
      <xs:element name="item" type="nxs:extra_files_fileType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="extra_files_fileType">
    <xs:sequence>
      <xs:element name="type" type="xs:string"/>
      <xs:element name="blob" type="nxs:content"/>
    </xs:sequence>
  </xs:complexType>
</xs:schema>

{% endhighlight %}
