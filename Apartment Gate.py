#### ---- INPUT ---- ####

print("Welcome to the Forest Hallways Apartment Complex!")
entry = input("Enter your five-digit code: ")

#### ---- OUTPUT ---- ####

## -- List of codes -- ##
codes = ["04786",
         "12795",
         "25255",
         "31251",
         "76220"
        ]


## -- Response to input -- ##
for code in codes:

    if entry == code:
        print("Welcome home!")
        break

else:
    print("That code was not found.")
        
