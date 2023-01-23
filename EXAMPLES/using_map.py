#

strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

result = [s.upper() for s in strings]  # Using a list comprehension, which is usually simpler than map()
print(result)

result = list(map(str.upper, strings))  # Using map to copy list to upper case
print(result)

result = list(map(len, strings))  # Using map to get list of string lengths
print(result)
