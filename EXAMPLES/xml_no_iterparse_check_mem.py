import lxml.etree as et
from memorychecker import MemoryChecker

def main():
    mem_checker = MemoryChecker()  # Create memory checker object

    doc = et.parse("../BIG_DATA/pubmed19n0001.xml")

    i = 0  # in case no articles were found
    for i, element in enumerate(doc.findall('.//PubmedArticle')):
        article_title = element.findtext('.//ArticleTitle')
        month_completed = element.findtext('.//DateCompleted/Month')
        year_completed = element.findtext('.//DateCompleted/Year')
        current_mem_use = mem_checker()  # Get current memory use
        print("{}/{} {} {}".format(month_completed, year_completed, article_title[:70], current_mem_use ))
    print("Total count: {}".format(i))




if __name__ == '__main__':
    main()
