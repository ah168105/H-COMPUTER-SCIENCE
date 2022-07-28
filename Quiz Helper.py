#### ---- INPUT ---- ####
answer = input("QUIZ QUESTION: What is the longest bone in the human body? ")


#### ---- RESPONSE ---- ####

## -- Correct response -- ##
if answer == "femur":
    print("That's correct!")

## -- Incorrect response -- ##
else:
    print("That's not it.")
    print("Hint: The bone is in the leg.")
    answer = input("Guess again: ")

    ## -- Second guess response -- ##
    if answer == "femur":
        print("That's correct!")
    else:
        print("Sorry. The answer was femur")
