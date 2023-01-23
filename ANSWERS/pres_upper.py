#!/usr/bin/python

last_names = []
with open('../DATA/presidents.txt') as pres_in:
    for line in pres_in:
        last_name = line.split(':')[1]
        last_names.append(last_name)

print(last_names)

last_names_upper = [ln.upper() for ln in last_names]

for last_name in last_names_upper:
    print(last_name)
