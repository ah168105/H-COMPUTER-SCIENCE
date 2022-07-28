#### ---- SETUP ---- ####

wait_list = ["Shantelle", "James", "Amy", "Barbara", "Daniel", "Arnie", "Maggie"]
print("As the host of this restaurant, you can use this program to check the position and estimated wait time of anyone on the list")

#### ---- OUTPUT ---- ####

## -- Wait list -- ##

print()
print("The following people are waiting for a table: ")
for person in wait_list:
    print(person)
print()

## -- Wait time -- ##

name = input("Enter the name of the person you'd like to get an estimated wait time for: ")

if name in wait_list:
    print("Sorry, that person isn't on the list yet")
else:
    name_index = wait_list.index(name)
    time - name_index * 5
    print("They are her, but there are " + str(name_index) + " waiting head of them. The estimated wait time is of " + str(time) + " minutes. ") 
