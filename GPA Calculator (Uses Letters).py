#### ---- SETUP ---- ####

letters = ["C", "D", "B", "C", "B", "C", "B", "A", "C", "B", "B", "A", "A", "A", "B", "A", "A"]
numbers = []
total = 0

#### ---- LOOP ---- ####

for letter in letters:
    if letter == "A":
        number = 4
    elif letter == "B":
        number = 3
    elif letter == "C":
        number = 2
    elif letter == "D":
        number = 1
    numbers.append(number)
    total += number

#### ---- OUTPUT ---- ####

print("Letter grades: " + str(letters))
print("Number grades: " + str(numbers))

average = total / len(numbers)
print("Your GPA is " + str(average))
