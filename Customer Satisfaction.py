#### ---- SETUP ---- ####

responses = ["happy", "happy", "neutral", "unhappy", "neutral", "happy", "neutral", "happy", "unhappy", "happy", "neutral", "happy", "happy", "neutral", "happy"]
scores = []
total = 0

#### ---- LOOP ---- ####
for response in responses:
    if response == "happy":
        score = 3
    elif response == "neutral":
        score = 2
    elif response == "unhappy":
        score = 1
    scores.append(score)
    total += score




#### ---- OUTPUT ---- ####

print("Customer Responses: " + str(responses))
print("Scores: " + str(scores))
print()
average = total / len(scores)
print("Your average customer service score is " + str(average) + " out of 3")
