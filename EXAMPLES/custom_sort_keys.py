
fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon",
         "Kiwi", "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG",
         "pear", "banana", "Tamarind", "persimmon", "elderberry", "peach",
         "BLUEberry", "lychee", "grape"]

def ignore_case(item):  # Parameter is _one_ element of iterable to be sorted
    return item.lower()  # Return value to sort on

fs1 = sorted(fruit, key=ignore_case)  # Specify function with named parameter key
print("Ignoring case:")
print(" ".join(fs1), end="\n\n")

def by_length_then_name(item):
    return (len(item), item.lower())  # Key functions can return tuple of values to compare, in order

fs2 = sorted(fruit, key=by_length_then_name)
print("By length, then name:")
print(" ".join(fs2))
print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)  # Numbers sort numerically by default
print("Numbers sorted numerically:")
for n in n1:
    print(n, end=' ')
print("\n")

n2 = sorted(nums, key=str)  # Sort numbers as strings
print("Numbers sorted as strings:")
for n in n2:
    print(n, end=' ')
print()
