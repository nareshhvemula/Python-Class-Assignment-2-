""" 8. Valid Triangle Check Q8
Given three angles of a triangle as integers, determine whether they form a valid triangle. A triangle is valid if the sum
of all three interior angles is exactly 180° and each angle is strictly greater than 0°.
Input: Three integers on separate lines representing angles a, b, and c.
Output: Print Valid Triangle if valid, else print Invalid Triangle.
SAMPLE 1
Input: 60, 60, 60 Output: Valid Triangle
SAMPLE 2
Input: 90, 90, 10 Output: Invalid Triangle """




a = int(input())
b = int(input())
c = int(input())

if (a+b+c==180) and (a>0 and b>0 and c>0):
    print("Valid Triangle")
else:
    print("Invalid Triangle")