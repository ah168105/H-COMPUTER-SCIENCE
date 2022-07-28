#### ---- SETUP ---- ####

## -- Variables -- ##

pattern1 = "-----------------"
pattern2 = "ooooooooooooooooo"
pattern3 = "xxxxxxxxxxxxxxxxx"
lines = 1

## -- Introduction -- ##

print("My beautiful rug design: ")
print()

#### ---- DRAW RUG ---- ####
while lines <= 14:
    if lines == 1 or lines == 14:
        print(pattern3)
    elif lines % 5 == 0:
        print(pattern1)
    else:
        print(pattern2)
    lines += 1
