""" 3. Check Even or Odd Q3
Given an integer, check whether it is evenly divisible by 2 using the remainder modulus operator (%).
Input: A single integer. | Output: Print Even if divisible by 2 with no remainder; otherwise, print Odd.
SAMPLE 1
Input: 24 Output: Even
SAMPLE 2
Input: 19 Output: Odd """



a = int(input())
if a % 2 == 0:
    print("Even")
else:
    print("Odd")