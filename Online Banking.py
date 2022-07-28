#### ---- INTRODUCTION ---- ####

print("May 1st")
print("Thanks for opening a bank account with us!")
print()

account_balance = int(input("How much money would you like to open your new account with? $"))

print()
print("Your current balance is: $" + str(account_balance))
print()


#### ---- TRANSACTIONS ---- ####

## -- Deposit -- ##

print ("May 15th: Payday!")

deposit = int(input("How much do you have to deposit into your account? $"))

account_balance += deposit
print()
print("Your current balance is: $" + str(account_balance))
print()

## -- Withdrawal -- ##

print("May 21: Your friend's birthday is in a few days and you'd like to buy her a gift. ")

withdraw = int(input("How much would you like to take out of your account to pay for the gift? $"))

account_balance -= withdraw
print()
print("Your current balance is: $" + str(account_balance))
