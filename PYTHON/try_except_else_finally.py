#!/usr/local/bin/python3.7

import sys

def divideByNumber(numerator, denominator):
    return numerator/denominator

try:
    numerator=int(input("Enter a numerator: "))
    denominator=int(input("Enter a denominator: "))
    if denominator == 0:
        raise ZeroDivisionError("Can't divide by zero")
except ValueError as v:
    print("Enter integer: ", v)
    sys.exit(1)
except ZeroDivisionError as e:
    print("Zero division error ", e)
    sys.exit(1)
# default 'except' must be last
except:
    print("No exception specified")
else:
    print("No exception while executing try block")
    print("Numerator: {}, Denominator: {}".format(numerator, denominator))
finally:
    print("Finally block will be executed always")

res = divideByNumber(numerator, denominator)
print("Division of {} and {} is {}.".format(numerator, denominator, res))

