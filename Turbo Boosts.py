#### ---- SETUP ---- ####

## -- Turbo variable -- ##
turbo = 3

## -- Introduction -- ##
print("Starting the race with " + str(turbo) + " turbo-boosts.")
print()


#### ---- BOOST CONDITIONS ---- ####

## -- Found boost -- ##
found_boost = input("Did player find a turbo-boost? y/n ")

if found_boost == "y":
    turbo += 1

    
print("Turbo Boosts Available: " + str(turbo))
print()

## -- Purchase boost package -- ##
boost_package = input("Did player purchase a 5-turbo-boost package? y/n ")

if boost_package == "y":
    turbo += 5


print("Turbo Boosts Available: " + str(turbo))
print()

## -- Single boost -- ##
single_boost = input("Did player use a turbo-boost? y/n ")

if single_boost == "y":
    turbo -= 1



print("Turbo Boosts Available: " + str(turbo))
print()

## -- Double boost -- ##
double_boost = input("Did player use a double turbo-boost? y/n ")

if double_boost == "y":
    turbo -= 2

print("Turbo Boosts Available: " + str(turbo))
print()
