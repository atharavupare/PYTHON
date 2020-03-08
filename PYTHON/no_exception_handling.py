#!/usr/local/bin/python3.7

import sys

def divideByNumber(numerator, denominator):
    return numerator/denominator

numerator=int(input("Enter a numerator: "))
denominator=int(input("Enter a denominator: "))
if denominator == 0:
    print("Can't divide by zero")
    sys.exit(0)

res = divideByNumber(numerator, denominator)
print("Division of {} and {} is {}.".format(numerator, denominator, res))
