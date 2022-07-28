# Give the starting temperature
temp = 70
print("It is currently " + str(temp) + " degrees in the house.")

# Ask if Dad is home
dad = input("Dad likes the house warm. Is Dad home? Enter y or n: ")
if dad == "y":
 temp += 5
    

# Ask if Mom is home
mom = input("Mom likes the house cool. Is Mom home? Enter y or n: ")
if mom == "y":
    temp -= 5    

# Ask for the user's preference
user = input("Do you like the house warm or cool? Enter warm or cool: ")
if user == "warm":
    temp += 3
if user == "cool":
    temp -= 3

# Give the final temperature
print("Setting the house temperature to " + str(temp) + " degrees.")
