print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("You're at a crossroad.  Go left or right? ")
if direction == "left":
    action = input("You come to a lake.  There is an island in the middle of the lake.  Type 'wait' to wait for a boat or 'swim' to swim across.")
    if action == "wait":
        door = input("You arrive at the island unharmed.  There is a house "
                    + "with 3 doors.  One red, one yellow, one blue.  Which "
                    + "color do you choose? ")
        if door=="yellow":
            print("You find a massive chest... full of treasure.  You win!!!!")
        elif door=="red":
            print("The room you enter is engulfed in flames and you die.  Game over.")
        elif door == "blue":
            print("Upon entering the room it is eerily quiet...  until a low growl is heard... "
                " then multiplies...  grows louder.  You are swarmed by a pack"
                " of beasts and eaten alive.  Game over.")
        else:
            print("You fail to choose a door and slowly die on the island.  Game over.")
    else:
        print("On your swim you are approached by a fish...  a trout.  "
            + "  The trout attacks and you die.  Game over.")
else:
    print("You fall into a hole and are dead.  Game over.")
