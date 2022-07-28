## -- Library -- ##

import random

## -- List -- ##

words = ["flood", "record", "sparks", "contain", "haircut", "busy", "spiders", "coding", "tasteful", "dreamy", "agree", "meddle", "harsh", "impolite", "chess", "grumpy", "wonder", "respect", "honorable", "camera", "friend", "skates", "tooth", "dancer", "whistle", "bump", "yellow", "elastic", "direction", "queen", "rhythm", "pink", "charge", "house", "produce", "hungry", "spotted", "previous", "physical", "typical", "beef", "travel", "rocky", "teacher", "wobble", "jumpy", "history", "night", "airport", "proud"]

#### ---- JUMBLE ---- ####

## -- Word choice -- ##

word = random.choice(words)

## -- Word jumble -- ##

letters = list(word)
random.shuffle(letters)
word_jumbled = "".join(letters)

#### ---- GUESS ---- ####

## -- Input -- ##

print("Unscramble this word: " + word_jumbled)
guess = input("Your guess: ")

## -- Comparison -- ##
if guess == word:
    print("You got it!")
else:
    print("Sorry, the correct answer was \"" + word + "\".")
