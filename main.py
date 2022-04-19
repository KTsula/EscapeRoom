# main.py
# This is the starting file for a mini python escape room game
# It uses graphics.py package.
# main.py activates play.py and play.py activates different rooms and checks the conditions in between.
# each room is displayed with different functions and the logic varies from room to room
# but the inventory is static and the player receives the time it took them to finish the game as a final rating.

from graphics import *
import time
from widgets import storytell
from play import play
import time

# a function for clearing a whole window
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def main():
    # if continueGame becomes False, we terminate a game and check the variable lost
    continueGame = True
    # if lost is True then we show a person that he lost
    # if lost is False but the game got terminated then he won
    lost = False
    # we enter the timer

    #creating a window
    win = GraphWin("Escape Room", 600, 400)
    win.setCoords(0, 0, 30, 20)
    win.setBackground('brown')
    # we create an empty directory first (here I put some stuff just to check if it works right)
    inventory = []

    #starting timer
    startTime = time.time()


    # The main function that keeps the game going
    while continueGame == True:
        # play is a function defined in play.py
        # play returns continueGame and lost variables in case something changes in them
        continueGame, lost = play(win, inventory, lost)


    endTime = time.time()
    timepassed = endTime - startTime

    if lost:
        storytell(win, "you needed {} seconds to finish the game and you lost".format(round(timepassed)))
    else:
        storytell(win, "you needed {} seconds to finish the game and you won".format(round(timepassed)))

    win.close()

if __name__ == '__main__':
    main()
