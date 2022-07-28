#### ---- INPUT ---- ####

bottles = int(input("How many bottles of pop do you want to start with? "))

#### ---- SONG LOOP ---- ####

while bottles:
    print()
    print(str(bottles) + " bottles of pop on the wall! " + str(bottles) + " bottles of pop!")
    bottles -= 1
    print("Take one down, pass it around, " + str(bottles) + " bottles of pop on the wall!")
    input("(Hit enter to continue)")

print()
print("The end!")
