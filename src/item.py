class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Item name: {self.name}, Item Description: {self.description}"

class Sword(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Shield(Item):
    def __init__(self, name, description, armor):
        super().__init__(name, description)
        self.armor = armor
        
# Examples
# Rapier = Sword('swooooord', 'shing, shing.', "1d8")
# Buckler = Shield("shiiield", "block, block.", "+1 to AC")