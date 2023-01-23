#!/usr/bin/env python

from president import President

for pres_term in 1, 26, 37:
    p = President(pres_term)

    lastname = getattr(p, 'last_name')
    firstname = getattr(p, 'first_name')
    party = getattr(p, 'party')
    print (firstname, lastname, 'was a', party)
