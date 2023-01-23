#
from itertools import chain, takewhile, dropwhile

spam = ['alpha', 'beta', 'gamma']
ham = ['delta', 'epsilon', 'zeta']

for letter in chain(spam, ham):  # treat spam and ham as a single iterable
    print(letter, end=' ')
print("\n")

eggs = [spam, ham]

for letter in chain.from_iterable(eggs):  # treat all elements of eggs as a single iterable
    print(letter, end=' ')
print("\n")

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]

for fruit in takewhile(lambda f: len(f) > 4, fruits):  # iterate over elements of fruits as long as length of current item > 4
    print(fruit, end=' ')
print("\n")

for fruit in takewhile(lambda f: f[0] != 'k', fruits):  # iterate over elements of  fruits as long as fruit does not start with 'k'
    print(fruit, end=' ')
print("\n")

values = [5, 18, 22, 31, 44, 57, 59, 61, 66, 70, 72, 78, 90, 99]

for value in dropwhile(lambda f: f < 50, values):  # skip over elements of values as long as value is < 50, then iterate over all remaining elements
    print(value, end=' ')
print("\n")
