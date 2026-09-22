"""  11. Check Temperature Category Q11
Given an ambient temperature reading in degrees Celsius, classify the weather condition based on three distinct
thermal tiers:
Temperature Range (°C) Classification Category
> 35 Hot
20 to 35 (inclusive) Normal
< 20 Cold
SAMPLE 1
Input: 38 Output: Hot
SAMPLE 2
Input: 25 Output: Normal """

a = int(input())

if a>=35 :
    print("Hot")
if 20<=a<35 :
    print("Normal")
if a<20 :
    print("cold")

