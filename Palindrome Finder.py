#### ---- INPUT ---- ####

phrase = input("Enter a phrase (lowercase with no punctuation): ")

#### ---- SPACE REMOVAL ---- ####

while " " in phrase:
    index = phrase.index(" ")
    phrase = phrase[:index] + phrase[index + 1:]

#### ---- PALINDROME CHECK ---- ####

phrase_flipped = phrase[::-1]
if phrase == phrase_flipped:
    print("The phrase is a palindrome!")
else:
    print("The phrase is not a palindrome.")
