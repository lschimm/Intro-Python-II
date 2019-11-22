# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.bags = []

    # funciton to add items
    def add_to_inventory(self, item):
        self.bags.append(item)

    def __str__(self):
        return f"Name: {self.name}, Room: {self.room}"