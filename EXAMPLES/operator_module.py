from operator import add
import operator

a = 10
b = 15

print("a + b: {}".format(a + b))  # Add with add operator
print("add(a, b): {}".format(add(a, b)))  # Add with add function
print()
print(dir(operator))
