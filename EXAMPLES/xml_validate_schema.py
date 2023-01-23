#
import os
from lxml import etree

XML_BASE = '../DATA' # set global variables for file locations
PRES_SCHEMA_PATH = os.path.join(XML_BASE, 'presidents.xsd')
PRES_XML_PATH = os.path.join(XML_BASE, 'presidents.xml')
BAD_PRES_XML_PATH = os.path.join(XML_BASE, 'presidents_bad.xml')

pres_schema = etree.XMLSchema(file=PRES_SCHEMA_PATH) # create schema from schema (.xsd) file
pres_parser = etree.XMLParser(schema=pres_schema) # create XML parser that uses schema

def validate(xml_path):
    try:
        pres_doc = etree.parse(xml_path, parser=pres_parser) # try to parse XML
    except etree.ParseError as err: # catch error if XML is invalid
        print(("Error Parsing {}:".format(xml_path)))
        print(err)
    else:
        print(("Parsed {} OK:".format(xml_path)))
        print(pres_doc) # XML is valid
    print(('-' * 60))

for xml_doc in PRES_XML_PATH, BAD_PRES_XML_PATH: # iterate over list of (2) XML files and try to validate
    validate(xml_doc)
