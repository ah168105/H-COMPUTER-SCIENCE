#### ---- ALLOWANCE INPUT ---- ####
#wish i got allowance :(

allowance = int(input("How much allowance do you feel you earned this week? $"))
print()

#### ---- LIMIT ALLOWANCE ---- ####
if allowance > 30:
    allowance = 30
    print("Sorry that's too much! ")
if allowance < 5:
    allowance = 5
    print("That's way too little money! ")


#### ---- OUTPUT ---- ####

print("So, your allowance will be $" + str(allowance) + " this week.")
