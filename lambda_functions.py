from functools import partial

def doit(some_func):
    some_func()

def spam():
    print("spam spam spam")

doit(spam)

doit(lambda : print("whoo hooo"))

#  lambda params: value

def ham(color):
    print(color)

ham_blue = partial(ham, "blue")


doit(ham_blue)



