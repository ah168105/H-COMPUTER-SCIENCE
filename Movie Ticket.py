import random

# Get the user's movie choice
print("Which movie would you like to see? All movies are $10.")
print("1: The Friendly Bear - Rated G")
print("2: World of Monkeys - Rated PG")
print("3: Things Blowing Up - Rated R")
movie = int(input("Enter the movie number: "))
print()

# Ask the user for their age and available money
age = int(input("How old are you? "))
money = float(input("How much money do you have on you? Enter just the number with no dollar sign: "))
print()

# Determine how many tickets are available
tickets = random.randint(0,10)
print("There are " + str(tickets) + " tickets available for that movie.")
print()

# Create boolean variables to reduce compound expression
can_afford = money >= 10
available = tickets > 0
old_enough = age >= 17 and (age >= 17 or movie != 3)

# Determine if the user can buy a ticket
if can_afford and available and old_enough:
    print("Here's your ticket!")
else:
    print("Sorry, you can't see this movie now.")
