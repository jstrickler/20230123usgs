#
"""
Demo of the Facade design pattern
"""
import csv

PRESIDENTS_FILE = '../DATA/presidents.csv'

class CSVUpper():
    """
    A facade for a CSV file
    """
    def __init__(self, csv_file):
        self._file_in = open(csv_file)
        self._rdr = csv.reader(self._file_in)

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self._rdr)
        if row:
            return [r.upper() for r in row]
        else:
            raise StopIteration()

    def __del__(self):
        self._file_in.close()

if __name__ == '__main__':
    presidents = CSVUpper(PRESIDENTS_FILE)
    for p in presidents:
        print(p)
