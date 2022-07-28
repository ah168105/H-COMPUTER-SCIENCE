#### ---- SETUP ---- ####

## -- Cost variable -- ##

cost = 0

## -- Introduction -- ##

print("Welcome to the SmartShop app. Scan your groceries to automatically calculate your total cost.")
print()

#### ---- PURCHASE CONDITIONS ---- ####

## -- Cereal -- ##

cereal = input("Are you purchasing Cap'n Charms for $5? Enter y or n: ")
if cereal == "y":
    cost += 5
if cereal == "n":
    cost == cost


print()
print("Current total: $" + str(cost))

## -- Greens -- ##

greens = input("Are you purchasing fresh greens for $4? Enter y or n: ")
if greens == "y":
    cost += 5
if greens == "n":
    cost == cost

print()
print("Current total: $" + str(cost))

## -- Chicken -- ##

chicken = input("Are you purchasing chicken for $12? Enter y or n: ")
if chicken == "y":
    cost += 12
if chicken == "n":
    cost == cost

print()
print("Total for groceries: $" + str(cost))
