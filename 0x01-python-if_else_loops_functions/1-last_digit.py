#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if number < 0:
    ld = ld - 10
if number % 10 > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number} is {ld} and is 0")
else:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
