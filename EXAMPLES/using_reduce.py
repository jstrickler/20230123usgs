#
from operator import add, mul
from functools import reduce

values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# sum()
result = reduce(add, values) # add values in list (initial value defaults to 0)
print("result is", result)

# sum() + 1000
result = reduce(add, values, 1000)  # add values in list (initial value is 1000)
print("result is", result)

# product
result = reduce(mul, values)  # multiply all values together (initial value is 1, otherwise product would be 0)
print("result is", result)

strings = ['fi', 'fi', 'fo', 'fum']

# join
result = reduce(add, strings, "") # concatenate strings (initial value is empty string; each string in iterable added to it)
print("result is", result)

# join + upper case
result = reduce(add, map(str.upper, strings), "")  # same, but make strings upper case
print("result is", result)
