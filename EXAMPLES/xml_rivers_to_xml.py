import csv
from dicttoxml import dicttoxml  # import dicttoxml module
import lxml.etree as ET
from pprint import pprint

rivers = {'rivers': []}  # create dictionary where key is tag and value is empty list

with open('../DATA/longest_rivers.csv') as rivers_in:
    rdr = csv.reader(rivers_in)
    for name, length in rdr:
        rivers['rivers'].append({'name': name, 'length': length})  # append sub-dictionary to dictionary tag element

pprint(rivers)
print('-' * 60)

snippet = dicttoxml(rivers, attr_type=False, root=False,
                    item_func=lambda x: x.rstrip('s'))  # create XML text snippet from dictionary

river_root = ET.fromstring(snippet)  # Parse XML text into tree of Elements
river_doc = ET.ElementTree(river_root)  # create ElementTree object from Element tree

print(ET.tostring(river_doc, pretty_print=True, xml_declaration=True).decode())  # convert XML doc to string (should be same as earlier snippet from dicttoxml()

river_doc.write('longest_rivers.xml', pretty_print=True,
                xml_declaration=True)  # write XML doc out to file
