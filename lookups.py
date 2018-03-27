
ITEMS_CLASS_URIS = {
    'board': [
        'http://www.w3.org/ns/org#Organization',
        'http://linked.data.gov.au/def/ont/directory.gov.au#Board'
    ],
    'commonwealth_of_parliament': [
        'http://www.w3.org/ns/org#Organization',
        'http://linked.data.gov.au/def/ont/directory.gov.au#CommonwealthOfParliament'
    ],
    'courts': [
        'http://www.w3.org/ns/org#Organization',
        'http://linked.data.gov.au/def/ont/directory.gov.au#Court'
    ],
    'directory_role': [
        'http://www.w3.org/ns/org#Organization',
        'http://linked.data.gov.au/def/ont/directory.gov.au#DirectoryRole'
    ],
    'directory_sub_structure': [
        'http://www.w3.org/ns/org#Organization',
        'http://linked.data.gov.au/def/ont/directory.gov.au#DirectorySubStructure'
    ],
    'enquiry_line': [
        'http://linked.data.gov.au/def/ont/directory.gov.au#EnquiryLine'
    ],
    'governor_general': [
        'http://xmlns.com/foaf/0.1/Person',
        'http://linked.data.gov.au/def/ont/directory.gov.au#GovernorGeneral'
    ],
    'non_board': [
        'http://www.w3.org/ns/org#Organization',
        'http://linked.data.gov.au/def/ont/directory.gov.au#NonBoard'
    ],
    'organisation': [
        'http://www.w3.org/ns/org#Organization'
    ],
    'person': [
        'http://xmlns.com/foaf/0.1/Person'
    ],
    'portfolio': [
        'http://www.w3.org/ns/org#Organization',
        'http://linked.data.gov.au/def/ont/directory.gov.au#Portfolio'
    ],
    'portfolio_role': [
        'http://www.w3.org/ns/org#Role',
        'http://linked.data.gov.au/def/ont/directory.gov.au#PortfolioRole'
    ],
    'role': [
        'http://www.w3.org/ns/org#Role'
    ],
    'single_executive_role': [
        'http://www.w3.org/ns/org#Role',
        'http://linked.data.gov.au/def/ont/directory.gov.au#SingleExecutiveRole'
    ]
}


ITEMS_NAMED_INDIVIDUALS_URI_BASES = {
    'board':                        'http://linked.data.gov.au/dataset/directory.gov.au/board/',
    'commonwealth_of_parliament':   'http://linked.data.gov.au/dataset/directory.gov.au/commonwealthOfParliament/',
    'courts':                       'http://linked.data.gov.au/dataset/directory.gov.au/courts/',
    'directory_role':               'http://linked.data.gov.au/dataset/directory.gov.au/directoryRole/',
    'directory_sub_structure':      'http://linked.data.gov.au/dataset/directory.gov.au/directorySubStructure/',
    'enquiry_line':                 'http://linked.data.gov.au/dataset/directory.gov.au/enquiryLine/',
    'governor_general':             'http://linked.data.gov.au/dataset/directory.gov.au/governorGeneral/',
    'non_board':                    'http://linked.data.gov.au/dataset/directory.gov.au/nonBoard/',
    'organisation':                 'http://linked.data.gov.au/dataset/directory.gov.au/organisation/',
    'person':                       'http://linked.data.gov.au/dataset/directory.gov.au/person/',
    'portfolio':                    'http://linked.data.gov.au/dataset/directory.gov.au/portfolio/',
    'portfolio_role':               'http://linked.data.gov.au/dataset/directory.gov.au/portfolioRole/',
    'role':                         'http://linked.data.gov.au/dataset/directory.gov.au/role/',
    'single_executive_role':        'http://linked.data.gov.au/dataset/directory.gov.au/singleExecutiveRole/',
}
CLASSIFICATION = {
    'A. Principal': 'http://linked.data.gov.au/def/ont/directory.gov.au#Principal',
    'B. Secondary': 'http://linked.data.gov.au/def/ont/directory.gov.au#Secondary',
    'C. Other': 'http://linked.data.gov.au/def/ont/directory.gov.au#Other',
    'X. Internal Management': 'http://linked.data.gov.au/def/ont/directory.gov.au#',
    'Y. Non-Government': 'http://linked.data.gov.au/def/ont/directory.gov.au#'
}


TYPE_OF_BODY = {
    'A. Non Corporate Commonwealth Entity':
        'http://linked.data.gov.au/def/ont/directory.gov.au#NonCorporateCommonwealthEntity',
    'B. Corporate Commonwealth Entity':
        'http://linked.data.gov.au/def/ont/directory.gov.au#CorporateCommonwealthEntity',
    'C. Commonwealth Company':
        'http://linked.data.gov.au/def/ont/directory.gov.au#CommonwealthCompany',
    'D. Advisory Body - Policy and Stakeholder Consultation':
        'http://linked.data.gov.au/def/ont/directory.gov.au#AdvisoryBodyPolicyAndStakeholderConsultation',
    'E. Statutory Office Holder Offices and Committees':
        'http://linked.data.gov.au/def/ont/directory.gov.au#StatutoryOfficeHolderOfficesandCommittees',
    'F. Non Statutory - Function w Separate Branding':
        'http://linked.data.gov.au/def/ont/directory.gov.au#NonStatutoryFunctionWithSeparateBranding',
    'G. Ministerial Councils and Related Bodies including those Established by the COAG':
        'http://linked.data.gov.au/def/ont/directory.gov.au#MinisterialCouncilsAndRelatedBodiesIncludingThoseEstablishedByTheCOAG',
    'H. Inter Jurisdictional and International Bodies':
        'http://linked.data.gov.au/def/ont/directory.gov.au#InterJurisdictionalAndInternationalBodies',
    'I. Subsidiaries of Corporate Commonwealth Entities and Commonwealth Companies':
        'http://linked.data.gov.au/def/ont/directory.gov.au#'
        'SubsidiariesOfCorporateCommonwealthEntitiesAndCommonwealthCompanies',
    'J. Joint Ventures, Partnerships and Interests in Other Companies':
        'http://linked.data.gov.au/def/ont/directory.gov.au#'
        'JointVenturesPartnershipsAndInterestsInOtherCompanies',
    'K. National Law Bodies':
        'http://linked.data.gov.au/def/ont/directory.gov.au#NationalLawBodies',
    'L. Bodies Linked to the Australian Government through Statutory Contracts Agreements and Delegations':
        'http://linked.data.gov.au/def/ont/directory.gov.au#'
        'BodiesLinkedToTheAustralianGovernmentThroughStatutoryContractsAgreementsAndDelegations',

    'R. Management Board':
        'http://linked.data.gov.au/def/ont/directory.gov.au#ManagementBoard',
    'S. Internal Organisation Structure':
        'http://linked.data.gov.au/def/ont/directory.gov.au#InternalOrganisationStructure',
    'U. Non-Government Body': 'http://linked.data.gov.au/def/ont/directory.gov.au#NonGovernmentBody'
}
