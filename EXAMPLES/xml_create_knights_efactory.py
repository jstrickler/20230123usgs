'''Create, print, and save a new XML document'''
from lxml.builder import E  # import E object
import lxml.etree as ET

FILE_NAME = 'knights.xml'


def main():
    '''Program entry point'''
    knight_info = get_knight_info()
    knight_root = build_tree(knight_info)
    knight_doc = ET.ElementTree(knight_root)
    write_doc(knight_doc)


def get_knight_info():
    '''Read knight data from the file'''
    info = []
    with open('../DATA/knights.txt') as kn:
        for line in kn:
            flds = line[:-1].split(':')
            info.append(flds)
    return info


def build_tree(knight_recs):
    '''Build the new XML document'''
    tree = ET.Element('knights')
    for knight_rec in knight_recs:
        knight = E.knight(  # create <knight> tag
            E.title(knight_rec[1]),  # nest other tags inside <knight>
            E.color(knight_rec[2]),
            E.quest(knight_rec[3]),
            E.comment(knight_rec[4]),
            name=knight_rec[0],
        )

        tree.append(knight)  # add <knight> tag to <knights> tag

    return tree


def write_doc(doc):
    '''Write the XML document out to a file, pretty-printing if available'''
    doc.write(FILE_NAME, pretty_print=True)


if __name__ == '__main__':
    main()
