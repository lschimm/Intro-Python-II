class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Item name: {self.name}, Item Description: {self.description}"

class Sword(Item):
    def __init__(self, name, description):
        super().__init__(name, description, damage)
        self.name = name
        self.damage = damage

class Shield(Item):
    def __init__(self, name, description):
        super().__init__(name, description, block)
        self.name = name
        self.block = block