import globalvariables  # imports the global variables
import time

def main():
    print("Now that you have your sword and an idea of where the wizard is, you leave town.")
    time.sleep(1.5)
    print("You head towards the forrest. It's super spooky scary!")
    time.sleep(1.5)
    print("As you move foward, you look around. It's so dark! You lose sight of the trail.")
    time.sleep(1.5)
    print("You worry if you'll ever make you way out of this maze...")
    time.sleep(1.5)
    sq2()

def sq1():
    x = input("Do you want to go right or down? ")
    if x.casefold() == "right":
        sq2()
    elif x.casefold() == "down":
        sq4()
    else:
        print("Huh? Which way did you want to go? ")
        sq1()

def sq2():
    x = input("Do you want to go left, right, or down? ")
    if x.casefold() == "left":
        sq1()
    elif x.casefold() == "right":
        sq3()
    elif x.casefold() == "down":
        sq5()
    else:
        print("Huh? Which way did you want to go? ")
        sq2()

def sq3():
    x = input("Do you want to go left or down? ")
    if x.casefold() == "left":
        sq2()
    elif x.casefold() == "down":
        sq6()
    else:
        print("Huh? Which way did you want to go? ")
        sq3()

def sq4():
    x = input("Do you want to go up, right, or down? ")
    if x.casefold() == "up":
        sq1()
    elif x.casefold() == "right":
        sq6()
    elif x.casefold() == "down":
        sq7()
    else:
        print("Huh? Which way did you want to go? ")
        sq4()

def sq5():
    x = input("Do you want to go up, right, left, or down? ")
    if x.casefold() == "up":
        sq2()
    elif x.casefold() == "right":
        sq6()
    elif x.casefold() == "left":
        sq4()
    elif x.casefold() == "down":
        sq8()
    else:
        print("Huh? Which way did you want to go? ")
        sq5()

def sq6():
    x = input("Do you want to go up, left, or down? ")
    if x.casefold() == "up":
        sq3()
    elif x.casefold() == "left":
        sq5()
    elif x.casefold() == "down":
        sq9()
    else:
        print("Huh? Which way did you want to go? ")
        sq6()

def sq7():
    x = input("Do you want to go up or right? ")
    if x.casefold() == "up":
        sq4()
    elif x.casefold() == "right":
        sq8()
    else:
        print("Huh? Which way did you want to go? ")
        sq7()

def sq8():
    x = input("Do you want to go left, right, or up? ")
    if x.casefold() == "left":
        sq7()
    elif x.casefold() == "right":
        sq9()
    elif x.casefold() == "up":
        sq5()
    else:
        print("Huh? Which way did you want to go? ")
        sq8()

def sq9():
    x = input("Do you want to go left, right, or up? ")
    if x.casefold() == "left":
        sq8()
    elif x.casefold() == "right":
        print("Finally! You found your way out of the forrest! Yayyyyy!")
        globalvariables.forrest_success = True
    elif x.casefold() == "up":
        sq6()
    else:
        print("Huh? Which way did you want to go? ")
        sq9()




if __name__ == "__main__":
    main()