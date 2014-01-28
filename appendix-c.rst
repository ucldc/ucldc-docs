******************************************************************************
Appendix C. Linking from Digital Objects to Collection Descriptions
******************************************************************************

The following guidelines apply to specialized use of the METS <mdRef> Metadata Reference element to create links from digital objects to associated, parent-level collection descriptions or “finding aids” (represented either in the form of a MARC record or in the form of an EAD collection guide). Note that particular METS profiles may provide for more specific guidelines on use of the <mdRef> element for this or other purposes.

.. raw:: html

    <u><b>MARC record linking</b></u>

If the collection description is encoded in a MARC record, then encode the entire URL for the MARC record in a <mdRef> Metadata Reference HREF attribute of the object's METS wrapper. Include a MDTYPE attribute (see the bolded examples). Note that it may be difficult to generate a static and durable URL for particular MARC records, depending on local OPACs:

*Example*::

    <METS:dmdSec ID='DMR1'>
        <METS:mdRef LOCTYPE='URL' MDTYPE='MARC' 
                xlink:href='http://antpac.lib.uci.edu/search/tkim+ha/tkim+ha/1%2C3%2C3%2CB/frameset&amp;FF=tkim+ha+papers+1983+1999&amp;1%2C1%2C'/>
    </METS:dmdSec>

.. raw:: html

    <u><b>EAD finding aid linking</b></u>

If the collection-level description is encoded as an EAD finding aid, then use the following procedures:

1.      Obtain the Archival Resource Key (ARK) URL for the finding aid that you would like to link the object to. (For finding aids already submitted to the CDL, the finding aid ARK URL can be obtained by viewing the finding aid in the OAC website).  Below is an example of the ARK URL syntax:

        \http://www.oac.cdlib.org/findaid/ark:/13030/##########

        The ARK is a machine-readable unique identifier scheme for persistent access to digital resources managed by the CDL. Because ARKs are specially constructed and globally unique identifiers, their production and management is controlled by the CDL. 

        In some cases, you may be creating objects that will link to a finding aid that has not yet been created or completed (and will be submitted to the CDL at a later time). To obtain a new “placeholder” ARK for the finding aid, `contact the CDL <mailto:oacops@cdlib.org>`_. At the point that you create the finding aid, encode the ARK within the <eadid> identifier attribute (see the bolded example). Only encode the portion of the ARK beginning with “ark:/...”, and not the entire ARK URL: 

        *Example of EAD finding aid with ARK encoding*::

            <eadid countrycode=“us” identifier=“ark:/13030/kt4w10133d” mainagencycode=“CU-SC” 
                publicid=“PUBLIC “-//University of California, Santa Cruz::University Library::Special Collections//TEXT (US::CU-SC::MS 74::John Cage Mycology Collection)//EN” “ms74.sgm”>
                ms74.xml
            </eadid>
    
2.      Encode the entire ARK URL for the finding aid in a <mdRef> metadata reference HREF attribute of the object’s METS wrapper: 

        *Example*::
        
            <METS:dmdSec ID="DMR1">
                <METS:mdRef LOCTYPE="URL" MDTYPE="EAD" LABEL="Arnold Rubin Papers"
                    xlink:href="http://www.oac.cdlib.org/findaid/ark:/13030/kt7489n8zj"/>
            </METS:dmdSec> 
        
        The LABEL value should be the title for the collection that the object is related to (e.g., “Arnold Rubin Papers”). This should be the same title used for the collection in the associated finding aid.

3.      Create or update your finding aids to link to their associated objects, following the specifications outlined in the `OAC Best Practice Guidelines for EAD <http://www.cdlib.org/services/dsc/contribute/docs/oacbpgead_v2-0.pdf>`_ (OAC BPG EAD), Sections 4.4.5 and 4.5. 

        Please ensure that the objects are online at the time that the finding aid (with outbound links) is published in the OAC.