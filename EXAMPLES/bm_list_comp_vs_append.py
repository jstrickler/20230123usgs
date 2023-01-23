
from timeit import Timer
NUMBER_OF_ITERATIONS = 10000

setup = """
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]
"""

code_snippets = [
    """
f1 = []
for f in fruits:
    if f.startswith('p'):
        f1.append(f.upper())
    """,

    """
f1 = [f.upper() for f  in fruits if f.startswith('p')]
    """,
    """
gen = (f.upper() for f in fruits if f.startswith('p'))
f1 = list(gen)
    """,
    """
f1 = []
i = 0
fruit_len = len(fruits)
while i < fruit_len:
    if fruits[i].startswith('p'):
        f1.append(fruits[i].upper())
    i += 1
    """
]

for code in code_snippets:
    t = Timer(code, setup)
    print("{:60s}{}".format(code, t.timeit(NUMBER_OF_ITERATIONS)))
    print('-' * 60)
