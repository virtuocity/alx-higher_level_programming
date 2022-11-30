#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
lastDigit = abs(number) % 10
if lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} {str1}")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif lastDigit != 0 and lastDigit < 6:
    print(f"Last digit of {number} is {lastDigit} {str2}")
if number < 0:
    if lastDigit != 0 and lastDigit < 6:
        print(print(f"Last digit of {number} is {lastDigit} {str2}"))
