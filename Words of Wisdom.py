#### ---- SETUP ---- ####

## -- Starting phrases -- ##

import random
advice = ["A _1 saved is a _2 earned",
          "Never look a gift _2 in the _1",
          "All's fair in _1 and _2",
          "_2 makes the _1 grow fonder",
          "A _1 in the hand is worth two in the _2",
          "The _2 is mightier than the _1",
          "A _1 and his _2 are soon parted",
          "A _2 a day keeps the _1 away",
          "Don't put the _1 before the _2",
          "A rolling _2 gathers no _1",
          "A _1 in time saves _2",
          "_2 is in the _1 of the beholder",
          "Don't judge a _1 by its _2",
          "Don't put all your _2 in one _1",
          "The early _1 gets the _2",
          "Every _2 has a silver _1",
          "_1 favors the _2",
          "_2 is the best _1",
          "A _1 of a thousand miles begins with a single _2",
          "You can't make a _1 without breaking some _2",
          "A _2 is only as strong as its weakest _1",
          "_1 catches more flies than _2",
          "You can lead a _2 to _1, but you can't make it drink",
          "There is no _1 on the _2",
          "You can't pluck a _2 off a bald _1",
          "Live like a _1 in _2",
          "A _2 across the sea can be seen, a _1 on the eyelid can't",
          "Only a _1 tests the depth of a _2 with both feet",
          "Rain beats the _2's skin, but it does not wash out the _1",
          "Shared _1 is a double _1, shared _2 is half a _2",
          "Where _2 reigns, the _1 may be attained",
          "A _1 does not know the taste of _2",
          "The most beautiful _2 may contain a _1",
          "Evil enters like a _1 and spreads like a _2",
          "_2 is honorable and _1 is noble",
          "In a _1 battle, a _2 will get squashed",
          "Give a man a _2 and you feed him for a _1",
          "It takes a _1 to raise a _2",
          "A large _2 does not make a _1",
          "_1 in youth is like engraving in _2",
          "A _2 does not seek his _1; _1 seeks its _2",
          "Turn your _2 towards the sun and the _1 will fall behind you",
          "If you go to a _1's house, don't talk about _2",
          "With great _2 comes great _1"
         ]

## -- User input -- ##

print("2 Players should each think of a word without discussing them.")
input("Hit enter when you're ready to continue.")
player1_noun = input("Player 1, enter a singular noun: ")
player2_noun = input("Player 2, enter a singular noun: ")

## -- Blank replacement -- ##

chosen_advices = []

for i in range(6):
    random_advices = random.choice(advice)
    advice.remove(random_advices)
    random_advices = random_advices.replace("_1", player1_noun)
    random_advices = random_advices.replace("_2", player2_noun)
    chosen_advices.append(random_advices)


## -- Phrase tracking variables -- ##

num_votes = 0
advice1 = chosen_advices[0]
advice2 = chosen_advices[1]
chosen_advices.remove(advice1)
chosen_advices.remove(advice2)


#### ---- MAIN LOOP ---- ####
rounds = 1
for i in range(5):

    ## -- Phrase display -- ##advice
    print()
    print("ROUND " + str(rounds) + ":")
    print(advice1 + "    VS    " + advice2)
    print()
    print("Which was the better advice?")

    ## -- User vote -- ##

    choice = input("1 or 2: ")
    while choice != "1" and choice != "2":
        choice = input("Please choose 1 or 2: ")
    if choice == "2":
        advice1 = advice2
        num_votes = 1
    else:
        num_votes += 1
    if chosen_advices != []:
        advice2 = random.choice(chosen_advices)
        chosen_advices.remove(advice2)






#### ---- FINAL OUTPUT ---- ####

message = "The winning advice was ""\"" + advice1 + "\" which was voted for " + str(num_votes) + " times."
if num_votes >= 2:
    message = message.replace(".", "!")
    message = message.upper()
print()
print(message)
