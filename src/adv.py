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
room["outside"].addItem(
    {"name": "sword", "description": "It's dangerous to go alone: take this!"}
)

room["foyer"].addItem(
    {"name": "Potion", "description": "Restores a minor amount of health"}
)
room["foyer"].addItem(
    {"name": "Tent", "description": "Allows you to camp in certain areas"}
)
room["overlook"].addItem({"name": "fossil", "description": "a rare item"})
room["narrow"].addItem({"name": "bow", "description": "ranged weapon"})
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
        print(f"\n{player.room.name}")
        print(player.room.description)
        print(
            f"Your investigation of the room shows you it contains a: {player.room.printItems()}"
        )
        print(f"Your current inventory is: {player.printItems()}")
        player_move = (
            input(
                "What would you like to do? Go N S E W, or take or drop items, or press q to quit: "
            )
        ).lower()
        player_move_arr = player_move.split(" ")
        if len(player_move_arr) == 1:
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
                print(
                    "Invalid input, please enter either n s e or w, or q to quit, or take or drop items"
                )
        elif len(player_move_arr) == 2:
            if player_move_arr[0] == "take":
                for item in player.room.inventory:
                    if item.name == player_move_arr[1]:
                        player.room.dropItem(item)
                        player.addItem(item)
            elif player_move_arr[0] == "drop":
                for item in player.inventory:
                    if item.name == player_move_arr[1]:
                        player.dropItem(item)
                        player.room.addItem(item)
        else:
            print(
                "Invalid operation: please enter either n s e or w, or q to quit, or take or drop items"
            )


play_game(player1)
