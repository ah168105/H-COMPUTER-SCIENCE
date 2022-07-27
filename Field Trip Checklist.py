#### ---- INPUT ---- ####

in_band = input("Are you in the band? (y/n): ")
in_choir = input("Are you in the choir? (y/n): ")
permission_slip = input("Do you have a signed permission slip? (y/n): ")
class_work = input("Are you caught up on class work? (y/n): ")
available = input("Are you available next Friday, on the day of the trip? (y/n) ")
print()

#### ---- VARIABLE SETUP ---- ####

can_go = True

#### ---- ATTENDING LOGIC ---- ####
if in_band == "y" or in_choir == "y" and permission_slip == "y" and class_work == "y" and available == "y":
    can_go = True
else:
    can_go = False

if can_go == True:
    print("You can go on the field trip!")
else:
    print("Sorry, you can't go on this field trip.  Maybe next time.")
