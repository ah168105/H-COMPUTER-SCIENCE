#### ---- SETUP ---- ####

import random
adjective = "nice"

#### ---- RANDOM CHOICE ---- ####
word = random.randint(1,4)
if word == 1:
    adjective = "fantastic"
if word == 2:
    adjective = "beautiful"
if word == 3:
    adjective = "marvelous"
if word == 4:
    adjective = "fun"
#### ---- OUTPUT ---- ####

print("Have a " + adjective + " day!")
