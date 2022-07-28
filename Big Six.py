import random

print("You have 6 chances to roll a 6")
print()

turns = 1

while turns <= 6:
    dice_roll = random.randint(1, 6)
    turns += 1

    if dice_roll == 6:
        print("Congrats! You got a 6!")
        break
    
    if dice_roll >= 4:
        print("You were so close with a " + str(dice_roll))
        continue

    print("You only rolled a " + str(dice_roll))

else:
    print("Sadly, you didn't roll a 6 in 6 turns")
