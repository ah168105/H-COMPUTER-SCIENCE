#### ---- INPUT ---- ####

print("Welcome to our secure 2-step login process.")
print("After entering your password, you will be sent an authentication code to verify your identity")
print()
password = input("Please enter your password: ")
print("Sending authentication code to phone number associated with your account.")
auth_code = input("Please enter your unique authentication code: ")
print()

#### ---- LOGIN ATTEMPT ---- ####
if password == "code" and auth_code == "1234":
    print("You successfully logged in")
else:
    print("You have invalid credentials")
