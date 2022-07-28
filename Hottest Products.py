#### ---- INITIAL STOCK ---- ####

product_names = ["Slinky", "Frisbee", "Barbie", "Pet Rock", "Nintendo", "Furby"]
available_products = ["Slinky", "Slinky", "Frisbee", "Barbie", "Barbie", "Barbie", "Pet Rock", "Pet Rock", "Nintendo", "Furby", "Furby"]
print("You're in luck! We have some of the hottest products available:")
print()
for product_name in product_names:
    number_available = available_products.count(product_name)
    print(product_name + ": " + str(number_available) + " available")
print()

#### ---- PURCHASE ---- ####
for items in available_products:
    available_products.remove(purchase)
    if available_products.count(purchase) == 0:
        product_names.remove(purchase)


#### ---- UPDATED STOCK ---- ####

print()
print("Here is our updated stock:")
print()
for product_name in product_names:
    number_available = available_products.count(product_name)
    print(product_name + ": " + str(number_available) + " available")
