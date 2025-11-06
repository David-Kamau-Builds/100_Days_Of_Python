print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Castle of the Lost Crown.Your mission is to find the Lost Crown.")
print("You have just entered the Castle and see two staircases. One goes upstairs the other downstairs.")
downOrUp = input("Do you want to go upstairs or downstairs? ").strip().lower()

if downOrUp == "upstairs":
    print("Great Choice 🫡")
    doorQuestion = input(
        "You go up the stairs and see a door, a library ahead and a vast hallway. What do you do? (Open door/ Head to library/ Navigate the hallway): ").strip().lower()
    if doorQuestion == "Open door":
        print("It's a trap! Game Over. ⚰️")
    elif doorQuestion == "Navigate the hallway":
        print("You get lost in the maze of halls. Game Over. ⚰️")
    elif doorQuestion == "Head to library":
        print("You are almost there. 🤏")
        bookColour = input(
            "You enter the library and see a shelf with 3 books. Red, Green, Blue. What book colour do you pick?: ").strip().lower()
        if bookColour == "Red":
            print("You fall asleep reading about flange joints and miss your chance. Game Over. ⚰️")
        elif bookColour == "Green":
            print("The floor gives way. Game Over. ⚰️")
        elif bookColour == "Blue":
            print("The book opens a secret passage. 🚪")
            print("The passage is locked. The key is a Riddle.")
            print("The Riddle: I am heavier than any stone in the wall, but a breeze can take me. ")
            print("\t\t\tI have been owned by every King but cannot be taken to the grave. ")
            passageRiddle = input(
                "\t\t\tI am worth more than the Crown you seek, yet I can be broken by a whisper.What am I? (A Promise/ A Secret/ Trust/ Reputation): ").strip().lower()
            if passageRiddle == "A Promise":
                print("You Win! You found the Lost Crown. 🥳💰💰💰💰")
            elif passageRiddle == "A Secret":
                print("The passage seals itself forever. You are trapped in an uncomfortable, dusty corridor. ⚰️")
            elif passageRiddle == "Trust":
                print("The passage seals itself forever. You are trapped in an uncomfortable, dusty corridor. ⚰️")
            elif passageRiddle == "Reputation":
                print("The passage seals itself forever. You are trapped in an uncomfortable, dusty corridor. ⚰️")
            else:
                print("The Passage locks and the alarm sounds. Game Over. ⚰️")
        else:
            print("The walls cave in on you. Game Over. ⚰️")
    else:
        print("A guard finds you. Game Over. ⚰️")
elif downOrUp == "downstairs":
    print("Encounter a Guard. Game Over. ⚰️")
else:
    print("You stumble in the dark forever. Game Over. ⚰️")