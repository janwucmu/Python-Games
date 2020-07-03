import time
import random
import sys

# game function
def game():
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Welcome to the cavern of secrets!")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)
    print ("You enter a dark cavern out of curiosity. It is dark and you can only find a sharp stick on the floor.")
    stick_decision = input("Do you take it? [y/n]: ")

    # STICK TAKEN
    if stick_decision in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You have taken the stick!")
        time.sleep(2)
        stick = True
    # STICK NOT TAKEN
    else:
        print("You did not take the stick")
        stick = False

    print ("As you proceed further into the cave, you hear a groaning")
    approach_decision = input("Do you approach it? [y/n]")

    # APPROACH Zombie
    if approach_decision in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print ("You approach the object...")
        time.sleep(2)
        print ("As you draw closer, you realize that the groaning sound is coming from a...")
        time.sleep(1)
        print ("ZOMBIE!")
        fight_decision = input("Do you try to fight it? [y/n]")

        # FIGHT Zombie
        if fight_decision in ['y', 'Y', 'Yes', 'YES', 'yes']:
            # WITH STICK
            if stick == True:
                print ("You only have a stick to fight with!")
                print ("You quickly jab the Zombie in it's eye and gain an advantage")
                time.sleep(2)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print (" Fighting... ")
                print (" You must guess the number the zombie picked ")
                print ("  If it is within 1 off: you will kill it ")
                print ("  If it is within 5 off: you will manage to hurt it and escape ")
                print ("  OR ELSE...HE WILL KILL YOU ")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                guess = int(input("Pick a number from 1-20. Choose wisely! Your life depends on it! "))
                zombie_num = random.randint(1, 20)

                if (guess >= (zombie_num - 1)) and (guess <= (zombie_num + 1)):
                    print ("You killed the Zombie!")
                    print ("You managed to get out! YAY!")
                
                elif (guess >= (zombie_num - 5)) and (guess <= (zombie_num + 5)): 
                    print ("Phew you guess close enough. The zombie is not dead, but you manage to escape") 
                    print ("RUN BEFORE HE GETS BACK UP!")
                    
                else: 
                    print ("RIP, looks like you weren't close enough")
                    print ("Better luck next time :)") 
                time.sleep(1)
                sys.exit(0)
            # NO STICK
            else:
                print ("You don't have anything to fight with!")
                print ("Should of picked up the stick right?")
                time.sleep(2)
                print ("Zombie gave you a chance. Make sure you answer this correctly!")
                guess = input("What was Python named after? [show/snake/person] ")
                if guess == "show":
                    print ("Wow you are correct! Did you know or was it just pure luck")
                elif guess == "snake":
                    print ("OOP YOU GOT TRICKED!")
                else:
                    print ("Nope, sorry you had your chance")
                print ("The language’s name isn’t about snakes, but about the popular British comedy troupe Monty Python (from the 1970s).")
                print ("Guido van Rossum, the creator of Python, is a big fan of Monty Python’s Flying Circus. ")
                time.sleep(1)
                sys.exit(0)
        
        #DON'T FIGHT Zombie
        else:
            print ("You chose not to fight the Zombie.")
            time.sleep(1)
            print ("As you turn away, it ambushes you and impales you with it's fangs!!!")
            time.sleep(1)
            sys.exit(0)
    # DON'T APPROACH Zombie
    else:
        print ("You turn away from the groaning sound, and attempt to leave the cave...")
        time.sleep(1)
        print ("But suddenly something breaks your neck from behind. You fall to the ground and die.")
        time.sleep(1)
        sys.exit(0)
    
game()
