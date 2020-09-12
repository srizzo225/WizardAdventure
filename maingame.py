import time  # Allows for use of the 'sleep' function to create pauses in the game's narration. Good for keeping a readable pace!
import random  # Allows for use of the 'randint' function to generate a seed for the RandomEvent module's random events to remain unpredictably random.
import sys  # Allows use of the exit() function to end the client.
import globalvariables  # imports the global variables
import intro01
import forrest02
import orc03
import puzzle04
import wizard05

def main():

    globalvariables.gVariables()  # initializes the global variables

    answer = input("Would you like to start playing (Yes/No)? ")
    if answer.casefold() == "no":
        globalvariables.continue_playing = False
        print("I'm not sure why you started the game... Good bye!")

    while globalvariables.continue_playing:
        intro01.main()
        if globalvariables.shop_success and globalvariables.pub_success:
            forrest02.main()
            if globalvariables.forrest_success:
                orc03.main()
                if globalvariables.orc_success:
                    puzzle04.main()
                    if globalvariables.puzzle_success:
                        wizard05.main()
                        if globalvariables.wizard_success:
                            print("Congrats you completed the game")
                            answer = input("Would you like to restart the game (Yes/No)? ")
                            if answer.casefold() == "no":
                                globalvariables.continue_playing = False
                                print("Great playing with you. Good bye!")
                    else:
                        print("you woke up back in the forrest!")
                        forrest02.main
                            #else:
                            #print("The wizard blasted you back to the forrest!")
                            #forrest02.main
if __name__ == "__main__":
    main()