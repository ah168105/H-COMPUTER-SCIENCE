#### ---- SETUP ---- ####

## -- Site visits from oldest to newest -- ##

visits = (117, 98, 134, 148, 122, 132, 121, 142, 123, 138, 166, 180, 295, 311, 326, 476, 523)

max_visits = 0
min_visits = 0
avg_visits = 0

#### ---- CALCULATIONS ---- ####

## -- Maximum and minimum -- ##

max_visits = max(visits)
min_visits = min(visits)


## -- Average -- ##

total = 0
last_ten_days = visits[-10:]
for visit in last_ten_days:
    total += visit

avg_visits = total / 10



#### ---- OUTPUT ---- ####

print("Maximum number of visits in a day: " + str(max_visits))
print("Minimum number of visits in a day: " + str(min_visits))
print("Average visits over the last 10 days: " + str(avg_visits))
