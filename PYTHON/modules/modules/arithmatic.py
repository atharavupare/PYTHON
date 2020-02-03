#!/usr/local/bin/python3.7

def add(a, b):
    '''Adding two numbers'''
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

print("__name__ in arithmatic.py is: {}".format(__name__))
if __name__ == "__main__":
    print("arithmatic module is being run directly")
else:
    print("arithmatic module is being imported")
