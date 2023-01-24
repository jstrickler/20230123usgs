from timeit import Timer

setup = """
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava", 
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon", 
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]
"""

code1 = """sorted([f.upper() for f in fruits if f.startswith('p')])"""
code2 = """[f.upper() for f in sorted(fruits) if f.startswith('p')]"""

t1 = Timer(code1, setup)
t2 = Timer(code2, setup)

print(t1.timeit())
print(t2.timeit())

