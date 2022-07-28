#### ---- INTRO ---- ####

print("Welcome to Sushi-Go-Round!")
print("All types of sushi are on colored plates that go around a conveyor belt throughout the restaurant.")
print("You will be charged for whatever plates you grab based on the color.")
print("Prices are:")
print("    $2 for a yellow plate")
print("    $3 for a green plate")
print("    $5 for a red plate")
print("    $8 for a blue plate")
print()

#### ---- NUMBER OF PLATES ---- ####

yellow = 0
green = 0
red = 0
blue = 0

#### ---- SELECT SUSHI ---- ####

california = input("A classic California roll passed by on a red plate. Do you want it (y/n)? ")
edamame = input("A healthy bowl of edamame passed by on a yellow plate. Do you want it (y/n)? ")
vegetable = input("A refreshing vegetable roll passed by on a green plate. Do you want it (y/n)? ")
otoro = input("A delectable otoro tuna sashimi passed by on a blue plate. Do you want it (y/n)? ")
salmon = input("A spicy salmon handroll passed by on a red plate. Do you want it (y/n)? ")

if california == "y":
    red += 1
if edamame == "y":
    yellow += 1
if vegetable == "y":
    green += 1
if otoro == "y":
    blue += 1
if salmon == "y":
    red += 1

#### ---- CALCULATE TOTAL ---- ####

subtotal = (yellow * 2) + (green * 3) + (red * 5) + (blue * 8)
total = subtotal * 1.10

#### ---- OUTPUT ---- ####

print()
print("Thank you for dining at Sushi-Go-Round! Your total bill is: $" + str(total))
