#### ---- VARIABLE SETUP ---- ####

## -- Initial health value -- ##

health = 100

## -- First-aid kit value -- ##

first_aid = 20

#### ---- GAME PLAY ---- ####

print("Level starting with Willa at " + str(health) + " health points.")
print()

## -- Enemy damage -- ##

print("Willa is hit by an enemy. How many health points did Willa lose?")
enemy_damage = int(input("Enter integer between 5 and 50: "))
if enemy_damage > 50:
    enemy_damage = 50
if enemy_damage < 5:
    enemy_damage = 5
health -= enemy_damage

print()
print("Willa now has " + str(health) + " health points.")
print()

## -- First-aid kit (+20 points) -- ##

print("Willa picks up the first-aid kit!")

health += first_aid
if health > 100:
    health = 100

print()
print("Willa now has " + str(health) + " health points.")
