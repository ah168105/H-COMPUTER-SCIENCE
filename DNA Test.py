#### ---- SETUP ---- ####

## -- Library -- ##
import random


## -- Variables -- ##

all_continents = ["North America", "South America", "Asia", "Africa", "Europe", "Oceania"]
places = []
percentages = []
percent_remaining = 100
## -- Introduction -- ##

print("Congratulations, we have processed your DNA test sample.")
input("Press enter to see estimated results of your ancestry.")

#### ---- DNA CREATION ---- ####

while percent_remaining >= 5:

    ## -- Continent selection -- ##
    
    continent = random.choice(all_continents)
    places.append(continent) 
    all_continents.remove(continent)
    ## -- Percentage selection -- ##

    percent = random.randint(5, percent_remaining)
    percentages.append(percent)
    percent_remaining -= percent
    ## -- No continents left -- ##
    
    if all_continents == []:
        break

## -- Other ancenstry -- ##

if percent_remaining > 0:
    places.append("Other")
    percentages.append(percent_remaining)
#### ---- DNA ANALYSIS ---- ####

## -- Sorting -- ##

sorted_places = []
sorted_values = []

while places != []:
    highest_value = max(percentages)
    highest_index = percentages.index(highest_value)
    highest_place = places[highest_index]

    sorted_places.append(highest_place)
    sorted_values.append(highest_value)
    percentages.remove(highest_value)
    places.remove(highest_place)

## -- Max values -- ##

max_value = sorted_values[0]
max_place = sorted_places[0]

## -- Output -- ##

print()
print("Our report shows that your ancestry comes primarily from " + max_place + " with " + str(max_value) + "%")
print("The full list of estimated ancestry is as follows: ")
for i in range(len(sorted_places)):
    print("   " + str(sorted_values[i]) + "% " + sorted_places[i])
