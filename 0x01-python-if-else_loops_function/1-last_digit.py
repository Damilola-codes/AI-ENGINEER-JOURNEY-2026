#!/usr/bin/env python3
import random
number = random.randint(-100, 100)

last_digit = abs(number) % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero.")
elif last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and less than 6 and not zero.")
print(number)
print(last_digit)
