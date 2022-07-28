#### ---- SETUP ---- ####

import random
print("Initial Scores:")
scores = []
for i in range(7):
    score = random.randint(4, 10)
    print("   Judge " + str(i + 1) + ": " + str(score))
    scores.append(score)

print()
print("To avoid bias, the highest and lowest scores will be dropped.")
print("The order of scores will be also be randomized for anonymity.")
input("Hit enter to hide the scores from the contestant.")
for i in range(100):
    print()

#### ---- SCORE MODIFICATION ---- ####

minimum = min(scores)
maximum = max(scores)
scores.remove(minimum)
scores.remove(maximum)
random.shuffle(scores)
#### ---- OUTPUT ---- ####

print("Contestant, your scores are: ")
total = 0
for score in scores:
    print("   " + str(score))
    total += score
print("Total Score (out of 50): " + str(total))
