#!/usr/bin/env python3

# a function that checks if a character is lowercase or not.
# it returns True if lowercase, otherwise it returns false.

def is_lower(char):
    if char >= 'a' and char <= 'z':
        return True
    else:
        return False


print(is_lower('z'))
