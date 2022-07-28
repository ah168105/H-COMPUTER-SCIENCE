#### ---- SETUP ---- ####

print("Welcome to the App Store!")
print()
purchase_history = [5, 0.5, 2, 2, 1, 0.5, 1.5, 2, 1, 3, 1.5]
total = 0
largest = 0

#### ---- OUTPUT ---- ####

## -- Loop -- ##
for purchase in purchase_history:
    total += purchase
    if purchase > largest:
        largest = purchase





print("You have spent a total of $" + str(total))
print("The most expensive app you purchased cost $" + str(largest))
