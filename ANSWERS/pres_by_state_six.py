import six

with open("../DATA/presidents.txt") as pres_in:
    count_of = {}

    for rec in pres_in:
        flds = rec.split(":")
        state = flds[6]
        if state in count_of:
            count_of[state] += 1
        else:
            count_of[state] = 1

for state, count in sorted(six.iteritems(count_of)):
    six.print_("%-16s %2d" % (state, count))
