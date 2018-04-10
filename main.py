from os import path
from datetime import datetime
import requests
from lxml import objectify
from rdflib import Graph, URIRef, Namespace, Literal, XSD, RDF, RDFS, OWL, BNode
import datetime
import lookups


URIDs = {}


def get_directory_xml():
    r = requests.get('https://www.directory.gov.au/sites/default/files/export.xml')
    this_dir = path.dirname(path.realpath(__file__))
    export_file_name = 'export_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.xml'
    open(path.join(this_dir, 'data', export_file_name), 'w').write(r.content.decode('utf-8'))


def make_type_count(export_file_name):
    """
    Makes something like this from an export.xml:

    types = {
        'board': 826,
        'commonwealth_of_parliament': 14,
        'courts': 3,
        'directory_role': 4478,
        'directory_sub_structure': 3513,
        'enquiry_line': 145,
        'governor_general': 4,
        'non_board': 372,
        'organisation': 180,
        'person': 9043,
        'portfolio': 18,
        'portfolio_role': 255,
        'role': 4331,
        'single_executive_role': 48
    }

    :param export_file_name:
    :return:
    """
    this_dir = path.dirname(path.realpath(__file__))
    types = {}
    items = objectify.parse(path.join(this_dir, 'data', export_file_name)).getroot().getchildren()
    for item in items:
        t = str(item.type)
        if t not in types.keys():
            types[t] = 0
        else:
            types[t] += 1

    return types


def parse_board(g, item, this_uri):
    if item.get('board_function_category') is not None:
        g.add((
            this_uri,
            AUORG.function_category,
            Literal(item.board_function_category, datatype=XSD.string)
        ))  # board_function_category TODO: change this to a categorised URI


def parse_commonwealth_of_parliament(g, item, this_uri):
    pass


def parse_courts(g, item, this_uri):
    pass


def parse_directory_role(g, item, this_uri):
    pass


def parse_directory_sub_structure(g, item, this_uri):
    pass


def parse_enquiry_line(g, item, this_uri):
    pass


def parse_governor_general(g, item, this_uri):
    pass


def parse_non_board(g, item, this_uri):
    pass


def parse_organisation(g, item, this_uri):
    '''
    <item>
        <content_id>80951</content_id>
        <unique_record_id>O-000887</unique_record_id>
        <title>Geoscience Australia</title>
        <type>organisation</type>
        <portfolio>78911</portfolio>
        <abn>80 091 799 039</abn>
        <annual_report_prep_tabled>Yes</annual_report_prep_tabled>
        <auditor>ANAO</auditor>
        <asl>600</asl>
        <classification>A. Principal</classification>
        <creation_date>1949-07-02 00:00:00</creation_date>
        <current_budget_total_expenditure>206121</current_budget_total_expenditure>
        <current_budget_total_appropriations>155790</current_budget_total_appropriations>
        <description><![CDATA[Geoscience Australia is Australia&#039;s national geoscience agency and exists to apply geoscience to Australia&#039;s most important challenges. Geoscience Australia provides geoscientific advice and information to the Australian Government to support it to deliver its priorities. Geoscientific information is also provided to industry and other stakeholders where it supports achievement of Australian Government objectives.]]></description>
        <email>sales@ga.gov.au</email>
        <established_by_under>PGPA Rule (Schedule 1)</established_by_under>
        <fax_number>(02) 6249 9999</fax_number>
        <gfs_function>Mining and Mineral Resources (other than fuels) Manufacturing and Construction</gfs_function>
        <gfs_sector_classification>GGS</gfs_sector_classification>
        <materiality>Small</materiality>
        <media_releases>http://www.ga.gov.au/about-us/news-media.html</media_releases>
        <phone_number>(02) 6249 9111</phone_number>
        <type_of_body>A. Non Corporate Commonwealth Entity</type_of_body>
        <updated>20/06/2017 - 4:15pm</updated>
        <website>http://www.ga.gov.au</website>
        <address><country><![CDATA[AU]]></country><administrative_area><![CDATA[ACT]]></administrative_area><locality><![CDATA[Symonston]]></locality><postal_code><![CDATA[2609]]></postal_code><thoroughfare><![CDATA[Cnr Jerrabomberra Ave and Hindmarsh Drive]]></thoroughfare></address>
        <postal_address>GPO Box 378, Canberra ACT 2601</postal_address>
        <ps_act_body>Yes - Operate with some Independence</ps_act_body>
        <annual_reports>http://www.ga.gov.au/about/corporate-documents</annual_reports>
        <budget_documentation>http://www.ga.gov.au/about/corporate-documents</budget_documentation>
        <strat_corp_org_plan>http://www.ga.gov.au/about/corporate-documents</strat_corp_org_plan>
    </item>
    '''


def parse_portfolio(g, item, this_uri):
    pass


def parse_portfolio_role(g, item, this_uri):
    pass


def parse_role(g, item, this_uri):
    pass


def parse_single_executive_role(g, item, this_uri):
    pass


def parse_item(g, item):
    '''
    <item>
        <postal_address>GPO Box 378, Canberra ACT 2601</postal_address>
        <current_budget_total_expenditure>206121</current_budget_total_expenditure>
        <current_budget_total_appropriations>155790</current_budget_total_appropriations>
        <established_by_under>PGPA Rule (Schedule 1)</established_by_under>
        <fax_number>(02) 6249 9999</fax_number>
        <gfs_function>Mining and Mineral Resources (other than fuels) Manufacturing and Construction</gfs_function>
        <gfs_sector_classification>GGS</gfs_sector_classification>
        <materiality>Small</materiality>
        <media_releases>http://www.ga.gov.au/about-us/news-media.html</media_releases>
        <ps_act_body>Yes - Operate with some Independence</ps_act_body>
        <annual_reports>http://www.ga.gov.au/about/corporate-documents</annual_reports>
        <budget_documentation>http://www.ga.gov.au/about/corporate-documents</budget_documentation>
        <strat_corp_org_plan>http://www.ga.gov.au/about/corporate-documents</strat_corp_org_plan>
    </item>
    '''
    # generic item parsing
    # unique_record_id
    this_uri = URIRef(lookups.ITEMS_NAMED_INDIVIDUALS_URI_BASES[item.type] + item.unique_record_id)

    # content_id
    # add this item's unique_record_id & content_id mapping to temp lookup
    URIDs[item.content_id] = this_uri

    # title
    g.add((this_uri, RDFS.label, Literal(item.title, datatype=XSD.string)))  # title

    # type
    for c in lookups.ITEMS_CLASS_URIS[item.type]:
        g.add((this_uri, RDF.type, URIRef(c)))

    # portfolio
    if hasattr(item, 'portfolio'):
        g.add((
            this_uri,
            AUORG.portfolio,
            URIRef(lookups.ITEMS_NAMED_INDIVIDUALS_URI_BASES['portfolio'] + str(item.portfolio))))

    # abn
    if hasattr(item, 'abn'):
        g.add((this_uri, ORG.identifier, Literal(item.abn, datatype=AUORG.AustralianBusinessNumber)))

    # annual_report_prep_tabled
    if hasattr(item, 'annual_report_prep_tabled'):
        annual_report_prep_tabled = True
    else:
        annual_report_prep_tabled = False
    g.add((this_uri, AUORG.annualReportPrepTabled, Literal(annual_report_prep_tabled, datatype=XSD.boolean)))

    # auditor
    if hasattr(item, 'auditor'):
        if item.auditor == 'ANAO':
            auditor_uri = URIRef(lookups.ITEMS_NAMED_INDIVIDUALS_URI_BASES['organisation'] + 'O-000908')
        else:
            auditor_uri = URIRef('http://www.opengis.net/def/nil/OGC/0/unknown')
        auditorAttr = BNode()
        g.add((this_uri, PROV.qualifiedAttribution, auditorAttr))
        g.add((auditorAttr, RDF.type, PROV.Attribution))
        g.add((auditorAttr, PROV.agent, auditor_uri))
        g.add((auditorAttr, PROV.hadRole, AUORG.Auditor))  # TODO: add Auditor to AUORG ont

    # asl
    if hasattr(item, 'asl'):
        g.add((this_uri, AUORG.averageStaffingLevel, Literal(item.asl, datatype=XSD.nonNegativeInteger)))

    # classification
    if hasattr(item, 'classification'):
        g.add((
            this_uri,
            AUORG.classification,
            Literal(item.classification, datatype=XSD.string)
        ))  # TODO: use a SKOS collection not AUORG.classification

    # classification
    # TODO: set up an AUORG type hierarchy but only "A. Principle" in the given data
    g.add((this_uri, RDF.type, URIRef(AUORG.PrincipleOrgansation)))

    # creation_date: 1949-07-02 00:00:00
    # TODO: deprecate this value since the current entity, GA, was not created at this date, a precursor was
    if hasattr(item, 'creation_date'):
        created = datetime.datetime.strptime(str(item.creation_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        g.add((this_uri, DCT.created, Literal(created, datatype=XSD.date)))

    # updated
    # TODO: ensure it's understood this is the date of the metadata, not the ORG
    updated = datetime.datetime.strptime(str(item.updated), '%d/%m/%Y - %I:%M%p').strftime('%Y-%m-%d')
    g.add((this_uri, DCT.modified, Literal(updated, datatype=XSD.date)))

    # description
    if hasattr(item, 'description'):
        g.add((this_uri, DCT.description, Literal(item.description, datatype=XSD.string)))

    # type_of_body
    # TODO: add these to a subclass hierarchy in the AUORG ontology
    if hasattr(item, 'type_of_body'):
        g.add((this_uri, RDF.type, URIRef(lookups.TYPE_OF_BODY[item.type_of_body])))

    # email
    if hasattr(item, 'email'):
        g.add((this_uri, VCARD.hasEmail, URIRef('mailto:{}'.format(item.email))))

    # phone_number
    if hasattr(item, 'phone_number'):
        phone = BNode()
        g.add((this_uri, VCARD.hasTelephone, phone))
        g.add((phone, RDF.type, VCARD.Work))
        g.add((phone, RDF.type, VCARD.Voice))
        tel = 'tel:{}'.format(item.phone_number)\
            .replace('(0', '+61')\
            .replace(')', '') \
            .replace(' ', '-')
        g.add((phone, VCARD.hasValue, URIRef(tel)))

    # website
    if hasattr(item, 'website'):
        website_uri = URIRef(str(item.website)
                             .replace(' ', '')
                             .replace('\\', '/')
                             .replace('|', '')
                             )
        g.add((this_uri, OWL.seeAlso, website_uri))  # due to one URL having a space

    '''
    <address>
        <country><![CDATA[AU]]></country>
        <administrative_area><![CDATA[ACT]]></administrative_area>
        <locality><![CDATA[Symonston]]></locality>
        <postal_code><![CDATA[2609]]></postal_code>
        <thoroughfare><![CDATA[Cnr Jerrabomberra Ave and Hindmarsh Drive]]></thoroughfare>
    </address>
    <postal_address>GPO Box 378, Canberra ACT 2601</postal_address>
    '''
    # address
    if hasattr(item, 'address'):
        address = lookups.ADDRESSES.get(item.unique_record_id)
        if address is not None:
            g.add((this_uri, VCARD.hasStreetAddress, URIRef(address)))
        else:
            # we don't have a GNAF address so we may as well try and cobble together an ISO19160 VCARD
            s_add = BNode()  # TODO: replace this with URI from GNAF
            g.add((s_add, RDF.type, VCARD.Work))
            g.add((s_add, RDF.type, VCARD.Address))
            if hasattr(item.address, 'thoroughfare'):
                g.add((
                    s_add,
                    URIRef('http://www.w3.org/2006/vcard/ns#street-address'),
                    Literal(item.address.thoroughfare, datatype=XSD.string)))
            if hasattr(item.address, 'locality'):
                g.add((
                    s_add,
                    URIRef('http://www.w3.org/2006/vcard/ns#locality'),
                    Literal(item.address.locality, datatype=XSD.string)))
            if hasattr(item.address, 'administrative_area'):  # State
                g.add((
                    s_add,
                    URIRef('http://www.w3.org/2006/vcard/ns#region'),
                    Literal(item.address.administrative_area, datatype=XSD.string)))
            if hasattr(item.address, 'postal_code'):
                g.add((
                    s_add,
                    URIRef('http://www.w3.org/2006/vcard/ns#postal-code'),
                    Literal(item.address.postal_code, datatype=XSD.string)))
            g.add((
                s_add,
                URIRef('http://www.w3.org/2006/vcard/ns#country-name'),
                Literal('Australia', datatype=XSD.string)))
            g.add((this_uri, ORG.siteAddress, s_add))

    # postal_address TODO: complete
    if hasattr(item, 'postal_address'):
        p_add = BNode()
        g.add((p_add, RDF.type, VCARD.Work))
        g.add((p_add, RDF.type, VCARD.Address))

        # g.add((this_uri, VCARD.hasStreetAddress, s_add))

        # g.add((this_uri, ORG.siteAddress, AUORG.NonCorporateCommonwealthEntity))
        # g.add((this_uri, RDF.type, AUORG.NonCorporateCommonwealthEntity))

    # current_budget_total_appropriations
    if hasattr(item, 'current_budget_total_appropriations'):
        budget = item.current_budget_total_appropriations * 1000
        g.add((this_uri, AUORG.budgetAppropriations, Literal(budget, datatype=AUORG.AustralianDollars)))
        # TODO: ad to AUORG

    # extra parsing based on item type
    if item.type == 'board':
        parse_board(g, item, this_uri)
    elif item.type == 'commonwealth_of_parliament':
        parse_commonwealth_of_parliament(g, item, this_uri)
    elif item.type == 'courts':
        parse_courts(g, item, this_uri)
    elif item.type == 'directory_role':
        parse_directory_role(g, item, this_uri)
    elif item.type == 'directory_sub_structure':
        parse_directory_sub_structure(g, item, this_uri)
    elif item.type == 'enquiry_line':
        parse_enquiry_line(g, item, this_uri)
    elif item.type == 'governor_general':
        parse_governor_general(g, item, this_uri)
    elif item.type == 'non_board':
        parse_non_board(g, item, this_uri)
    elif item.type == 'organisation':
        parse_organisation(g, item, this_uri)
    elif item.type == 'portfolio':
        parse_board(g, item, this_uri)
    elif item.type == 'portfolio_role':
        parse_portfolio_role(g, item, this_uri)
    elif item.type == 'role':
        parse_role(g, item, this_uri)
    elif item.type == 'single_executive_role':
        parse_single_executive_role(g, item, this_uri)


def parse_items(g, export_file_name):
    this_dir = path.dirname(path.realpath(__file__))
    export_file_path = path.join(this_dir, 'data', export_file_name)
    items = objectify.parse(export_file_path).getroot().getchildren()
    for item in items:
        parse_item(g, item)


def set_up_graph(g):
    pass


if __name__ == '__main__':
    # get the XML from the web
    # get_directory_xml()
    #
    # print('got XML')
    # exit()

    # set up the graph
    g = Graph()
    # set_up_graph(g)

    # declare namespaces
    SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
    g.bind('skos', SKOS)
    DCT = Namespace('http://purl.org/dc/terms/')
    g.bind('dct', DCT)
    ORG = Namespace('http://www.w3.org/ns/org#')
    g.bind('org', ORG)
    PROV = Namespace('http://www.w3.org/ns/prov#')
    g.bind('prov', PROV)
    FOAF = Namespace('http://xmlns.com/foaf/0.1/')
    g.bind('foaf', FOAF)
    VCARD = Namespace('http://www.w3.org/2006/vcard/ns#')
    g.bind('vcard', VCARD)
    AUORG = Namespace('http://linked.data.gov.au/def/ont/auorg#')
    g.bind('auorg', AUORG)

    # TODO: incorporate this into an ontology/ORG profile
    # custom datatype
    g.add((AUORG.AustralianBusinessNumber, RDFS.label, Literal('Australian Business Number', datatype=XSD.string)))
    desc = '''A number issued by the Australian Business Register (https://abr.gov.au) to identify businesses in 
    Australia. Australian Business Numbers (ABN)s are formatted as per: NN NNN NNN NNN, for example, the ABN for 
    Geoscience Australia is 80 091 799 039'''
    g.add((AUORG.AustralianBusinessNumber, RDFS.comment, Literal(desc, datatype=XSD.string)))

    # custom datatype
    g.add((AUORG.AustralianDollars, RDFS.label, Literal('Australian Dollars', datatype=XSD.string)))
    g.add((AUORG.AustralianDollars, RDFS.subPropertyOf, XSD.decimal))

    # parse the XML file
    parse_items(g, 'export_2018-04-10.xml')

    # write the resultant graph to a turtle file
    # ttl_file = 'export_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.ttl'
    ttl_file = 'export_2018-04-10.nt'
    open(ttl_file, 'w').write(g.serialize(format='nt').decode('utf-8'))
