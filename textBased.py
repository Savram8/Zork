#This is the famous game of Zork written in python but with a little bit of my own added flair. 

print("ZORK I: The Great Underground Empire")
print("Copyright (c) 1981, 1982, 1983 Infocom, Inc. All rights reserved.")
print("ZORK is a registered trademark of Infocom, Inc.")
print("Revision 88 / Serial number 840726")
print("HOW TO PLAY: Enter your commands by the >>> prompt")
print("Commands to use: walk + direction, Open, Pick up, Hit, Throw, Talk, inventory, take, look , walk")

#11 Comamands to choose from.


direction = 5
inventory = []


print("------------------------------------------------------------------------------------")
print("West of House")
print("You are standing in an open field west of a white house, with a boarded front door.")
print("There is a small mailbox in front of you.")

#Direction 1 = North
#Direction 2 = West
#Direction 3 = South 
#Direction 4 = North
#Direction 5 = North

player = "yes"


#Main Story Line
while player == "yes":
    if direction == 5:
        while direction == 5:
    
            print(" ") 
            choice = input(">>> ")
            if choice.lower() == ("walk"): #First Command
                print("Walk in which direction?")

            elif choice.lower() == ("walk north"): 
                print('You walk into the forest, the sounds of birds are chirping, the forest is wet and smells nice.')
                direction == 1

            elif choice.lower() == ("walk west"):
                print("You walk up to the white house, the front door is boarded up.")
                direction = 2
            
            elif choice.lower() == "Walk east":
                print("You walk towards the ocean, you find a nice raft and a paddle.")
                direction = 4

            elif choice.lower() == "Walk south":
                print("You walk away from the house and towards the forbidden forest. This is a dangerous area. Are you sure you want to enter?")
                direction = 3
                
            elif choice.lower() == "open":
                print("you look at the mailbox, it does not have a lock. You open it up and inside find a Jade key. You put it in your inventory. Where to next?")
                inventory.append("Jade key")

            elif choice.lower() == "take":
                print("You take the mailbox and put it in your inventory. It's kind of heavy. ")
                inventory.append("Mailbox")

            elif choice.lower() == "look":
                print("You look around, to the north is the forest, nothing too special. To the South is the Forbidden Forest, looks scary. To the east, is the ocean. Looks calming. To the west, is the white house. Where to? ")

            elif choice.lower() == "hit":
                print ('Hit what??')

            elif choice.lower() == "throw":
                print ('Throw What??')

            elif choice.lower() == "inventory":
                print (inventory)



    # If you Walk West, The house
    if direction == 2:
        while direction == 2:
            print(" ")
            choice2 = input(">>> ")

            if choice2.lower() == "hit":
                print("You hit the door, it cracks open a bit. Enough for you to squeeze by. Do you enter? Yes or No? ")

            elif choice2.lower() == "yes":
                print("You squeeze through the opening. The room is dark and smells musty. You look around for a light. You flick on the light")
                direction = 6
                 
                
            elif choice2.lower() == "no":
                 print("You turn around and walk back to the start of Zork. Kinda a bitch move...")
                 direction = 5


            elif choice2.lower() == "take":
                print("You put the key in your inventory. You see a silver door. Walk to the door maybe?")
                inventory.append("Silver key")

            elif choice2.lower() == "walk":
                print("You walk towards the door, You take the key out of your inventory and you unlock the door. You are greeted with a open celler, with stairs leading you down. You go below and you are in a poorly light tunnel. Keep walking, Yes or no?")
                inventory.remove("Silver key")
            
            elif choice2.lower() == "n":
                    print("you get scared and climb back up. You hear a noise as you are running back. You run back to where you started. Now what.....pussy")
                    direction = 5
            elif choice2.lower() == "y":
                     print("You walk down the tunnel, You hear a loud growling as approach the end of the hallway. When you reach the end, you find just a wall. When you turn around, you hear a Bang and a flash of light. You die instantly. You lose....")
                     break   


#Yes in the house, This leads to death.
    if direction == 6:
        while direction == 6:
            print(" ")
            choice3 = input(">>> ")

            if  choice3.lower() == "look":
                print("You look around and see old dining room. Cobwebs everywhere. You see a  Silver key in the middle of the table. The room is grey and looks old. Nothing much is here:")

            elif choice3.lower() == "take":
                print("You put the key in your inventory. You see a silver door. Walk to the door maybe?")
                inventory.append("Silver key")
                
            elif choice3.lower() == "hit":
                print("hit what?")

            elif choice3.lower() == "throw":
                print("hit what?")

            
            

                

    

            



            
            


            



            



    