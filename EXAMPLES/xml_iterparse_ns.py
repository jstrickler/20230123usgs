from lxml.etree import iterparse

XML_FILE = '../DATA/libreoffice_content.xml'


TAG_LIST = [  # List of tags to find, with namespace prefixes
    'style:font-face',
    'text:list-level-style-number',
]


def main():
    nsmap = get_nsmap()  # Create the namespace mapping dictionary

    tag_list = [replace_prefix(tag, nsmap) for tag in TAG_LIST]  # Replace prefixes with actual namespaces, as used by etree

    context = iterparse(XML_FILE, tag=tag_list)  # Open the file for parsing

    for i, (event, element) in enumerate(context, 1):  # Iterate over file, finding tags as needed
        print(element.tag, element.text)
        # Do something with the element here. 'element' is a normal etree Element object, which you can search, etc.

        element.clear()  # When finished with the element, remove it, since we don't need it. If we don't do this, we will run out of memory when processing huge XML files

        while element.getprevious() is not None:  # Also clear siblings. if we don't do this, on a really large XML file we'll leave empty nodes, and the memory use will add up. On a sub-GB file, probably not so important
            del element.getparent()[0]

    print("found {} elements".format(i))


def get_nsmap():
    """
    Parse the entire file to get the embedded namespaces,
    an turn them into a dictionary for later use.

    Note -- you could write this to run separately, saving the nsmap in a file
    (pickle would work great here) and then reuse it for
    subsequent searches, rather than always having to parse twice.

    :return: Dict of namespace mappings
    """
    # Parse document looking for beginning namespace tags
    # Returns tuples of (event, element) (in this case event is always 'start-ns')
    # Each element is a ("prefix", "namespace") tuple
    parser = iterparse(XML_FILE, events=('start-ns',))

    # Use generator expression to pull elements out of the parser,
    # which become the key:value pairs of a new dictionary mapping prefixes to namespaces
    # Note: This reads the entire XML file.
    nsmap = dict(element for event, element in parser)

    return nsmap  # Return NS map as dict


def replace_prefix(nstag, nsmap):
    """
    Replace the tag prefix with the actual namespace, surrounded by "{}", because
    this is what etree.iterparse() needs.

    :param nstag: A tag in the form:  "prefix:tag"
    :param nsmap: The dictionary of namespace mappings
    :return: A string with the full namespace as used by etree: "{full-namespace}tag"
    """
    prefix, tag = nstag.split(':')  # split "prefix:tag" into separate strings
    map = nsmap.get(prefix, "ERROR")   # get the namespace for that prefix
    return "{{{}}}{}".format(map, tag)  # return the namespace and tag in etree format

if __name__ == '__main__':
    main()
