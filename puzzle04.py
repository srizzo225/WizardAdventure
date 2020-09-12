#This module is for the puzzles in chapter 4
#Last edited 2020-08-23

import globalvariables  # imports the global variables
import time

def puzzle1():
    time.sleep(1.5)
    print("PUZZLE 1")
    time.sleep(1.5)
    print("Mr. and Mrs. Mustard have six daughters and each daughter has one brother.")
    time.sleep(1.5)
    answer = int(input("How many people are in the Mustard family?"))
    if answer == 9:
        print("Correct! Here is a key")
        key1 = True
    else:
        print("Wrong.")
        key1 = False
    return key1

def puzzle2():
    print("PUZZLE 2")
    time.sleep(1.5)
    answer = int(input("How many times can you subtract the number 5 from 25?"))
    if answer == 1:
        print("Correct! Here is a key")
        key2 = True
    else:
        print("Wrong.")
        key2 = False
    return key2

def puzzle3():
    print("PUZZLE 3")
    time.sleep(1.5)
    answer = input("What has 6 faces and 21 eyes, but wears no makeup and can't see?")
    time.sleep(1.5)
    if answer.casefold() == "die" or answer == "a die" or answer == "a dice" or answer == "dice":
        print("Correct! Here is a key")
        key3 = True
    else:
        print("Worng")
        key3 = False
    return key3


def main():
    print("CHAPTER FOUR")
    time.sleep(1.5)
    print("Phew. You made it past that orc. It looks like you found the wizard's lair!")
    time.sleep(1.5)
    print("You see the door, but it looks like you need to solve some puzzles to open it up!")
    key1 = False
    key2 = False
    key3 = False
    while key1 == False:
        key1 = puzzle1()
    while key2 == False:
        key2 = puzzle2()
    while key3 == False:
        key3 = puzzle3()
    globalvariables.puzzle_success = True

#main(key1, key2, key3)

if __name__ == "__main__":
    main()


#print(puzzle1())
#print(puzzle2())
#print(puzzle3())