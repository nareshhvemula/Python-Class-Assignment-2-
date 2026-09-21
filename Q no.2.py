""" 2. Check Positive, Negative, or Zero Q2
Given an integer value, determine whether it lies strictly above zero, strictly below zero, or is exactly zero.
Input: A single integer. | Output: Print Positive if > 0, Negative if < 0, and Zero if 0.
SAMPLE 1
Input: -8 Output: Negative
SAMPLE 2
Input: 0 Output: Zero """



a = int(input())
if a > 0:
    print("Positive")
if a < 0:
    print("Negative")
if a==0:
    print("Zero")