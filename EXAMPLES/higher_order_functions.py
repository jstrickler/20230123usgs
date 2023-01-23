#

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]


def process_list(alist, func):  # Define a function that accepts a list and a passed-in function (AKA callback)
    new_list = []
    for item in alist:
        new_list.append(func(item))  # Call the callback function on one item of the passed-in list
    return new_list


f1 = process_list(fruits, str.upper)  # Call process_list() with str.upper as the callback
print(f1, "\n")

f2 = process_list(fruits, lambda s: s[0].upper())  # Call process_list() with a lambda function as the callback
print(f2, "\n")

f3 = process_list(fruits, len)  # Call process_list() with the builtin function len() as the callback()
print(f3, "\n")

total_length = sum(process_list(fruits, len))  # Pass the result of process_list() to the builtin function sum() to sum all the values in the returned list

print(total_length, "\n")
