#### ---- INPUT ---- ####

number = int(input("Enter an integer to see its powers: "))
amount = int(input("How many powers of " + str(number) + " do you want to see? "))

#### ---- OUTPUT ---- ####
for i in range(amount):
    result = str(number ** i)
    print(str(i) + ": " + result)
