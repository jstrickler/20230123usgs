from pdb import set_trace
from  carddeck import CardDeck
from jokerdeck import JokerDeck

print(callable(42))
print(callable(CardDeck))

d1 = CardDeck("Wednesday")
print(f"d1: {d1}")
print(f"repr(d1): {repr(d1)}")
print(f"d1._dealer: {d1._dealer}")  # naughty naughty!!

print(f"d1.dealer: {d1.dealer}")  # public variable
print(f"d1.udealer: {d1.udealer}")

d1.dealer = "Ahab"
print(f"d1.dealer: {d1.dealer}")

try:
    d1.dealer = 123
except TypeError as err:
    print(err)

print(f"d1.cards: {d1.cards}")
d1.shuffle()

for i in range(8):
    print(d1.draw())
print()
print('-' * 60)
j1 = JokerDeck("Jimmy")
print(f"j1: {j1}")
j1.shuffle()
print(f"j1.cards: {j1.cards}")
# set_trace()  # jump into debugger
print(len(d1), len(j1))
print(repr(j1))

# len(d1)
# CardDeck.__len__(d1)

x = d1 + j1
print(x)
print(len(x))
print(x.draw())
print(dir(d1))
