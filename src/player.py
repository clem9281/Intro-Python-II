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
        if itemString == "":
            return "No items"
        return itemString

    def addItem(self, item):
        if isinstance(item, Item):
            self.inventory.append(item)
        else:
            self.inventory.append(Item(item["name"], item["description"]))

    def dropItem(self, item):
        self.inventory.remove(item)

    def __str__(self):
        return f"Player: {self.room}"

    def __repr__(self):
        return f"Player({repr(self.room)})"
