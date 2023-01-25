from itertools import chain, islice

a = [0, 1, 2, 3]
b = 4, 5, 6
c = "789"

for value in chain(a, b, c):
    print(value, end=' ')
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruit_list = [f.upper() for f in fruits]
print(f"fruit_list: {fruit_list}")
print(f"fruit_list[2:6]: {fruit_list[2:6]}")

fruit_gen = (f.upper() for f in fruits)
print(f"fruit_gen: {fruit_gen}")
fruit_slice = islice(fruit_gen, 2, 6)
print(f"fruit_slice: {fruit_slice}")
for x in fruit_slice:
    print(x)
print('-' * 60)
for x in fruit_gen:
    print(x)

data = [('spam', 'ham', 'toast'), ('foo', 'bar', 'blah'), ('wombat', 'koala', 'musk ox')]

for item in chain.from_iterable(data):
    print(item)







