from timeit import Timer

NUM_RUNS = 100

setup_code = """
from random import random
NUM_ROWS = 5000
NUM_COLUMNS = 30
data = []
for i in range(NUM_ROWS):
    new_row = []
    data.append(new_row)
    for j in range(NUM_COLUMNS):
        new_row.append(round(random() * 100, 2))
"""

codes = [
    ('str concat', """
csv = ""
for raw_row in data:
    row = ",".join(str(i) for i in raw_row)
    csv += (row + "\\n")
    
with open('junk1.csv', 'w') as junk_out:
    junk_out.write(csv)
    """),

    ('csv module', """
import csv
with open('junk2.csv', 'w') as junk_out:
    wtr = csv.writer(junk_out)
    for row in data:
        wtr.writerow(row)
    """),

    ('bytearray', """
csv = bytearray()

for data_row in data:
    row = ','.join(str(i) for i in data_row)
    csv.extend(ord(c) for c in row)
    csv.append(ord('\\n'))

    
with open('junk3.csv', 'wb') as junk_out:
    junk_out.write(csv)

    """),

    ('list concat', """
csv = list()
for data_row in data:
    csv.append(','.join(str(i) for i in data_row))

with open('junk4.csv', 'w') as junk_out:
    junk_out.write('\\n'.join(csv))
    junk_out.write('\\n')

    """),

    ('numpy', """
import numpy as np
a = np.array(data)
np.savetxt('junk5.csv', a, delimiter=',', fmt="%5.2f")
    """),

]

for label, code in codes:
    t = Timer(code, setup_code)
    # print(code, '\n')
    print(label, t.timeit(NUM_RUNS))
    print('-' * 60)
