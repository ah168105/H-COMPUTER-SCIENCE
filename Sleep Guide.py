#### ---- INTRO ---- ####

print("According to the National Sleep Foundation, there is a suggested number of hours of sleep you should get based on your age.")
print("See if you are getting more or less sleep than what is suggested for your age!")
print()

#### ---- SLEEP INFO ---- ####

age = int(input("How old are you? "))
hours = float(input("How many hours of sleep do you get on average? "))

#### ---- SLEEP RESULTS---- ####

if age < 2:
    if hours < 11:
        print("For a toddler, that is not enough sleep. It is suggested to get 11-14 hours of sleep.")
    elif 11 <= hours < 14:
        print("For a toddler, that is just the right amount of sleep.")
    else:
        print("For a toddler, that is more than enough sleep.")
if 2 <= age < 13:
    if hours < 9:
        print("For a school age child, that is not enough sleep. It is suggested to get 9-11 hours of sleep.")
    elif 9 <= hours < 11:
        print("For a school age child, that is just the right amount of sleep.")
    else:
        print("For a school age child, that is more than enough sleep.")
if 13 <= age < 17:
    if hours < 8:
        print("For a teenager, that is not enough sleep. It is suggested to get 8-10 hours of sleep.")
    elif 8 <= hours < 10:
        print("For a teenager, that is just the right amount of sleep.")
    else:
        print("For a teenager, that is more than enough sleep.")
else:
    if hours < 7:
        print("For an adult, that is not enough sleep. It is suggested to get 7-9 hours of sleep.")
    elif 7 <= hours < 9:
        print("For an adult, that is just the right amount of sleep.")
    else:
        print("For an adult, that is more than enough sleep.")

