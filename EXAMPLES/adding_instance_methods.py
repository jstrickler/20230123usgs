from types import MethodType

class Dog(): # Define Dog type
    pass

d1 = Dog()  # Create instance of Dog

def bark(self):  # Define (unbound) function
    print("Woof! woof!")

setattr(Dog, "bark", bark)  # Add function to class (which binds it as an instance method)

d2 = Dog() # Define another instance of Dog

d1.bark()  # New function can be called from either instance
d2.bark()

def wag(self): # Create another unbound function
    print("Wagging...")

setattr(d1, "wag", MethodType(wag, d1))  # Add function to instance after passing it through MethodType()

d1.wag()  # Call instance method
try:
    d2.wag()  # Instance method not available - only bound to d1
except AttributeError as err:
    print(err)
