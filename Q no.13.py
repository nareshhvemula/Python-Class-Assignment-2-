"""  13. Grade Calculator Q13
Accept a student's total test score (integer) and determine their academic letter grade based on the following
classification scale:
Marks Range Grade Marks Range Grade
90 – 100 A 75 – 89 B
60 – 74 C 40 – 59 D
Below 40 F
EXAMPLE 1
Input: 82 → Output: B
EXAMPLE 2
Input: 35 → Output: F """



a = int(input())
if a>100 :
    print("They are not Marks, you idiot.")
if 100>=a>90 :
    print("A")
elif 75<a<=89 :
    print("B")
elif 60<a<=74 :
    print("C")
elif 40<=a<=59 :
    print("D")
else :
    print("F")