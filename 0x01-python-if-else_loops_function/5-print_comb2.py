#!/usr/bin/env python3

"""
print all possible combination of two numbers - from 0 to 90, separated by commas.
Pairs must not repeat itself.
e.g. 01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89.
"""

for num1 in range(0, 9):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print(f'{num1}{num2}', sep="")
        else:    
            print(f"{num1}{num2}, ", end="")