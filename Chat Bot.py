### Introduction ###
name = input("What is your name? ")
print("Hello " + str(name) + ", it's a pleasure to meet you!")
print("")
print("My name is ChatBot!")
print("I'm going to ask you some questions, and tell you some fun facts based on your responses")
print("")

### Color ###
color = input("What is your favorite color? ")
print("Oh wow! " + str(color) + " is my favorite color too!")
print("")

### Height ###
height = float(input("What is your height in inches? "))
height *= 0.0254
print("That's " + str(height) + " meters!")
height /= 0.0254
height *= 2.54
print("Or " + str(height) + " centimeters!")
print("")

### Age ###
age = int(input("How old are you? "))
age *= 365
print("Did you know that you're over " + str(age) + " days old?")
age /= 365
age *= 31536000
print("That's " + str(age) + " seconds!")
print("")

### Weight ###
weight = float(input("How much do you weigh in pounds? "))
weight *= 0.453592
print("That's " + str(weight) + " kilograms!")
print("")

### GoodBye Message ###
print("I hope you got to learn some fun facts about yourself today")
print("It was fun chatting with you, " + str(name) + "! " + "Have a great day!")
