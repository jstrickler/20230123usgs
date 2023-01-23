counts = {}  # create new empty dict

with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip()
        if breakfast_item in counts:   # check to see if current item in dict
            counts[breakfast_item] = counts[breakfast_item] + 1   # if so, increment count for specified key
        else:
            counts[breakfast_item] = 1 # else add new element 

for item, count in counts.items():
    print(item, count)
