#### ---- SETUP ---- ####

player_scores = [1100, 540, 300, 650, 760, 1500, 1800, 200, 100, 800]
good_scores = []
print("Searching for players with scores between 500 and 1000...")


#### ---- FILTER LOOP ---- ####


for score in player_scores:
    if 500 <= score > 1000:
        good_scores.append(score)

player_scores = good_scores
#### ---- FINAL OUTPUT ---- ####

print()
print("Found players that match your level:")
print(player_scores)
