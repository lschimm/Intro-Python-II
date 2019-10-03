class Animal:
    def __init__(self):
        self.name = 'Animal'
        self.sound = 'animal noise'

        self.secret_number = 982

    def __str__(self):
        return f"<Animal: {self.name}, {self.sound}, {self.secret_number}>"

    def make_sound(self):
        print(self.sound)


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'cat'
        self.sound = 'Meow'


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'dog'
        self.sound = 'arf'


animals = [Cat(), Dog(), Cat(), Dog()]

for a in animals:
    a.make_sound()

# a = Animal()
# print(a)
# a.make_sound()
c = Cat()
print(c)
# c.make_sound()  # uses the function inside animal/ inherits that function


class Calico(Cat):
    def __init__(self):
        super().__init__()
        self.sound = "Calico meow"


cc = Calico()
print(c)
