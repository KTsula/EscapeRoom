# room1.py
# The function draws and activates a room1
import time
from graphics import *
from button import Button
from widgets import storytell
import time

def room1(win, inventory):

  # setting base variables
    continueGame = True
    lost = False

  # drawing room
    img1 = Image(Point(20, 10), "room1.gif")
    img1.draw(win)

  # drawing user
    user = Image(Point(20,1), "thief.gif")
    user.draw(win)
  
  # drawing inventory label
    inventLabel = Text(Point(5, 19), "Inventory")
    inventLabel.setStyle("bold")
    inventLabel.draw(win)

  # drawing a button that says that a person can put an item into inventory by pressing g
    get_item = Button(win, Point(5,2), 8, 2, "Get Item by Pressing <g>")

  # drawing inventory items
    inventoryTexts = []
    last = 17
    for x in inventory:
        inventoryTexts.append(Text(Point(5,last), x))
        last = last - 1
    for x in inventoryTexts:
        x.draw(win)

    # setting up the key items for the room and what can be collected
    main_item = 'candle'
    things_in_room = {"Point(21.0,11.0)": "candle", "Point(28.0,3.0)": "candle", "Point(12.0,2.0)": "plant"}

    # storytell


    # Storytell The beginning
    storytell(win,
          "The house has one of the safest designs. So, all the doors are locked and once you get to another room you can't go back (they lock automatically once you close the door). In order to unlock the door of the following room, you must find a hidden object in each of the rooms.")
    storytell(win,
          "A thief just accessed the house and sees a letter on the Table: 'Dear Mom, I have left for you 3 bars of gold in the safe located in our room. In order to open it, you have the code we gave you last week. If you forgot the code, each room of the house (if you go on the right order), poses a clue to the password. Hope you dont have any trouble. Love, your daughter and John.'")


    while continueGame is True and lost is False:

        # ask for key input (arrows)
        k = win.getKey()
        # check which arrow was pressed and move the user accordingly 
        # while also checking that the user doesn't go outside the room's
        # borders
        if k == "Right" and user.getAnchor().getX() != 30:
            user.move(1, 0)
        if k == "Left" and user.getAnchor().getX() != 10:
            user.move(-1, 0)
        if k == "Up" and user.getAnchor().getY() != 20:
            user.move(0, 1)
        if k == "Down" and user.getAnchor().getY() != 0:
            user.move(0, -1)

        if k == 'G' or k == 'g':
          if get_item.active:
              inventory.append(item)
              inventoryTexts.append(Text(Point(5, last), item))
              last = last - 1
              inventoryTexts[-1].draw(win)

        # Getting user location
        usx = user.getAnchor().getX()
        usy = user.getAnchor().getY()

        user_pos = "Point({0},{1})".format(usx, usy)
        # Activating a pickup button if the user is standing on a candle
        if user_pos in things_in_room.keys() and things_in_room[user_pos] not in inventory:
            item = things_in_room[user_pos]
            get_item.activate()
        else:
            get_item.deactivate()
          
        # checks that if user tries to go through the 
        # left door, he/she dies
        if usx == Point(10.0, 7.0).getX() and usy == Point(10.0, 7.0).getY():
          storytell(win,"The thief went into the living room and the dog got woken up and barked till the neighbours came. You loose! The thief got arrested.")
          continueGame = False

        # checking the ladder
        if usx >= Point(10.0, 17.0).getX() and usx<= Point(16.0, 17.0).getX() and usy >= Point(10.0, 17.0).getY() and usy <= Point(10.0, 20.0).getY():
            # checking if a user has essential item
            if main_item in inventory:
                # delete the room picture on the screen
                storytell(win,"Good Job! You passed the first room and had a candle in your inventory that helped you see in on the dark stairs. Now you move to another room.")
                user.undraw()
                img1.undraw()
                for i in inventoryTexts:
                    i.undraw()
                get_item.undrawButton(win)
                # and return the state
                return True, False, inventory
            else:
                storytell(win,"The stairs were too dark and the thief fell down, opened his head and layed unconscious until the owners came back. Next, he was arrested.")
                return False, True, inventory





    return continueGame, lost, inventory