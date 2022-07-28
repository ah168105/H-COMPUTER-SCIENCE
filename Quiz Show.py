#### ---- INTRODUCTION ---- ####

print("Welcome!  You are the next contestant!")
print("Answer all three questions correctly to win the grand prize.")
print()

#### ---- QUESTIONS ---- ####

print("Question 1: How many teeth does an aardvark have?")
print("a) 0     b) 4     c) 24     d) 108")
q1_correct = input("Choose a letter: ") == "a"

print()
print("Question 2: What degree temperature is the boiling point of water on the Celsius scale?")
print("a) 0    b) 100     c) 212     d) 500")
q2_correct = input("Choose a letter: ") == "b"

print()
print("Question 3: What is a group of lions known as?")
print("a) colony     b) family     c) pride     d) school")
q3_correct = input("Choose a letter: ") == "c"
print()

#### ---- QUIZ GRADER ---- ####

## -- All correct -- ##
if q1_correct and q2_correct and q3_correct:
    print("Congratulations!! You answered all three questions correctly. You win the grand prize!")

## -- Some correct -- ##
if not q1_correct or not q2_correct or not q3_correct:
    print("Nice try! You correctly answered at least one question. See if you can get them all right next time!")

## -- None correct -- ##
if not q1_correct and not q2_correct and not q3_correct:
    print("Study more random facts and try again.")
