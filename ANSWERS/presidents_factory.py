#!/usr/bin/env python
# (c) 2016 John Strickler
#
import csv
from lxml import etree as ET
from lxml.builder import E

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    presidents_tree = ET.Element('presidents')
    for pres_rec in rdr:
        president = E.presidents(
            E.firstname(pres_rec[1]),
            E.lastname(pres_rec[2]),
            E.birthplace(pres_rec[3]),
            E.birthstate(pres_rec[4]),
            E.party(pres_rec[5]),
            term=pres_rec[0],
        )

        presidents_tree.append(president)

tree = ET.ElementTree(presidents_tree)
tree.write('potus.xml', pretty_print=True, xml_declaration=True)
