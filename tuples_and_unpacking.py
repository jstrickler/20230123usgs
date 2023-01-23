
gates = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(f"type(gates): {type(gates)}")
print(f"gates[0]: {gates[0]}")

# tuple: record, struct, row, etc...
alpha = 1, 2, 3
beta = 1, 2
gamma = 1,
delta = ()

def doit(person):
    first_name, last_name, product, dob = person  # iterable unpacking
    print(first_name, last_name)

doit(gates)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
]

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)
print('-' * 60)

for first_name, last_name, *_ in people:
    print(first_name, last_name, _)
print('-' * 60)



