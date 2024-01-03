#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{random.randint} is positive")
elif number == 0:
    print("{random.randint} is zero")
else:
    print("{random.randint} is negative")
