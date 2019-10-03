# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Item


class Player:
    def __init__(self, room, name, items=[]):
        self.inventory = []
        for element in items:
            self.inventory.append(Item(element["name"], element["description"]))
        self.name = name
        self.room = room

    def printItems(self):
        itemString = ""
        for item in self.inventory:
            itemString += f"\n{item.name} : {item.description}"
        return itemString

    def addItems(self, items):

        for element in items:
            self.inventory.append(Item(element["name"], element["description"]))

    def __str__(self):
        return f"Player: {self.room}"

    def __repr__(self):
        return f"Player({repr(self.room)})"

