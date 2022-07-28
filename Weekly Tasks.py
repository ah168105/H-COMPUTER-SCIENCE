#### ---- SETUP ---- ####

tasks = "Amir will sharpen pencils and collect any attempts at this week's puzzle, and Haley will collect breakfast trash and pass out graded work."

print("This week:")
print(tasks)

#### ---- SWAP ---- ####

tasks = tasks.replace("Amir", "*TEMP*")
tasks = tasks.replace("Haley", "Amir")
tasks = tasks.replace("*TEMP*", "Haley")
#### ---- OUTPUT ---- ####

print("Next week:")
print(tasks)
