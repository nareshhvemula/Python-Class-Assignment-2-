""" 7. Alphabet Case Identifier Q7
Given a single character from the Latin alphabet, determine whether the character is uppercase or lowercase using
ASCII code comparisons or character comparison operators.
Input: A single character. | Output: Print Uppercase if 'A' ≤ char ≤ 'Z', or Lowercase if 'a' ≤ char ≤ 'z'.
SAMPLE 1
Input: G Output: Uppercase
SAMPLE 2 
Input: m Output: Lowercase """



nari = input()
if "A" <=nari<= "Z" :
    print("Uppercase")
elif "a" <=nari<= "z":
    print("Lowercase")
else :
    print("Not an alphabet")
