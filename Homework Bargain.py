# Tell the user what the deal is
print("You can watch up to 30 minutes of television if you do at least 60 minutes of homework.")

# Ask the user how many minutes of homework they will do
homework = int(input("How many minutes of homework will you do? "))
if homework < 60:
    homework = 60


# Ask the user how many minutes of television they want to watch
television = int(input("How many minutes of television do you want to watch? "))
if television > 30:
    television = 30


# Tell the user what they've agreed to
print("Once you do " + str(homework) + " minutes of homework, you can watch " + str(television) + " minutes of television.")
