#### ---- SETUP ---- ####

donations = [50, 23, 10, 15, 10, 100, 15, 50, 20, 1200, 20, 16, 12, 10, 10, 200, 25, 25, 50, 25, 10, 5, 15, 20, 15]
total = 0
largest = 0

#### ---- LOOP ---- ####
for amount in donations:
    total += amount
    if amount > largest:
        largest = amount

average = total / len(donations)

#### ---- OUTPUT ---- ####
print("The total amount donated was: $" + str(total))
print("The largest single donation was: $" + str(largest))
print("The average donation was: $" + str(average))
