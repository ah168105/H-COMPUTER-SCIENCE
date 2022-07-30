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

    ## -- Adding a new card -- ##
    if user == "buy":

        card_buy = input("Enter a code for the new card: ")
        card_amount = int(input("Enter the amount of money for the new card: "))
            ## -- Code check -- ##
        while card_buy in valid:
            print("invalid")
            card_buy = input("Enter a code for the new card: ")


        ## -- Adding card -- ##
        valid.append(card_buy)
        amount.append(card_amount)
        print(str(card_buy) + " has been added with a balance of $" + str(card_amount) + " successfully.")
