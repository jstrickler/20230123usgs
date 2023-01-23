class Animal():
    _count = 0  # class data

    def __init__(self, species, name, sound):
        self._species = species
        self._name = name
        self._sound = sound
        Animal._count += 1

    @property
    def species(self):
        return self._species

    def die(cls):
        Animal._count -= 1

    @classmethod
    def kill(cls, obj):
        obj.die()

    @property
    def name(self):
        return self._name

    def make_sound(self):
        print(self._sound)

    @classmethod
    def count(cls):  # zoo_size gets class object when called from instance or class
        return cls._count

if __name__ == "__main__":
    leo = Animal("African lion", "Leo", "Roarrrrrrr")
    garfield = Animal("cat", "Garfield", "Meowwwww")
    felix = Animal("cat", "Felix", "Meowwwww")

    for animal in leo, garfield, felix:
        print(animal.name, "is a", animal.species, "--", end=' ')
        animal.make_sound()

    print(animal.count())
    animal.kill(leo)
    print(animal.count())
    garfield.die()
    print(animal.count())
