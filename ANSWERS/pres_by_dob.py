#!/usr/bin/python
import datetime

FILE = '../DATA/presidents.txt'

def main():
    info = []
    with open(FILE) as presidents_in:
        for line in presidents_in:
            (
                term, lname, fname, bdate, ddate, bplace, bstate, tsdate, tedate,
                party
            ) = line[:-1].split(':')
    
            name = '{} {}'.format(fname, lname)
    
            birth_date = make_date(bdate)
    
            info.append((name, birth_date, party))
    
    for name, date, party in sorted(info, key=lambda e: e[1]):
        print("{:35s} {} {}".format(name, date, party))

def make_date(date_str):
    year, month, day = date_str.split('-')
    date = datetime.date(int(year), int(month), int(day))
    return date


if __name__ == '__main__':
    main()
