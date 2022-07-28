#### ---- INPUT ---- ####

age = int(input("Enter your age:  "))
months_since_bday = int(input("How many months ago was your last birthday? "))

#### ---- CALCULATIONS ---- ####
age *= 12
age += months_since_bday


#### ---- OUTPUT ---- ####

print()
print("You are " + str(age) + " months old!")
