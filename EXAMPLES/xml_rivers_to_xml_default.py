#
import csv
from dicttoxml import dicttoxml # import dicttoxml module
import lxml.etree as ET

rivers = {'rivers': []} # create dictionary where key is tag and value is empty list
with open('../DATA/longest_rivers.csv') as rivers_in:
    rdr = csv.reader(rivers_in)
    for row in rdr: # for each river in source file, add dictionary with river into to main dictionary
        rivers['rivers'].append({'name': row[0], 'length': row[1]})

snippet = dicttoxml(rivers)  # convert dictionary to XML string

river_root = ET.fromstring(snippet) # create lxml element tree from snippet string
river_doc = ET.ElementTree(river_root) # create lxml doc from element tree

print(ET.tostring(river_doc, pretty_print=True, xml_declaration=True).decode())  # print XML

river_doc.write('longest_rivers_default.xml', pretty_print=True, xml_declaration=True) # save XML to file
