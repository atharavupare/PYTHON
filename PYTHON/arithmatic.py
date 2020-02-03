def factorial(num): #THIS FUNCTION FINDS THE FACTORIAL FOR GIVEN NUMBER
    res=1
    if num<0:
        return -1
    while num>0:
        res*=num
        num-=1
    return res
#factorial(5)
print("__name__ in arithmatic.py is {}".format(__name__))