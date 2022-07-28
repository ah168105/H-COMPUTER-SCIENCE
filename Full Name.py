#### ---- NAME INPUTS ---- ####

## -- Honorific -- ##
full_name = input("What is your honorific (Ms., Mr., Mx., Madam, Sir, Dr., etc.)? ")

## -- First name -- ##
full_name += " " + input("What is your first name? ")


## -- Middle name -- ##
full_name += " " + input("What is your middle name? ")

## -- Last name -- ##
full_name += " " + input("What is your last name? ")

#### ---- GREETING OUTPUT ---- ####

print("Pleased to meet you, " + full_name + "!")
