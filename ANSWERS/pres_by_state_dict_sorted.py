from itertools import groupby

with open("../DATA/presidents.txt") as pres_in:
    states = map(lambda p: p.split(':')[6], pres_in)
    for state, state_group in groupby(sorted(states)):
        print(state, len(list(state_group)))
