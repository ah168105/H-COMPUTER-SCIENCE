#### ---- SETUP ---- ####

## -- Starting cards -- ##
valid = ["ASDF", "1234", "QWER", "ZXCV", "0000"]
amount = [100, 50, 75, 20, 50]


## -- Intro -- ##
print("Welcome to the Gift Card service app.")


#### ---- MAIN LOOP ---- ####
while True:

    user = input("Enter 'use' to use a card, 'buy' to buy a card, or 'exit' to quit: ")


    ## -- Exiting -- ##
    if user == "exit":
        break


    ## -- Using a card -- ##
    if user == "use":
        card_use = input("Enter the code of the card you want to use: ")


        ## -- Code check -- ##
        while card_use not in valid:
            print("Invalid")
            card_use = input("Enter the code of the card you want to use: ")


        ## -- Balance display -- ##
        card_amount = amount[valid.index(card_use)]
        
        print("Your card's balance is $" + str(card_amount))

        ## -- Spending balance -- ##
        spend_card = int(input("How much would you like spend? "))
        if spend_card > card_amount:
            print("That is more money than you have available.")
        else:
            card_amount -= spend_card
            amount[valid.index(card_use)] = card_amount
        
        print("You have $" + str(card_amount) + " left in your card.")



        ## -- Removing card -- ##
        if card_amount == 0:
            del amount[valid.index(card_use)]
            del valid[valid.index(card_use)]
            print(str(card_use) + " has been removed!")

        ## -- Invalid input -- ##



    ## -- Adding a new card -- ##
if user == "buy":

    buy_card = input("Enter a code for the new card: ")
    valid.insert(0, buy_card)
    amount.append(100)
    card_amount = 100
    print("A new card has been added with code " + str(buy_card) +" and a balance of $" + str(card_amount))
        ## -- Code check -- ##
    while buy_card in valid:
        print("invalid")
        buy_card = input("Enter a code for the new card: ")


        ## -- Adding card -- ##
    valid.append(buy_card)
    amount.append(100)
    print(str(buy_card) + " has been added with a balance of $100.")
