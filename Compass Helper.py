#### ---- INPUT ---- ####
rising = input("Is the sun a) rising or b) setting? Enter a or b: ")
direction = input("Is the sun to your a) left or b) right? Enter a or b: ")


#### ---- RESPONSE ---- ####
if rising == "a":
    if direction == "a":
        print("The sun is facing the South.")
    else:
        print("The sun is facing the North.")
else:
    if rising == "b":
        if direction == "a":
            print("You are facing North.")
    else:
            print("You are facing South.")
