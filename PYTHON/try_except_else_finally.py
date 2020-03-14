#!/usr/local/bin/python3

import sys

def divideByNumber(numerator, denominator):
    return numerator/denominator
flag = True
while(flag==True):
    flag = False
    try:
        numerator=int(input("Enter a numerator: "))
        denominator=int(input("Enter a denominator: "))
        res = divideByNumber(numerator, denominator)
        print("Division of {} and {} is {}.".format(numerator, denominator, res))
    except ValueError as v:
        print("Enter integer: ", v)
    except ZeroDivisionError as e:
        print("Zero division error ", e)
    #default 'except' must be last
    #execept block without any name is generic exception block which means Whenever any other error than specified error is occured then this block is executed
    except:
        print("No exception specified")
    else:
        flag = True #if no exception is occured then flag is set to True
        print("No exception while executing try block")
        print("Numerator: {}, Denominator: {}".format(numerator, denominator))
    finally:
        print("Finally block will be executed always")
        if(flag == False):
            sys.exit(1)
