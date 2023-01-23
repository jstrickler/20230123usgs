from singledispatch import singledispatch
from io import TextIOWrapper

@singledispatch
def xopen(source, mode="r"):  # define generic function that is actually called
    source_type = type(source).__name__
    raise TypeError("Invalid arg: must be file, str, or bytes, not {}".format(source_type))

@xopen.register(TextIOWrapper)  # define handler for TextIOWrapper type (normal text files)
def _(fileobj):
    return fileobj

@xopen.register(str)  # define handler for string type
def _(str, mode="r"):
    return open(str, mode)


@xopen.register(bytes)  # define handler for bytes type
def _(bytes, mode="r"):
    return open(bytes.decode(), mode)


mary_in = open('../DATA/mary.txt')  # open a file and get a file object (type TextIOWrapper)

for x in mary_in, '../DATA/mary.txt', b'../DATA/mary.txt', 52:
    try:
        file_in = xopen(x)  # call single dispatch function -- correct handler will automatically be called
        result = file_in.read()
        print("Length: {}".format(len(result)))
    except TypeError as err:
        print('ERROR:', err)

print('-' * 60)
print(xopen.dispatch(str), "\n")  # show handler function for str

for arg_type, func in xopen.registry.items():
    print("{:30s} {}".format(str(arg_type), func))  # show functions for each registered type
