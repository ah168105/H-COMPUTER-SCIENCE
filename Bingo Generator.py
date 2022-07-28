#### ---- SETUP ---- ####

import random

number = random.randint(1,75)

#### ---- OUTPUT ---- ####

print("The next number is...")

if number <= 15:
    print("B " + str(number))
elif number <= 30:
    print("I " + str(number))
elif number <= 45:
    print("N " + str(number))
elif number <= 60:
    print("G " + str(number))
else:
    print("O " + str(number))
