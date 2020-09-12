import globalvariables 
import time

def main():
    print("CHAPTER 5")
    time.sleep(1.5)
    print("Woah! When you solved all the puzzles a door to the Wizard's lair opened up!")
    time.sleep(1.5)
    print("Wizard: Who's there?")
    time.sleep(1.5)
    print("You shout that you're here to get our sister turned back into a human")
    time.sleep(1.5)
    print("Oh that? Eh, are you sure about that? Possums are pretty cute and eat ticks!")
    time.sleep(1.5)
    print("Hmm. The wizard does have a point, but no! You need help with chores.") 
    time.sleep(1.5)
    print("Also who goes around turning people into possums?")
    time.sleep(1.5)
    print("Fiiiiiine. If you can beat me I'll turn your sister back.")
    time.sleep(1.5)
    battle()

def battle():
    attack = input("Do you want to jump, duck, or punch the wizard in the tummy? (jump/duck/punch): ")
    if attack.casefold() == "jump":
        time.sleep(1.5)
        print("Ehhhh. What was your plan there?")
        time.sleep(1.5)
        print("All you did was make the wizard laugh!")
        time.sleep(1.5)
        battle()
    elif attack.casefold() == "duck":
        duck()
    elif attack.casefold() == "punch":
        print("BAHAHAHA. The wizard is doubled over laughing at your poor choice.")
        print("The wizard blasts you back to the forrest!")
    else:
        print("You really only have three choices here.")
        battle()

def duck():
    time.sleep(1.5)
    print("Good choice!")
    time.sleep(1.5)
    print("The same time you ducked, the wizard cast a spell!")
    time.sleep(1.5)
    print("But it bounced off the wall and hit the wizard!")
    time.sleep(1.5)
    print("The wizard yelps in pain.")
    time.sleep(1.5)
    print("ugh. I guess I'll change your sister back.")
    time.sleep(1.5)
    print("The wizard snaps his fingers.")
    time.sleep(1.5)
    print("You are transported back to your home, but where's your sister?")
    time.sleep(1.5)
    print("You look out the window- she's back in the garden!")
    time.sleep(1.5)
    print("It's as if nothing happened! Phew. You're glad to see everything is back to normal.")
    time.sleep(1.5)
    print("For now anyway... you didn't actually defeate the wizard.")
    time.sleep(1.5)
    print("But that's a challenge for another day. For now, dinner time!")
    time.sleep(1.5)
    print("THE END.")
    globalvariables.wizard_success = True

if __name__ == "__main__":
    main()