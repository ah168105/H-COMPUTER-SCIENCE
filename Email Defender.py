#### ---- SETUP ---- ####

print("Reduce spam by making your email address harder for computers to read")
email = input("Enter your email: ")
secure_email = ""

#### ---- SECURE EMAIL ---- ####

for character in email:
    if character == "@":
        secure_email += " <at> "
    elif character == ".":
        secure_email += " <dot> "
    else:
        secure_email += character
        
#### ---- OUTPUT ---- ####

print("Your secured email is: " + secure_email)
