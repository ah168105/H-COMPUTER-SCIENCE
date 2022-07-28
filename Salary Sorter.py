## Salary data from https://www.levels.fyi/


#### ---- SETUP ---- ####

## -- Lists -- ##

companies = ["Adobe", "Amazon", "Apple", "DoorDash", "Dropbox", "Facebook", "Google", "Microsoft", "Tesla", "Uber"]
amounts = [114000, 122107, 127486,  135625, 126000, 120320, 128883, 111081, 116200, 120412]
salaries = []
for i in range(len(companies)):
    salary = str(amounts[i]) + " at " + companies[i]
    salaries.append(salary)

## -- Reverse sort -- ##

salaries.sort()
salaries.reverse()

#### ---- OUTPUT ---- ####

## -- Intro -- ##

print("Let's look at the annual salaries of some entry-level software engineers starting in 2020.")
print()

## -- Loop -- ##
for salary in salaries:
    print("One engineer started at $" + str(salary))
