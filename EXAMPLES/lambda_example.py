
fruits = ['watermelon', 'lime', 'Apple', 'Mango', 'KIWI', 'apricot', 'LEMON', 'guava']

sorted_fruits = sorted(fruits, key=lambda e: (len(e), e.lower()))  # The lambda function takes one fruit name and returns a tuple containing the length of the name and the name in lower case. This sorts first by length, then by name.

print(sorted_fruits)
