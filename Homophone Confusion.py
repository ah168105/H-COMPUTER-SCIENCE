#### ---- SETUP ---- ####

paragraph = "You know its important to type carefully, but sometimes your in a rush and you're writing has some typos. The document your working on might have some words swapped, and it's spellcheck feature may not always find you're mistakes."

print("Original:")
print(paragraph)
print()

#### ---- SWAP ---- ####

## -- First swap -- ##

paragraph = paragraph.replace("its", "*TEMP*")
paragraph = paragraph.replace("it's", "*TEMP*")
paragraph = paragraph.replace("*TEMP*", "it's")

## -- Second swap -- ##

paragraph = paragraph.replace("your", "*TEMP*")
paragraph = paragraph.replace("you're", "*TEMP*")
paragraph = paragraph.replace("*TEMP*", "you're")

#### ---- OUTPUT ---- ####

print("Fixed:")
print(paragraph)
