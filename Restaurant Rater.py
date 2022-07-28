#### ---- USER INPUT ---- ####

## -- Restaraunt -- ##

print("RESTAURANT RATER")
name = input("What restaurant did you visit? ")

## -- Food rating -- ##
food = float(input("How would you rate the food, from 1-10? "))

## -- Food validation -- ##
while food > 10:
    food = float(input("Please enter a number between 1-10."))


## -- Service rating -- ##
service = float(input("How would you rate the service, from 1-10? "))

## -- Service validation -- ##
while service > 10:
    service = float(input("Please enter a number between 1-10."))



#### ---- RESULTS ---- ####

print()
average = (food + service) / 2
print("You have given " + name + " an overall score of " + str(average) + ".")
print("Now the whole world will know the truth.")
print("Thanks for using Restaurant Rater!")
