#### ---- SETUP ---- ####

## -- Library -- ##

import random

## -- Game setup -- ##

print("Welcome to the Treasure Hunt game show! You have three chances to collect prizes from 10 boxes.")
print("Be careful, one of them is a trap that will take all your prizes!")
trap = random.randint(1, 10)

## -- Boolean variable -- ##
picked_trap = False


#### ---- GAME LOOP ---- ####

## -- Loop variables -- ##

chances = 3
while chances > 0:

    ## -- User input -- ##
    
    guess = int(input("Which box would you like to open? Choose a number between 1 and 10: "))

    ## -- Check if still safe -- ##
    if guess == trap:

        ## -- Update boolean variable -- ##
        picked_trap = True
    else:
        picked_trap = False

    ## -- Update loop variable -- ##
    chances -= 1

#### ---- OUTPUT ---- ####

## -- Print a message to the user -- ##
if picked_trap:
    print("Oh no! You picked the trap in box " + str(trap) + "!")
else:
    print("Congratulations! You've collected 3 treasures and avoided the trap in box " + str(trap))
