#### ---- SETUP ---- ####

## -- Question lists -- ##

instruments = ["piano", "sitar (at minimum)", "guqin", "marimba (4.3 octave)", "808 drum machine"]
instrument_parts = ["keys", "strings", "strings", "bars", "keys"]

## -- Answer and guess lists -- ##

answers = [88, 18, 7, 50, 16]
guesses = []

#### ---- GUESSING ---- ####

## -- Intro -- ##

print("**Super Difficult Music Quiz**")
print()

## -- Guessing loop -- ##

for i in range(len(answers)):
    guess = input("How many " + instrument_parts[i] + " does a " + instruments[i] + " have? ")
    guesses.append(int(guess))

## -- Response -- ##
if guesses == answers:
    print("Amazing! You got them all!")
else:
    print("You got at least one answer wrong.Try again!")

