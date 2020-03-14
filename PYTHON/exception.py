#!/usr/local/bin/python3.7

import sys

def divideByNumber(numerator, denominator):
    return numerator/denominator

try: #statements under this block are checked for errors
    numerator=int(input("Enter a numerator: "))
    denominator=int(input("Enter a denominator: ")) #if invalid input is passed to int function it will throw ValueError automatically and this error is handled in the except block
    if denominator == 0: #if this condition becomes true
        raise ZeroDivisionError("Can't divide by zero") #throw an exception with raise keyword
except ValueError as v: #error specification under this block
    print("ValueError: ", v)
    sys.exit(1)
except ZeroDivisionError as e: #error specification under this block
    print("Zero division error ", e)
    sys.exit(1)
else: #This block is optional and is called if no error is raised in try block/no exception is occured
    print("Numerator: {}, Denominator: {}".format(numerator, denominator))
    res = divideByNumber(numerator, denominator)
    print("Division of {} and {} is {}.".format(numerator, denominator, res))
finally: #This block is optional and is called always no matter what, whether the exception is raised or not, finally will be executed
    print("Program End")
