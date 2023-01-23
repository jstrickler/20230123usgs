#
from datetime import date as Date
from random import randint
from itertools import groupby

date_details = [
    (1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30),
    (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31),
]


def main():
    sample_dates = generate_sample_dates()
    display_groups(sample_dates)


def generate_sample_dates():
    '''
    Generate sorted list of random dates.

    @return: sorted list of datetime.date objects
    '''
    dates = []
    for month, days in date_details:
        for i in range(1, days + 1):
            for _ in range(randint(1, 3)):
                date = Date(2014, month, i)
                dates.append(date)
    return dates


def display_groups(dates):
    '''
    Display dates, grouped by ISO week #

    @param dates: a sorted list of Python datetime.date objects
    @return: None
    '''
    for week_number, date_list in groupby(dates, lambda e: e.isocalendar()[1]):
        print("Week:", week_number)
        for dl in date_list:
            print("\t" + str(dl))


if __name__ == '__main__':
    main()
