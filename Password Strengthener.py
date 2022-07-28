#### ---- SETUP ---- ####

import random

alpha = False
digit = False

alpha_additions = ["platypus", "pineapple", "yrt", "qwx", "aquarium", "jkz", "pfv", "guitar", "ytc"]

user_password = input("Enter a password to get a more secure version of it: ")
while user_password == "":
    user_password = input("Please enter a password: ")
print()

#### ---- PASSWORD STRENGTHENING ---- ####

for strength in user_password:
    if strength.isalpha():
        alpha = True
    if strength.isdigit():
        digit = True

if "password" in user_password:
    print ("password")
    user_password.split()
    new = user_password.replace("password", random.choice(alpha_additions))
    
elif alpha and digit:
    new_password = user_password
elif alpha:
    new_password = (user_password) + str(random.randint(100,999))
elif digit:
    new_password =  random.choice(alpha_additions) + user_password                                     
else:
    new_password = random.choice(alpha_additions) + str(random.randint(100,999))    

#### ---- OUTPUT ---- ####

print("Your secure password is " + new_password)
