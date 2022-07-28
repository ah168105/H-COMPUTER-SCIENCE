#### ---- POPULATION ESTIMATION ---- ####

## -- How many people are on Earth -- ##
seats_required = 7000000000
print ("There are about " + str(seats_required) + " people in the world.")

## -- How many babies are on Earth -- ##
babies_in_the_world = 200000000
print("There are about " + str(babies_in_the_world) + " babies that will sit on their parents' laps.")
seats_required -= babies_in_the_world
print("So only " + str(seats_required) + " people need their own seats.")
print()

#### ---- SPACE CALCULATION ---- ####

## -- How big is each seat? -- ##
seat_width = 2
seat_length = 3
square_feet_per_seat = seat_width * seat_length
print("Each person needs about " + str(square_feet_per_seat) + " square feet to sit.")  

## -- How big does the stadium need to be? -- ##
square_feet_required = seats_required * square_feet_per_seat
print("The stadium would need to cover " + str(square_feet_required) + " square feet, ")

## -- Converting from square feet to square miles -- ##
square_feet_per_square_mile = 5280 * 5280
square_miles_required = square_feet_required / square_feet_per_square_mile
print("which is " + str(square_miles_required) + " square miles.")
print()

#### ---- UNDERSTANDING THE NUMBER ---- ####

## -- Divide space amongst decks -- ##
decks = 3
square_miles_required /= decks
print("With three decks, the stadium would only need to cover " + str(square_miles_required) + " square miles, ")

## -- How many New York Cities? -- ##
new_york_city = 302.6
ratio = square_miles_required / new_york_city
print("which is about " + str(ratio) + " New York Cities.") 
