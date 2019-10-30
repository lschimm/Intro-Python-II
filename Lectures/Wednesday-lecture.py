# Stores!

class Store:
    def __init__(self, name):
        self.name = self

    def __str__(self):
        return f"Store: {self.name}"



s = Store("Gundams R Us")


# print(s.name)
print(s)

num = input("Enter dept number: ")

i = int(num)