
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


fruit_list = [f.upper() for f in fruits]
print(f"fruit_list: {fruit_list}")

fruit_gen = (f.upper() for f in fruits)
print(f"fruit_gen: {fruit_gen}")
print(dir(fruit_gen))

