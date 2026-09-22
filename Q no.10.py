"""  10. Find the Largest of Three Numbers Q10
Read three separate integers from input. Using compound conditional logic (such as logical AND) or nested checks,
isolate and print the maximum value among all three.
Input: Three integers provided on separate lines.
Output: Print the single highest integer value.
SAMPLE INPUT
25 48 31
SAMPLE OUTPUT & HINT
48 (Hint: Check if X ≥ Y and X ≥ Z) """


a = input()
if int(a[0])==0 :
    print("It's not a 3 digit Number")
elif int(a[0])>int(a[1]) and int(a[0])>int(a[2]):
    print(int(a[0]))
elif int(a[1])>int(a[2]) and int(a[1])>int(a[0]):
    print(int(a[1]))
else:
    print(int(a[2]))

