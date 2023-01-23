

class MultiIndexList(list):  # Define new class that inherits from list

    def __getitem__(self, item):  # Redefine __getitem__ which implements []
        if isinstance(item, tuple):  # Check to see if index is tuple
            if len(item) == 0:
                raise ValueError("Tuple must be non-empty")
            else:
                tmp_list = []
                for index in item:
                    tmp_list.append(
                        super().__getitem__(index)  # Call list.__getitem__() for each index in tuple
                    )
                return tmp_list
        else:
            return super().__getitem__(item)  # Call the normal __getitem__()


if __name__ == '__main__':
    m = MultiIndexList(
        'banana peach nectarine fig kiwi lemon lime'.split()
    )  # Initialize a MultiIndexList
    m.append('apple')  # Add an element (works like normal list)
    m.append('mango')
    print(m)

    print(m[0])
    print(m[1])
    print(m[5, 2, 0])  # Index with tuple
    print(m[:4])
    print(len(m))
    print(m[5, ])
    print(m[:2, -2:])
    print()
    print(m)
    m.extend(['durian', 'kumquat'])
    print(m)
    print()
    for fruit in m:
        print(fruit)
    print(len(fruit))
