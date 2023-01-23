#!/usr/bin/env python
# (c) 2016 John Strickler
#
import csv
from collections import OrderedDict
# note: OrderDict not needed starting with 3.6
from dicttoxml import dicttoxml
import lxml.etree as ET


with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    presidents = {'presidents': []}

    for pres_rec in rdr:
        president = OrderedDict()
        president["term"] = pres_rec[0]
        president["firstname"] = pres_rec[1]
        president["lastname"] = pres_rec[2]
        president["birthplace"] = pres_rec[3]
        president["birthstate"] = pres_rec[4]
        president["party"] = pres_rec[5]
        presidents['presidents'].append(president)

pres_xml = dicttoxml(presidents, root=False, attr_type=False,
        item_func=lambda e: 'president')

print(pres_xml)

pres_root = ET.fromstring(pres_xml)
pres_doc = ET.ElementTree(pres_root)

print(ET.tostring(pres_doc, pretty_print=True, xml_declaration=True))

pres_doc.write('potus_gen.xml', pretty_print=True,
    xml_declaration=True)
