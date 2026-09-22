"""  9. Check Pass or Fail Q9
A candidate takes a standard examination. To qualify, the student must achieve a benchmark score of 40 marks or
above out of the maximum score.
Input: A single integer representing candidate's mark. | Output: Pass if mark ≥ 40, else Fail.
TEST CASE 1
Input: 67 Output: Pass
TEST CASE 2
Input: 32 Output: Fail """




a = int(input())
if a >= 40 :
    print("Pass")
else :
    print("Fail")