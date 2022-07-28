#### ---- SETUP ---- ####

players = ["Carli", "Geraldo", "Candace", "Michale", "Jaunita", "Oren", "Pauline", "Minh", "Estelle", "Ruben", "Shiela", "Tyrell", "Serafina", "Xavier", "Maddie"]
team1 = []
team2 = []
team3 = []

#### ---- PLAYER ASSIGNMENT ---- ####

team1 = players[0::3]
team2 = players[1::3]
team3 = players[2::3]



#### ---- OUTPUT ---- ####

print("Here are the teams!")

print()
print("TEAM 1:")
for player in team1:
    print(player)

print()
print("TEAM 2:")
for player in team2:
    print(player)

print()
print("TEAM 3:")
for player in team3:
    print(player)
