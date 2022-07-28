# Print instructions
print("In this game, take turns deciding what the next number should be. You can increment the current number by 1, 2 or 3.")
print("If you're the first player to enter a number over 20, you lose!")
print()

# Ask how many players there are
num_players = int(input("How many players are there" ))

# Start the game at 0 with Player 1 going first
number = 0
current_player = 1

# Initialize a boolean variable to control the game loop
playing = True

# Take turns until someone loses
while playing:

    # Get the next number from the current player
    print()
    print("The number is currently " + str(number))
    new_number = int(input("Player " + str(current_player) + ", enter the next number: "))

    # Force correct input for the next number
    while new_number <= number or new_number > number + 3:
        new_number = int(input("Your options are " + str(number + 1) + ", " + str(number + 2) + " or " + str(number + 3)+ ": "))

    # Once the next number is valid, it becomes the new number
    number = new_number

    # If the new number is greater than 20, the current player loses
    if number > 20:
        print("Player " + str(current_player) + ", you lose!")
        playing = False

    # Move to the next player's turn
    current_player = current_player % num_players + 1
