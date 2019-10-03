class Lifeform:  # "Base class"
    pass


"Subclasses of Lifeform"


class Plant(Lifeform):
    "Plant inherits from Lifeform"
    "Plant subclasses Lifeform"
    "Plant is-a Lifeform"
    "Plant specializes Lifeform"
    "Lifeform is the parent class of Plant"
    "Plant is the child class of Lifeform"
    pass


class Animal(Lifeform):
    pass


class Vertebrate(Animal):
    pass


class Mammal(Vertebrate):
    pass


class Cat(Mammal):
    pass
