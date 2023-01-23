
def void(thing_being_decorated):
    return 42  # replace function with 42

name = "Guido"
x = void(name)

@void  # decorate hello() function
def hello():
    print("Hello, world")

@void
def howdy():
    print("Howdy, world")

print(hello, type(hello)) # hello is now the integer 42, not a function
print(howdy, type(howdy)) # hello is now the integer 42, not a function
print(x, type(x))
