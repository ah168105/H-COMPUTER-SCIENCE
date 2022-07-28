# Print the first part of the joke
print("Knock knock")

# Get the user's first response
first = input()

# If the first response is correct, continue the joke
if first == "Who's there?" or  first == "Who's there" or first == "who's there" or first == "who's there":
    print("Lettuce")

    # Get the user's second response
    second = input()

    # If the second response is correct, finish the joke
    if second == "Lettuce who?" or second == "Lettuce who" or second == "lettuce who?" or second == "lettuce who":
        print("Lettuce in, it's cold out here!")

    # Otherwise, tell the user to ask lettuce who?
    else:
        print("You need to ask: Lettuce who?")

# Otherwise, tell the user to ask who's there?
else:
    print("You need to ask: Who's there?")
