from io import StringIO  # import StringIO module which treats a string like a file object
import presidentsDS  # import module which was created separately from presidents.xsd

# to create presidentsDS module:
# python generateDS.py -o presidentsDS.py presidents.xsd

def main():
    pres_data = get_presidents_data('../DATA/presidents.txt')
    pres_list = build_presidents_xml(pres_data)
    xml_string = build_xml_string(pres_list)
    print(xml_string)
    write_xml_to_file(xml_string, 'presidents_generated.xml')


def get_presidents_data(file_name):
    with open(file_name) as presidents_in:
        records = [line.rstrip('\n\r').split(':') for line in presidents_in]
    return records


def build_presidents_xml(presidents_data):
    pres_list = presidentsDS.presidents.factory()  # use generated factory to create <presidents> element

    for president_info in presidents_data:
        pres = presidentsDS.presidentType.factory()  # use other factories to create nested data
        name = presidentsDS.nameType.factory()
        birth = presidentsDS.birthType.factory()
        death = presidentsDS.deathType.factory()
        termstart = presidentsDS.termstartType.factory()
        termend = presidentsDS.termendType.factory()

        name.set_last(president_info[1])  # set values for elements using factories
        name.set_first(president_info[2])
        pres.set_name(name)
        make_date(birth, president_info[3])
        pres.set_birth(birth)
        make_date(death, president_info[4])
        pres.set_death(death)
        pres.set_birthplace(president_info[5])
        pres.set_birthstate(president_info[6])
        make_date(termstart, president_info[7])
        pres.set_termstart(termstart)
        make_date(termend, president_info[8])
        pres.set_termend(termend)
        pres.set_party(president_info[9])

        pres_list.add_president(pres)

    return pres_list


def make_date(date_obj, date_str):
    """
    Convert date string from file into XML date element

    :param date_obj: date object from date factory
    :param date_str: date string to convert to date object
    :return: date object with data from string
    """
    if date_str == 'NONE':
        year, month, day = ("",) * 3
    else:
        year, month, day = date_str.split('-')
    date_obj.set_year(year)
    date_obj.set_month(month)
    date_obj.set_day(day)


def build_xml_string(pres_list):
    xml_str = StringIO()  # create StringIO() object
    pres_list.export(xml_str, 0)  # write XML into string object (like writing to file)
    return xml_str.getvalue()


def write_xml_to_file(xml, file_name):
    with open(file_name, 'w') as pres_out:
        pres_out.write(xml)  # save XML as file


if __name__ == '__main__':
    main()
