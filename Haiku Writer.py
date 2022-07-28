# Print instructions
print("Let's write a haiku together!")
print("A haiku is a short poem that has a specific number of syllables for each line.")
print("The first line has five syllables, the second line has seven, and the third has five.")
print()

# First line
poem = "Code is like a "
poem += input("Enter a one-syllable noun: ")

# Second line
poem += "\nFix a bug and then you "
poem += input("Enter a one-syllable verb: ")

# Third line
poem += "\nMakes me feel "
poem += input("Enter a two-syllable adjective: ")

# Print poem
print()
print(poem)
