
def function_1(self):  # create method (not inside a class -- could be a lambda)
    print("Hello from f1()")


def function_2(self):  # create method (not inside a class -- could be a lambda)
    print("Hello from f2()")


NewClass = type("NewClass", (), {  # create class using type() -- parameters are class name, base classes, dictionary of attributes
    'hello1': function_1,
    'hello2': function_2,
    'color': 'red',
    'state': 'Ohio',
})

n1 = NewClass()  # create instance of new class

n1.hello1()  # call instance method
n1.hello2()
print(n1.color)  # access class data
print()

SubClass = type("SubClass", (NewClass,), {'fruit': 'banana'})  # create subclass of first class
s1 = SubClass()  # create instance of subclass
s1.hello1()  # call method on subclass
print(s1.color)  # access class data
print(s1.fruit)
