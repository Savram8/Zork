#This is the famous game of Zork written in python but with a little bit of my own added flair. 
import sys

def intro_text():
    print("ZORK I: The Great Underground Empire")
    print("Copyright (c) 1981, 1982, 1983 Infocom, Inc. All rights reserved.")
    print("ZORK is a registered trademark of Infocom, Inc.")
    print("Revision 88 / Serial number 840726")
    print("HOW TO PLAY: Enter your commands by the >>> prompt")
    print("Commands to use: walk + direction, Open, Pick up, Hit, Throw, Talk, inventory, take, look , walk")   



#11 Comamands to choose from.


direction = 5
inventory = []

intro_text()


print("------------------------------------------------------------------------------------")
print("West of House")
print("You are standing in an open field west of a white house, with a boarded front door.")
print("There is a small mailbox in front of you.")



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
                print("You walk up to the white house, the front door is locked. The door looks weak though, a swift kick would be able to open it.")
                direction = 2
            
            elif choice.lower() == "walk east":
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

            else:
                print("Commands to use: walk + direction, Open, Pick up, Hit, Throw, Talk, inventory, take, look , walk")




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

            elif choice2.lower() == "look":
                print("You look at the door, I'm pretty sure if you kicked it. You might be able to squeeze by.")
                
            elif choice2.lower() == "no":
                 print("You turn around and walk back to the start of Zork. Kinda a bitch move...")
                 direction = 5


            elif choice2.lower() == "take":
                print("You put the key in your inventory. You see a silver door. Walk to the door maybe?")
                inventory.append("Silver key")

            elif choice2.lower() == "talk":
                print ("Talk to who? There is no one around? Are you okay?")


            elif choice2.lower() == "inventory":
                print(inventory)
            
            else:
                print("Commands to use: walk + direction, Open, Hit, Throw, Talk, inventory, take, look , walk")


#Yes in the house, This leads to death.
    if direction == 6:
        while direction == 6:
            print(" ")
            choice3 = input(">>> ")

            if  choice3.lower() == "look":
                print("You look around and see old dining room. Cobwebs everywhere. You see a Silver key in the middle of the table. The room is grey and looks old, a silver door shines behind the table. hmmm, that's intresting:")

            elif choice3.lower() == "inventory":
                print(inventory)
            
            elif choice3.lower() == "walk":
                print("You walk across the room to the silver door. But it's locked... Maybe take the silver key on the table?")

            elif choice3.lower() == "take":
                print("You put the key in your inventory. You see a silver door. Walk to the door? yes or no")
                inventory.append("Silver key")

            elif choice3.lower() == "yes":
                print("You walk towards the door, You take the key out of your inventory and you unlock the door. You are greeted with a open celler, with stairs leading you down. You go below and you are in a poorly light tunnel. At the end of the tunnel is a door. I have a weird feeling about this door...... Open? or Run? ")
                inventory.remove("Silver key")

            elif choice3.lower() == "open":
                print("You open the door and a loud flash goes off. Dead. A masked figure stands there, shotgun in hand")
                print("   ")
                print("************************GAME OVER************************")
                direction = 8 

                
            elif choice3.lower() == "run":
                 print("Good choice, I have a weird vibe about that door. Lets return to the start!")
                 print("**********************************************************************************")
                 intro_text()

                 direction == 5

            elif choice3.lower() == "no":
                    print("you get scared and climb back up. You hear a noise as you are running back. You run back to where you started. Now what.....")
                    direction = 5

            elif choice3.lower() == "hit":
                print("hit what?")

            elif choice3.lower() == "throw":
                print("hit what?")

            elif choice2.lower() == "inventory":
                print(inventory)
            else:
                print("Commands to use: walk + direction, Open, Pick up, Hit, Throw, Talk, inventory, take, look , walk")



    #If you end up going east
    if direction == 4:
        while direction == 4:
            print(" ")
            choice4 = input(">>> ")

            if choice4.lower() == "look":
                print("you see a raft, do you want to get on it? Yes or no?")
            
            elif choice4.lower() == "hit":
                print("why would you hit the raft? I don't understand")

            elif choice4.lower() == "take":
                print("Listen... I'm not sure how to break it to you, but that raft is fucking massive. I doubt we can carry that")
            
            elif choice4.lower() == "walk":
                print("We can either get on the raft or go back. Do you want to get on the raft? Yes or no?")
            elif choice4.lower() == "inventory":
                print(inventory)
            elif choice4.lower() == "throw":
                print("throw what?")
            elif choice4.lower() == "open":
                print("what do you want to open?")
            elif choice4.lower() == "talk":
                print("uhhhh... Nobody is here... Are you ok?")
            elif choice4.lower() == "yes":
                print("You get on the raft and start to paddle away. You start to doze off and you fall asleep for a couple hours. Enter wake whenever you want to wake up")
                print("Zzzzzz")
                print("Zzzzzz")
                print("Zzzzzz")
            elif choice4.lower() == "no":
                print("Thats fine, there is nothing else here. Lets return to the beginning, shall we?")
                direction = 5
            elif choice4.lower() == "wake":
                print("You awake, it's dark and you are in the middle of the ocean. You feel something bumping the raft. You lean over the raft to try and catch a peek at whatever it is. As you lean over, a massive shark grabs you and pulls you under.")
                print("********** GAME OVER *************")
                print(" ")
                direction = 8
            else:
                 print("Commands to use: walk + direction, Open, Pick up, Hit, Throw, Talk, inventory, take, look , walk")



                








    #Ending
    if direction == 8:
        while direction == 8:
            print(" ")
            print("Do you want to play again? yes or No")
            choice8 = input(">>> ")


            if choice8.lower() == "yes":
                print("Lets go!")
                direction = 5
            elif choice8.lower == "no":
                print("Thanks for playing!")
                sys.exit()
            else:
                print("Let me make this easy for you since you are having trouble understanding. Type yes, if you want to play again! Type No, if you don't want to play anymore. Simple!")

                



                
                

                    

        

                



                
            


            



            



    