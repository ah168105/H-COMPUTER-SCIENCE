#### ---- SETUP ---- ####

import random
number = input("Enter a decimal number in the U.S. format, with commas and a period: ")

#### ---- SYMBOL SWAP ---- ####
number = number.replace(",", "@")
number = number.replace(".", ",")
number = number.replace("@", ".")

#### ---- OUTPUT ---- ####

country = random.choice(["Argentina", "Brazil", "France", "Germany", "Indonesia", "Mozambique", "Russia", "South Africa", "Sweden", "Vietnam"])
print("In " + country + ", that number would be written: " + number)
