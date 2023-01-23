
from datetime import date

color = 'blue'
animal = 'iguana'

print('{} {}'.format(color, animal))  # {} placeholders are autonumbered, starting at 0; this

fahr = 98.6839832
print('{:.1f}'.format(fahr))  # Formatting directives start with ':'; .1f means format

value = 12345
print('{0:d} {0:04x} {0:08o} {0:016b}'.format(value))  # {} placeholders can be manually numbered to reuse parameters

data = {'A': 38, 'B': 127, 'C': 9}

for letter, number in sorted(data.items()):
    print("{} {:4d}".format(letter, number))  # :4d means format decimal integer in a field 4 characters wide
