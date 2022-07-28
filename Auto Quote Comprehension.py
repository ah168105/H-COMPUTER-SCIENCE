#### ---- INPUT ---- ####

age = int(input("How old are you in years? "))
auto_type = input("What kind of vehicle do you have (sedan, coupe, sports, van, truck, motorcycle)? ")
auto_age = int(input("How old is the vehicle in years? "))
location = input("What kind of neighborhood do you live in (urban, suburban, rural)? ")

quote = 0

#### ---- CALCULATIONS ---- ####

# Age
if age < 18:
    quote += 50
elif age < 21:
    quote += 40
else:
    quote += 25

# Vechicle Type
if auto_type == "sedan":
    quote += 30
elif auto_type == "coupe":
    quote += 40
elif auto_type == "sports":
    quote += 60
elif auto_type == "van":
    quote += 25
elif auto_type == "truck":
    quote += 35
elif auto_type == "motorcycle":
    quote += 60

# Vehicle Age
if auto_age < 5:
    quote += 20
elif auto_age < 10:
    quote += 10
else:
    quote += 5

# Location
if location == "urban":
    quote += 20
elif location == "suburban":
    quote += 15
elif location == "rural":
    quote += 10

#### ---- OUTPUT ---- ####

print("The estimated monthly cost of auto insurance is: $" + str(quote))
