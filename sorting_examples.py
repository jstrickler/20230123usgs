fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print(f"f0: {f0}\n")

f1 = sorted(fruits, key=str.lower)
print(f"f1: {f1}\n")

def ignore_case(s):
    comparison_value = s.lower()
    print(f"comparing {s} as {comparison_value}")
    return comparison_value

f2 = sorted(fruits, key=ignore_case)
print(f"f2: {f2}\n")

f3 = sorted(fruits, key=len)
print(f"f3: {f3}\n")

def len_and_name(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=len_and_name)
print(f"f4: {f4}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_last_name(p):
    return p[1], p[0]

for person in sorted(people, key=by_last_name):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: (p[3], p[1])):
    print(person)


