
from animal import Animal


class Mammal(Animal):  # inherit from Animal
    def __init__(self, species, name, sound, gestation):
        super(Mammal, self).__init__(species, name, sound)
        self._gestation = gestation

    @property
    def gestation(self):  # add property to existing Animal properties
        """Length of gestation period in days"""
        return self._gestation


if __name__ == "__main__":
    mammal1 = Mammal("African lion", "Bob", "Roarrrr", 120)
    print(mammal1.name, "is a", mammal1.species, "--", end=' ')
    mammal1.make_sound()

    print("Number of animals", mammal1.count())

    mammal2 = Mammal("Fruit bat", "Freddie", "Squeak!!", 180)
    print(mammal2.name, "is a", mammal2.species, "--", end=' ')
    mammal2.make_sound()

    print("Number of animals mammal2.count()", mammal2.count())
    print("Number of animals Mammal.count()", Mammal.count())
    print("Number of animals Animal.count()", Animal.count())

    mammal1.die()
    print("Number of animals", Mammal.count())

    print(f"Gestation period of the {mammal1.species} is {mammal1.gestation} days")
    print(f"Gestation period of the {mammal2.species} is {mammal2.gestation} days")

    print(Animal.count())
    Animal.kill(mammal1)
    print(Animal.count())
