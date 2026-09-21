""" 5. Divisibility by 5 and 11 Q5
Given a single positive integer, determine whether it is completely divisible by both 5 and 11 simultaneously using the
logical AND operator.
Input: A single integer n. | Output: Print Divisible if n % 5 == 0 and n % 11 == 0, otherwise print Not Divisible.
SAMPLE 1
Input: 55 Output: Divisible
SAMPLE 2
Input: 35 Output: Not Divisible """



a = int(input())
if a%5 == 0 and a%11 ==0:
    print("Divisible")
else:
    print("Not Divisible")