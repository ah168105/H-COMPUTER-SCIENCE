#### ---- SETUP ---- ####

print("This program converts lines from stage plays to sentences.")
print()
dialog1 = "Amy\nAnd now we're back at square one..."
dialog2 = "Joe\nAt least this time we have snacks!"

#### ---- LINE CONVERSION ---- ####

split1 = dialog1.split("\n")
split2 = dialog2.split("\n")
name1 = split[0] + "."
name2 = split2[0] + "."
sentence1 = "\"" + split1[1] + "\""
sentence2 = "\"" + split2[1] + "\""


#### ---- OUTPUT ---- ####

print("-Original Lines-")
print()
print(dialog1)
print()
print(dialog2)
print()

print("-Lines as Sentences-")
print()

print(sentence1 + "said " + name1)
print(sentence2 + "said " + name2)
