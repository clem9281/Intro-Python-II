from room import Room
from player import Player
from items import Item

# Declare all the rooms
room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        "Dim light filters in from the south. Dusty passages run north and east.",
    ),
    "overlook": Room(
        "Grand Overlook",
        "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
    ),
    "narrow": Room(
        "Narrow Passage",
        "The narrow passage bends here from west to north. The smell of gold permeates the air.",
    ),
    "treasure": Room(
        "Treasure Chamber",
        "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
    ),
}
# Link rooms together
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# add items to rooms
room["outside"].addItems(
    [{"name": "Sword", "description": "It's dangerous to go alone: take this!"}]
)

room["foyer"].addItems(
    [
        {"name": "Potion", "description": "Restores a minor amount of health"},
        {"name": "Tent", "description": "Allows you to camp in certain areas"},
    ]
)
room["overlook"].addItems([{"name": "Potion", "description": "Restores a minor amount of health"}, {"name": "Tent", "description": "Allows you to camp in certain areas"}])
room["narrow"].addItems([{"name": "Bow", "description": "ranged weapon"}])
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player1 = Player(room["outside"], "player1")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# print(player1)


def play_game(player):
    while True:
        print(player.room.name)
        print(player.room.description)
        print(
            f"Your investigation of the room shows you it contains a: {player.room.printItems()}"
        )
        player_move = (input("What would you like to do? Go N S E W: ")).lower()
        if player_move == "q":
            print("End Game")
            break
        # If the room has that directional attribute, get it and set it to the next room, then set the player's room to next_room, but if that attribute hasn't been assigned yet print the prompt to try a different direction'
        elif hasattr(player.room, f"{player_move}_to"):
            next_room = getattr(player.room, f"{player_move}_to")
            # getattr might return none above, check if it returned a proper room
            if next_room:
                setattr(player, "room", next_room)
            else:
                print("There is nothing in that direction, try again!")
        # if nothing above has fired then the user gave us something other than n s e w so tell them their input is invalid
        else:
            print("Invalid input, please enter either n s e or w")


play_game(player1)
