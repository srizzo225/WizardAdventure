WIZARD ADVENTURE README FILE

*WHERE IS THE CODE HOSTED?*
The code is hosted on GitHub: https://github.com/srizzo225/WizardAdventure

*EXTERNAL SERVICES*
None, the game is self-contained.

*LANGUAGES & TECHNOLOGIES*
Wizard Adventure is written in Python 3.

*SYSTEM REQUIREMENTS & SUPPORTED APPLICATIONS*
The only system requirement is that you have an application that can run Python 3 or greater. 

*CODING/NAMING CONVENTIONS*
I mostly use all lowercase and underscores for variables (ex- shop, wizard_success). 
I try to keep variable names and files as descriptive as possible (ex- playerHP- the HP of the player, 
key1- the first key needed for a door, or ch03orc.py, the 3rd chapter in the game and has the orc battle)

*HOW TO RUN/BUILD/DEPLOY THE PROGRAM (AKA START THE GAME!)*
Simply download all the files from the repository into one folder. Open maingame.py to begin playing.
While you will not be opening the other files, it important to download them all and store them in one folder together 
so that the main program will be able to access them.

*OVERVIEW OF THE ARCHITECTURE*
The game runs entirely from the maingame.py file. 
Each chapter of the game is a seperate file and imported into the main file as a module.
Global variables are used to move the player from chapter to chapter.
Global variables are stored in the globalvariables.py file.
Each chapter has a task that needs to be completed to move on.
Once the task in completed, the chapter sets the global variable for that chapter to True, 
then once the main game sees that varible is set to true, it allows you to move on to the next chapter.
If the player fails chapter 3 or 5, they will be sent back to the beginning of the game (these are battles, if you lose the battle the player "dies").
For chapters 1, 2, and 4 the player will just get stuck if they fail. The chapters involve finding something, 
so if you don't find the "thing" (way out of the maze in chapter 2 or keys in chapter 4) you can't move on.
