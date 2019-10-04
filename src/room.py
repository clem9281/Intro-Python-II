# Implement a class to hold room information. This should have name and
# description attributes.

from items import Item
from player import Player


class Room(Player):
    def __init__(
        self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None
    ):
        # Don't understand why items needs to go first here
        super().__init__(items, name)
        self.description = description
        self.inventory = []
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        for item in items:
            super().addItem(item)

    def __str__(self):
        return f"Room: {self.name} : {self.description} : {self.inventory}"

    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"

