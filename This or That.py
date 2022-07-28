#### ---- USER INPUT ---- ####

print("Icebreakers are a great way to get to know people")
print("Please answer the following 'this-or-that' questions:")
print()

## -- Dessert -- ##

dessert = input("Which do you prefer, cake or pie? ")

## -- Dessert validation -- ##
while dessert != "cake" and dessert != "pie":
    dessert = input("Please enter a valid option")

## -- Writing -- ##

writing = input("Which do you prefer, pens or pencils? ")

## -- Writing validation -- ##
while writing != "pens" and writing != "pencils":
    writing = input("Please enter a valid option")

## -- Drink -- ##

drink = input("Which do you prefer, tea or coffee? ")

## -- Drink Validation -- ##
while drink != "tea" and "coffee":
    drink = input("Please enter a valid option")

#### ---- RESULTS ---- ####

print()
print("Here is what you chose: ")
print("Between cake and pie you chose: " + dessert)
print("Between pens and pencils you chose: " + writing)
print("Between tea and coffee you chose: " + drink)
