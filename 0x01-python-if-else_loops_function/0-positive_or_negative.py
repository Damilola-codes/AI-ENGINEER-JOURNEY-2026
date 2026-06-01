#!/usr/bin/env python3
"""
This should print if a number is positive, negative or zero.
"""
import random

number = random.randint(-10, 10)

if number == 0:
    number = 0
    print(f"{number} is zero")

elif number > 0:
    print(f"{number} is positive")

else:
    print(f"{number} is negative")
