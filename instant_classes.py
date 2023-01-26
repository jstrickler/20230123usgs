
class Animal:
    pass

class Cat(Animal):
    def meow(self):
        print("meow")

c = Cat()
c.meow()

Dog = type('Dog', (Animal), {'bark': lambda self: print("woof woof")})

d = Dog()
d.bark()
print(f"isinstance(d, Dog): {isinstance(d, Dog)}")
print(f"isinstance(d, Animal): {isinstance(d, Animal)}")
