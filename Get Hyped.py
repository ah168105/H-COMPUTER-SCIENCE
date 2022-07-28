#### ---- INPUT ---- ####

phrase = input("Enter a sentence to make more exciting: ")

#### ---- STRING CHANGES ---- ####

## -- Capitalization -- ##

words = phrase.split()
for word in words:
    if len(word) > 4:
        new = word.upper()
        words[words.index(word)] = new

sentence = " ".join(words)



## -- Punctuation -- ##

sentence = sentence.replace(".", "!")

#### ---- OUTPUT ---- ####

print(sentence)
