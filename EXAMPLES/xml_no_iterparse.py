import lxml.etree as et


def main():
    doc = et.parse("../BIG_DATA/pubmed19n0001.xml")


    i = 0  # in case no articles were found
    for i, element in enumerate(doc.findall('.//PubmedArticle')):
        article_title = element.findtext('.//ArticleTitle')
        month_completed = element.findtext('.//DateCompleted/Month')
        year_completed = element.findtext('.//DateCompleted/Year')
        print("{}/{} {}".format(month_completed, year_completed, article_title[:70]))

    print("Total count: {}".format(i))




if __name__ == '__main__':
    main()
