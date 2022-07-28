#### ---- SETUP ---- ####

player_ages = [32, 25, 29, 35, 32, 28, 27, 26, 22, 25, 23, 28, 28, 25, 29, 20, 21, 31, 32, 31, 27, 25, 20]

#### ---- OUTPUT ---- ####

## -- Loop -- ##
total_years = 0

for age in player_ages:
    total_years += age

## -- Average -- ##

total_players = len(player_ages)
average_age = total_years / total_players

print("The average age of players on the 2020 US Women's Soccer Team is "
      + str(average_age) + " years.")
