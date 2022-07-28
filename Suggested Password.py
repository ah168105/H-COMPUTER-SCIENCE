#### ---- SETUP ---- ####

import random
parts = ["El3ph@ant", "K!tch3n", "J34lou$", "R@nd0m", "T@ct!cs", "C0mput3r$", "L!z4rd", "C*rr3ct", "H0r$3", "B@tt3ry", "St@pl3"]
password = ""

#### ---- GENERATION ---- ####
parts_index1 = random.randint(0, 10)
parts_index2 = random.randint(0, 10)
parts_index3 = random.randint(0, 10)
password1 = parts[parts_index1]
password2 = parts[parts_index2]
password3 = parts[parts_index3]
password = password1 + password2 + password3
#### ---- OUTPUT ---- ####

print("Your new password is: " + password)
