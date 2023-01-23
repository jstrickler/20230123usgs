#
from itertools import product, permutations, combinations

SUITS = 'CDHS'
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = product(SUITS, RANKS)  # Cartesian product (match every item in one list to every item in the other list)
print(list(cards), '\n')

cards = [r + s for r, s in product(SUITS, RANKS)]  # reverse order and concatenate elements using list comprehension
print(cards, '\n')

giant = ['fee', 'fi', 'fo', 'fum']

result = combinations(giant, 2)  # all distinct combinations of 4 items taken 2 at a time
print(list(result), "\n")

result = permutations(giant, 2)  # all distinct permutations of 4 items taken 2 at a time
print(list(result), "\n")
