#
import csv
from lxml import etree
from lxml.builder import ElementMaker  # import ElementMaker

NS_RIVER_URL = "http://www.cja-tech.com/ns/river"  # (fake) URL for namespace

E = ElementMaker(  # create ElementMaker with namespace
    namespace=NS_RIVER_URL,
    nsmap={'lr': NS_RIVER_URL}
)

RIVER_LIST = E.riverlist  # use ElementMaker to create individual element makers
RIVER = E.river
RIVER_NAME = E.name
RIVER_LENGTH = E.length

doc = RIVER_LIST()  # create <riverlist> tag

with open('../DATA/longest_rivers.csv') as rivers_in:
    rdr = csv.reader(rivers_in)
    for row in rdr:  # iterate over records in file
        doc.append(
            RIVER(  # use element makers to create <river> elements, with other elements nested inside
                RIVER_NAME(row[0]),
                RIVER_LENGTH(row[1])
            )
        )

print(etree.tostring(doc, pretty_print=True).decode())  # pretty-print XML
etree.ElementTree(doc).write('longest_rivers_ns.xml',
                             pretty_print=True)  # write XML to file
