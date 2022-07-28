#### ---- SETUP ---- ####

## -- Library -- ##

import random

## -- User input -- ##
print("I'm thinking of a random number.")
guess = input("Guess whether it's even or odd! ")
answer = "I don't know"
number = 0

#### ---- NUMBER CHOICE ---- ####
number = random.randint(1,10)
if number % 2 == 0:
     answer = "even"
else:
     answer = "odd"   


#### ---- OUTPUT ---- ####

if answer == guess:
    print("You guessed right!")
else:
    print("No, that wasn't it. Sorry.")
print("The number was " + str(number))
