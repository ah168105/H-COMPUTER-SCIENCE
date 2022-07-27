cost= 0
topping_cost =2
size = input("Enter your pizza size (s, m, l): " )
if size == "s":
    cost=5
elif size == "m":
    cost=10
elif size ==  "l":
    cost=15
topping = (int(input("How many toppings do you want? ")))
topping_total = topping * topping_cost
cost += topping_total
print("Your total pizza cost is $" + str(cost))

