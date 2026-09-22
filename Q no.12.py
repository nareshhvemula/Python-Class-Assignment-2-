"""  12. Calculate Discount Q12
A retail store offers a conditional 10% discount on orders whose total billing value is ≥ 1000. Compute and print the
final payable amount.
Formula: If amount ≥ 1000, Discount = 10%; Final = amount - (amount × 0.10).
SAMPLE INPUT & OUTPUT
Input: 1500 Output: 1350
COMPUTATION TRACE
1500 × 10% = 150 Final = 1500 - 150 = 1350  """



a = int(input())

if a>=1000:
    print(a-((a/100)*10))
else :
    print(a)