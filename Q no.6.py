""" 6. Check Leap Year Q6
A year is a leap year if it is divisible by 4, except for end-of-century years, which must also be divisible by 400. (Divisible
by 4 and not 100, or divisible by 400).
Input: A four-digit integer representing the year. | Output: Print Leap Year or Not a Leap Year.
SAMPLE 1
Input: 2024 Output: Leap Year
SAMPLE 2
Input: 1900 Output: Not a Leap Year """



a = int(input())
if a%4==0 and not(a%100==0) or a%400==0 :
    print("Leap year")
else :
    print("Not a Leap Year")