## -- Variables -- ##
lincoln = 0
kahlo = 0
lovelace = 0
howard = 0
## -- Instructions -- ##
print("Which famous historical figure are you? Answer the questions below to find out!")
input("Hit enter to begin.")
print("")
#### ---- QUESTIONS ---- ####

## -- Question 1 -- ##
print("I would rather...")
print(" a) Do something brand new")
print(" b) Improve something that already exists")
question_1 = input("Your answer: ")
## -- Scores 1 -- ##
if question_1 == "a":
    lovelace += 1
elif question_1 == "b":
    lincoln += 1
    kahlo += 1
else:
    print("That wasn't one of the available choices. Ignoring your answer.")
    howard += 1
## -- Question 2 -- ##
print("My idea of fun is...")
print(" a) Spending time with friends")
print(" b) Creating art")
print(" c) Learning something new")
question_2 = input("Your answer: ")
## -- Scores 2 -- ##
if question_2 == "a":
    lincoln += 1
elif question_2 == "b":
    kahlo += 1
elif question_2 == "c":
    lovelace += 1
else:
    print("That wasn't one of the available choices. Ignoring your answer.")
    howard += 1
## -- Question 3 -- ##
print("Of the following, my favorite class is:")
print(" a) English")
print(" b) Math")
print(" c) Art")
question_3 = input("Your answer: ")

## -- Scores 3 -- ##
if question_3 == "a":
    lincoln += 1
elif question_3 == "b":
    lovelace += 1
elif question_3 == "c":
    kahlo += 1
else:
    print("That wasn't one of the available choices. Ignoring your answer.")
    howard += 1
#### ---- FINAL SCORES ---- ####

## -- Label -- ##
print("-- YOUR HISTORICAL FIGURE --")
print("")

## -- All scores -- ##
print("Your final scores were as follows:")
print("Abraham Lincoln: " + str(lincoln))
print("Ada Lovelace: " + str(lovelace))
print("Frida Kahlo: " + str(kahlo))
print("")

## -- Joke win -- ##
if lincoln == 0:
    if lovelace == 0:
        if kahlo == 0:
            print("Alright wise guy, you're Moe Howard.")

## -- Majority win -- ##
if lincoln > lovelace > kahlo:
    print("You are Abraham Lincoln!")
elif lovelace > lincoln > kahlo:
    print("You are Ada Lovelace!")
elif kahlo > lincoln > lovelace:
    print("You are Frieda Kahlo!")
## -- No majority -- ##
if lincoln == 1:
    if lovelace == 1:
        if kahlo == 1:
            print("You didn't get a majority score on any one person; looks like you're a true individual!")
