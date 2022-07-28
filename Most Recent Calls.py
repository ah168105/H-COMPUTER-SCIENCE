#### ---- CALL LISTS ---- ####

phone_numbers = ["(555-9438)", "(555-3465)", "(555-2349)", "(555-9438)", "(555-1205)"]
contact_names = ["Mom", "Tomas", "Pizza Guy", "Mom", "Ayla"]

#### ---- OUTPUT ---- ####

## -- Introduction -- ##

print("Your five most recent calls:")

## -- Print numbers -- ##

for i in range(len(phone_numbers)):
    label = str(i + 1)
    number = phone_numbers[i]
    name = contact_names[i]
    print(label + ". " + name + " " + number)
