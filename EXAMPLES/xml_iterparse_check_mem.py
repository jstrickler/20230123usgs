from lxml.etree import iterparse
from memorychecker import MemoryChecker

def main():
    doc = iterparse("../BIG_DATA/pubmed19n0001.xml", tag='PubmedArticle')  # Start parser

    mem_checker = MemoryChecker()  # Create memory checker object

    for i, (event, element) in enumerate(doc, 1):  # Loop over (and count) found elements
        year_completed = element.findtext('.//DateCompleted/Year')  # Get text from subelement
        month_completed = element.findtext('.//DateCompleted/Month')
        clear_element(element)
        current_mem_use = mem_checker() # Get current memory use

        print("{:5d}. {}/{} {}".format(i, month_completed, year_completed, current_mem_use))

    print("Total count: {}".format(i))

def clear_element(element):
    element.clear()  # Remove memory used by current node
    while element.getprevious() is not None:  # Loop over siblings already seen
        del element.getparent()[0]  # Remove sibling

if __name__ == '__main__':
    main()
