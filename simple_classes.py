x = list()    #  List x = new List();
x.append('spam')
x.append('ham')
print(f"x[0]: {x[0]}")  # x.__getitem__(0)
print(f"x: {x}")  # repr()  vs. print()
poem = "Mary had a little lamb\nHer fleece was white as snow"
print(f"poem: {poem}")
print(f"repr(poem): {repr(poem)}")

count = 1    #   Int count = new count(1);
print(type(x), type(count), type(print), type(type))


class Dog:
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d2 = Dog()
d3 = Dog()
d2.bark()











