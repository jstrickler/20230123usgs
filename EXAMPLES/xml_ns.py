from pprint import pprint
import lxml.etree as ET

XML_FILE = '../DATA/libreoffice_content.xml'

TAG_LIST = [  # List of tags (with ns prefix) to find
    'style:font-face',
    'text:list-style',
]

ATTRIBUTE_LIST = [  # List of attributes (with ns prefix) to find
    'text:name',
    'style:name',
]


def main():

    doc = ET.parse(XML_FILE)  # Parse XML file into ElementTree

    root = doc.getroot()  # Get the root Element

    print("Namespace map:\n")
    pprint(root.nsmap)  # Display the namespace map as found in the XML document
    print("\n\n")

    print("Finding nodes by tags:\n")

    for tag in TAG_LIST:
        xpath = './/' + tag  # Create xpath search string for NS:TAG
        node = root.find(xpath, root.nsmap)  # Find tag; NS prefix is looked up in NS map
        print("Searching for tag [{}]\n".format(xpath))
        print_node(node)

    print("Finding nodes by attributes:\n")

    for attribute in ATTRIBUTE_LIST:
        xpath = './/*[@{}]'.format(attribute)  # Create xpath search string for NS:ATTRIBUTE
        node = root.find(xpath, root.nsmap)
        print("Searching for attribute [{}]\n".format(xpath))
        print_node(node)


def print_node(node):
    node_as_string = ET.tostring(node, pretty_print=True).decode()  # Convert Element to bytes object with pretty_printing, then decode to str
    print(node_as_string, '\n')

if __name__ == '__main__':
    main()
