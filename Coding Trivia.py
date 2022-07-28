# Print instructions
print("For each statement, enter either 'true' or 'false'.")
print()

## -- First question -- ##
first = input("The computer chips in phones today are more than 1,000 times faster than the computer on the Space Shuttle that first took men to the moon: ")
while first != "true" and first != "false":
    first = input("Please enter true or false")


    
print("That's true! Your phone also has more than ten million times more storage space as the Apollo 11 Space Shuttle.")
print()

## -- Second question -- ##
second = input("On average, people spend almost four times as much on video games as on movies every year: ")
while second != "true" and second != "false":
    second = input("Please enter true or false")



    
print("That's also true! In 2019, the film industry made $42 billion, while the video game industry took in $152 billion.")
print()

## -- Third question -- ##
third = input("The first computer virus was created in 1996: ")
while third != "true" and third != "false":
    third = input("Please enter true or false")

    
print("False! The first virus was written in 1971 and ws called Creeper.")
print()

## -- Score the user -- ##
score = 0
if first == "true":
    score += 1
if second == "true":
    score += 1
if third == "false":
    score += 1
print("You got " + str(score) + " out of 3 questions correct.
