#chapter 1 shop module
#Last edit 2020-09-06

import globalvariables  # imports the global variables
import time


def main():
    print("You are a pesant in a small village. You live with your mom, dad, and sister.")
    time.sleep(1.5)
    print("One day, you are in the kitchen making dinner.")
    time.sleep(1.5)
    print("You ask your sister to run out to the garden to grab some fresh basil to complete the lovely meal you're cooking.")
    time.sleep(1.5)
    print("A few minutes later you hear a comotion. What's that sound?")
    time.sleep(1.5)
    print("You look out the window and see a wizard laughing and then run off")
    time.sleep(1.5)
    print("You go outside to see what happened to your sister and don't see her right away. Then you hear a screachy sound.")
    time.sleep(1.5)
    print("You look down and see that wizard turned your sister into a possum!")
    time.sleep(1.5)
    print("While possums are cute, they can't do chores, so I guess you'll have to head into town and figure out how to fix this.")
    time.sleep(1.5)
    places()
    
def places(): 
    whereto = input("Do you want to head to the shop or pub? ")   
    if whereto.casefold() == "shop":
        shop()
    elif whereto.casefold() == "pub":
        pub()
    else:
        print("Sorry, it's not a big town. It's just the pub or shop.") 
        places()

def shop():
    welcome = input("Welcome to the town shop. Are you off to fight the wizard? yes/no ")
    if welcome.casefold() == "yes":
        print("Shopkeeper: That's great! That wizard is so annoying. It's dangerous to go in to the forrest without a weapon. Take this!")
        time.sleep(1.5)
        print("Narrator: The shopkeeper gave you a sword! It does +2 damage on attacks!")
        globalvariables.shop_success = True
        if globalvariables.pub_success == False:
            places()
    elif welcome.casefold() == "no":
        print("Shopkeeper: That's too bad. I can't stand that wizard. Also maybe you should help your sister?")
        time.sleep(1.5)
        places()
    else:
        print("Shopkeeper: Sorry, I don't understand.")
        time.sleep(1.5)
        shop()

def pub():
    print("You walk into the pub. You see your pal Ian and explain what happened.")
    time.sleep(1.5)
    print("Ian is shocked! He doesn't know much about the wizard, but the bartender Dasha over heard you.")
    time.sleep(1.5)
    print("Dasha is a retired rogue! She knows all about the wizard.")
    time.sleep(1.5)
    print("Dasha explains that to defete the wizard you will need to find your way through the forrest.")
    time.sleep(1.5)
    print("Who knows what's in there! Watch out for monsters.")
    time.sleep(1.5)
    print("Then, you'll stumble upon the wizard's cave, but he keeps it pretty locked down.")
    time.sleep(1.5)
    print("Dasha isn't sure what kind of security the wizard uses these days, but it might be tricky!")
    time.sleep(1.5)
    print("Finally, Dasha explains, you'll get to the wizards lair. The wizard isn't super strong, but he's got some powerful magic.")
    time.sleep(1.5)
    print("you'll need to be quick on your feet to doge the Wizard's spells") 
    time.sleep(1.5)
    print("but it you get in low, you should be able to knock down the Wizard real easy!")
    time.sleep(1.5)
    print("You thank Dasha, and leave the pub.") 
    time.sleep(1.5)
    print("You're starting to doubt your choice to help your sister, but it's too late to turn back now!")
    globalvariables.pub_success = True
    if globalvariables.shop_success == False:
        places()

if __name__ == "__main__":
    main()
