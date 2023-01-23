#
from itertools import islice, count, cycle, repeat

for i in count(0, 10):  # count by tens starting at 0 forever
    if i > 50:
        break  # without a check, will never stop
    print(i, end=' ')
print("\n")

for i in islice(count(0, 10), 6):  # saner, using islice to get just the first 6 results
    print(i, end=' ')
print("\n")

giant = ['fee', 'fi', 'fo', 'fum']

for i in islice(cycle(giant), 10):  # cycle over values in list forever (use islice to stop)
    print(i, end=' ')
print("\n")

for i in repeat('tick', 10):  # repeat value 10 times (default is repeat forever)
    print(i, end=' ')
print("\n")
