from lxml.etree import iterparse


def main():
    # Create a 'context' -- start the parser, skipping all but specified tag
    doc = iterparse("../BIG_DATA/pubmed19n0001.xml", tag='PubmedArticle')

    # Loop over each occurrence of tag ("end event").
    # Use enumerate() to count how many elements found
    for i, (event, element) in enumerate(doc, 1):
        # Within the found element (tag="PubmedArticle") find subelements and get their text
        article_title = element.findtext('.//ArticleTitle')
        year_completed = element.findtext('.//DateCompleted/Year')
        month_completed = element.findtext('.//DateCompleted/Month')
        clear_element(element)  # Clear element after all wanted data is extracted
        print("{}/{} {}".format(month_completed, year_completed, article_title[:70]))

    print("Total count: {}".format(i))


def clear_element(element):
    element.clear()  # Remove element from memory
    while element.getprevious() is not None:  # Loop over siblings
        # Delete parents (saves memory left over in empty nodes)
        del element.getparent()[0]


if __name__ == '__main__':
    main()
