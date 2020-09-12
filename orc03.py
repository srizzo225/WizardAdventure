import random
import globalvariables
import time

playerHP = 20
orcHP = 12

def main():
    print("CHAPTER THREE")
    time.sleep(1.5)
    print("Phew. You made it out of the forrest.")
    time.sleep(1.5)
    print("Uh oh. What's that sound?")
    time.sleep(1.5)
    print("An orc! Get ready to attack!")
    battlesequence(playerHP, orcHP)

def hitdice():
    d12 = random.randrange(1, 13)
    return d12

def diceattack():
    d20 = random.randrange(1, 20)
    return d20

def orcattack(playerHP, orcHP):
    roll = diceattack()
    if roll == 1:
        orcHP = 0
        print("The orc got confused and ran away!")
    elif roll == 20:
        print("Oh no! The orc sliced you in half.")
        playerHP = 0
    elif 2 <= roll <= 10:
        print("Phew! The orc missed you!")
    else:
        print("Uh oh, the orc hit you!")
        playerHP -= hitdice()
    print("Your health is ", playerHP)
    return playerHP, orcHP

def playerattack(playerHP, orcHP):
    roll = diceattack()
    if roll == 1:
        playerHP = 0
        print("Oh no! You tripped and stabbed yourself. Womp womp.")
    elif roll == 20:
        print("Alrght! You sliced you in half.")
        orcHP = 0
    elif 2 <= roll <= 10:
        print("Ugh, your attack missed the orc.")
    else:
        print("Nice! You hit the orc")
        orcHP -= hitdice()
    time.sleep(1.5)
    print("The orc's health is ", orcHP)
    return playerHP, orcHP

def battlesequence(playerHP, orcHP):
    while orcHP > 0 and playerHP > 0:
        print("Your turn:")
        time.sleep(1.5)
        playerHP, orcHP = playerattack(playerHP, orcHP)
        time.sleep(1.5)
        print("your health is", playerHP, "The orc's health is", orcHP)
        time.sleep(1.5)
        if orcHP <= 0:
            print("Yay! You defeated the orc!")
            globalvariables.orc_success = True
        else:
            print("The orc's turn:")
            time.sleep(1.5)
            playerHP, orcHP = orcattack(playerHP, orcHP)
            time.sleep(1.5)
            print("your health is", playerHP, "The orc's health is", orcHP)
            time.sleep(1.5)
            if playerHP <= 0:
                print("you lost! the end")


#playerHP, orcHP = playerattack(playerHP, orcHP)
#playerHP, orcHP = orcattack(playerHP, orcHP)
#print(playerHP, orcHP)

#orcattack(playerHP, orcHP)

if __name__ == "__main__":
    main()