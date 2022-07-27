#### ---- SET UP ---- ####

print("An anagram of a word or sentence uses all the same letters, but in a different order. (Spaces are ignored.)")
print("Make up a secret identity by creating an anagram of your name. (Use lower-case letters only.)")
print()

name = input("Enter your name in lower-case letters: ")
secret = input("Enter your anagrammed secret identity in lower-case letters: ")

#### ---- ANAGRAM CHECK ---- ####

all_letters = name + secret

anagram = True

for letter in all_letters:
    if letter == " ":
        continue

    elif name.count(letter) != secret.count(letter):
        anagram = False


#### ---- RESULTS ---- ####

print()
if anagram:
    print("Yes! It turns out " + secret + " is a valid anagram of " + name)
else:
    print("That won't work, since " + secret + " is not a valid anagram of " + name)
