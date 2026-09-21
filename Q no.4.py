""" 4. Find the Greater Number Q4
Compare two distinct integer variables, a and b. Determine which value dominates, or identify if they share identical
values.
Input: Two lines containing integer a and integer b respectively.
Output: a is greater if a > b, b is greater if b > a, or Equal if identical.
SAMPLE 1
Input: 25, 18 Output: a is greater
SAMPLE 2
Input: 30, 30 Output: Equal """



a = int(input())
b = int(input())
if a>b :
    print("a is grater")
if b>a:
    print("b is grater")
if a==b:
    print("Equal")