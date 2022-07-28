#### ---- SETUP ---- ####

import random

print("Welcome to Animal Soccer!")
print("This year's teams are as follows:")
print()

animal_options = ["cat", "dog", "horse", "guinea pig", "turkey", "ferret", "ostrich", "opossum", "goat"]

team1 = []
team2 = []

#### ---- TEAM CREATION ---- ####

for i in range(7):
    animal1 = random.choice(animal_options)
    animal2 = random.choice(animal_options)

    team1.append(animal1)
    team2.append(animal2)

team1.sort()
team2.sort()

#### ---- OUTPUT ---- ####

print("TEAM 1:")
for animal in team1:
    print(animal)

print()
print("~~~~~~ VS ~~~~~~")
print()

print("TEAM 2:")
for animal in team2:
    print(animal)

print()
winner = input("Who do you think will win? (1 or 2): ")
print("I agree, I think Team " + winner + " is a strong looking team!")
