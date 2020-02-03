#!/usr/local/bin/python3.7

import arithmatic

print("__name__ in math.py is: {}".format(__name__))

def factorial(num):
    if num < 0:
        return -1
    if num == 0:
        return 1
    res = 1
    while num > 1:
        res = arithmatic.mult(res, num)
        num = arithmatic.sub(num, 1)
    return res

if __name__ == "__main__":
    print("math module is being run directly")
else:
    print("math module is being imported")
