"""
Adnan Hossain
Student Project
Project Title: Pythagoren Theorem Calculator
"""
import math

print("This is a Pythagorean Theorem calculator! Use this program to calculate your triangle sides.")
print("Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle)")
two_sides = input("Which 2 side lengths do you have from a, b, and c? Please write your answer like the example. (ex. a and b or A and B) ")

#Variables for when the 2 side lengths the user has is sides a and b
a_and_b = two_sides == "a and b"
A_and_B = two_sides == "A and B"
b_and_a = two_sides == "b and a"
B_and_A = two_sides == "B and A"

#Variables for when the 2 side lengths the user has is sides b and c
b_and_c = two_sides == "b and c"
B_and_C = two_sides == "B and C"
c_and_b = two_sides == "c and b"
C_and_B = two_sides == "C and B"

#Variables for when the 2 side lengths the user has is sides a and c
a_and_c = two_sides == "a and c"
A_and_C = two_sides == "A and C"
c_and_a = two_sides == "c and a"
C_and_A = two_sides == "C and A"

#Find the missing side of c by adding the square root of a and b
if a_and_b or A_and_B or b_and_a or B_and_A:
    side_a = int(input("Input the length of side a: "))
    side_b = int(input("Input the length of side b: "))

    side_c = math.sqrt(side_a**2 + side_b**2)
    
    print("The length of side c is: ")
    print(side_c)

#Find the missing side of a by subtracting the square root of c and b
elif b_and_c or B_and_C or c_and_b or C_and_B:
    side_b = int(input("Input the length of side b: "))
    side_c = int(input("Input the length of side c: "))
    
    side_a = math.sqrt((side_c**2) - (side_b**2))
    
    print("The length of side a is: ")
    print(side_a)

#Find the missing side of b by subtracting the square root of c and a    
elif a_and_c or A_and_C or c_and_a or C_and_A:
    side_a = int(input("Input the length of side a: "))
    side_c = int(input("Input the length of side c: "))
        
    side_b = math.sqrt((side_c**2) - (side_a**2))
    
    print("The length of side b is: ")
    print(side_b)
    
#If the user doesn't write their 2 side lengths properly, this asks the user to reinput their side lengths
else:
    print("Please give two side lengths between a, b, c (ex, a and b)")
