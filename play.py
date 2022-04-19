# play.py
# the program storytells between the rooms and also activates rooms
import time
from room1 import room1
from room2 import room2
from room3 import room3
from room4 import room4
from room5 import room5
from widgets import storytell
import time

def play(win, inventory, lost):
    lost = False
    continueGame = True
  # first room gets activated
    continueGame, lost, inventory = room1(win, inventory)
  # after first room is exited the below code checks for the variables
  # and if a person lost or continueGame is False we stop the game.
    if continueGame is False:
        return continueGame, lost

    # if the above code is passed without closing the game then here we need to activate a room2
    continueGame, lost, inventory = room2(win, inventory)

    if continueGame is False:
        return continueGame, lost

    # if the above code is passed without closing the game then here we need to activate a room3
    continueGame, lost, inventory = room3(win, inventory)

    if continueGame is False:
        return continueGame, lost

    # if the above code is passed without closing the game then here we need to activate a room4

    continueGame, lost, inventory = room4(win, inventory)

    if continueGame is False:
        return continueGame, lost

    continueGame, lost, inventory = room5(win, inventory)

    return continueGame, lost

