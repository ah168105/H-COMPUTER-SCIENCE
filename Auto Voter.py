#### ---- SETUP ---- ####

## -- Library -- ##
import random

## -- Lists -- ##
options = ["Coke", "pancakes", "Latin", "books", "blue", "squirrels", "iPhone", "vanilla", "Batman"] 
voters = ["Abdul", "Amira", "Casey", "Elmer", "Howard", "Maya", "Owen", "Tanisha"]

## -- Variables -- ##
option1_index = random.randint(0, len(options) -1)
option2_index = random.randint(0, len(options) -1)

option1 = options[option1_index]
option2 = options[option2_index]

option1_votes = 0
option2_votes = 0

vote = random.randint(1,2)
#### ---- INPUT ---- ####

## -- User vote -- ##
for option in options:
    input("Do you prefer " + option1 + " or " + option2 + "?")

## -- Vote tally -- ##
while  vote != option1 or vote != option2:
        input("Do you prefer " + option1 + " or " + option2 + "?")
if user == option1:
    votes1 += 1
else:
    votes2 += 1
#### ---- OUTPUT ---- ####

## -- Voter loop -- ##
for voter in voters:
    vote = random.randint(1,2)
    if vote == 1:
        option1_votes += 1
        vote = option1
    else:
        option2_votes += 1
        vote = option2
## -- Results -- ##
print()

print("Final votes are in!")
print(str(votes1) + " for " + option1)
print(str(votes2) + " for " + option2)

if votes1 > votes2:
    print(option1 + " Wins!")
else:
    print(option2 + " Wins!")
