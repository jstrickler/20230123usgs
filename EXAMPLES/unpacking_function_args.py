#

people = [ # list of 4-element tuples
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Brown', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]

def display_person(first_name, last_name, city, state): # function that takes 4 parameters
    print("{} {} lives in {}, {}".format(first_name, last_name, city, state))

for person in people:  # person is a tuple (one element of people list)
    display_person(*person)  # {splat}person unpacks the tuple into four individual parameters
