#!/usr/local/bin/python3.7

import sys

def divideByNumber(numerator, denominator):
    return numerator/denominator

try:
    numerator=int(input("Enter a numerator: "))
    denominator=int(input("Enter a denominator: "))
    if denominator == 0:
        raise ZeroDivisionError("Can't divide by zero")
except (ValueError, ZeroDivisionError) as v:
    print("Exception: ", v)
    sys.exit(1)

res = divideByNumber(numerator, denominator)
print("Division of {} and {} is {}.".format(numerator, denominator, res))

