from room import Room
from player import Player
from item import Item
from item import Sword
from item import Shield

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"  ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Jin", room["outside"])

player_input = ""

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


while True:
    print(player.room.name)
    print(player.room.description)
    print(player.room.items)
    player_input = input(f"Choose north, south, east, or west.")
    if player_input.lower() == "n":
        if hasattr(player.room, "n_to"):
            player.room = player.room.n_to
        else:
            print (f"-------{player_input} is an invalid input. Please choose again.-------")
    elif player_input.lower() == "s":
        if hasattr(player.room, "s_to"):
            player.room = player.room.s_to
        else:
            print (f"-------I'm sorry. {player_input} is an invalid input. Please choose again.-------")
    elif player_input.lower() == "e":
        if hasattr(player.room, "e_to"):
            player.room = player.room.e_to
        else:
            print (f"-------I'm sorry. {player_input} is an invalid input. Please choose again.-------")
    elif player_input.lower() == "w":
        if hasattr(player.room, "w_to"):
            player.room = player.room.w_to
        else:
            print (f"-------I'm sorry. {player_input} is an invalid input. Please choose again.-------")
    elif player_input.lower() =="q":
        print (f"Quitting game.....")
        print (f"Thanks for playing!")
        break
    else:
        print("Invalid")