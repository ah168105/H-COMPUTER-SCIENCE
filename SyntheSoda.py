#### ---- SETUP ---- ####

## -- Menu -- ##
print("Your available soda syrups are:")
print(" cola")
print(" cherry")
print(" lemon-lime")
print(" orange")
print(" rootbeer")
print(" none")
print("")

## -- Variables -- ##
cola = False
cherry = False
lemon_lime = False
orange = False
rootbeer = False
none = False

## -- User selections -- ##
first_flavor = input("Enter your first flavor choice: ")
second_flavor = input("Enter your second flavor choice: ")

#### ---- RECORD FLAVORS ---- ####

## -- Flavors for either input -- ##
if first_flavor == "cola" or second_flavor == "cola":
    cola = True
if first_flavor == "cherry" and second_flavor == "cherry":
    cherry = True
if first_flavor == "lemon-lime" and second_flavor == "lemon-lime":
    lemon_lime = True
if first_flavor == "orange" and second_flavor == "orange":
    orange = True
if first_flavor == "rootbeer" and second_flavor == "rootbeer":
    rootbeer = True
if first_flavor == "none" and second_flavor == "none":
    none = True
if cola or cherry or lemon_lime or orange or rootbeer:
    syrup = True
    
## -- Single syrup - none and anything else -- ##
if syrup and none:
    print("You have made a normal soda. A little plain, but nothing wrong with that.")

#### ---- FLAVOR OUTPUTS ---- ####
elif cola and cola:
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("You must really like cola? Enjoy!")
    
elif cherry and cherry:
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("You must really like cherry? Enjoy!")
    
elif lemon_lime and lemon_lime:
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("You must really like lemon-lime? Enjoy!")
    
elif orange and orange:
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("You must really like orange? Enjoy!")
    
elif rootbeer and rootbeer:
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("You must really like rootbeer? Enjoy!")
    
elif (cherry and cola) or (cola and cherry):
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("This Cherry Cola is mysterious and complex. An instant classic!")
    
elif (cherry and lemon_lime) or (lemon_lime and cherry) or (cherry and orange) or (orange and cherry):
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("Cherry Citrus: a fruity mixture with surprising depths.")
    
elif (cherry and rootbeer) or (rootbeer or cherry):
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("Cherry Rootbeer! Avant-garde! A new twist on a comforting classic!")
else:
    print("Let's try the drink you designed...")
    print("Hmmm...")
    print("This combination was a bold choice, but hopefully you will still like it.")
