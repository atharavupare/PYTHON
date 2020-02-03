#!
a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))
c=int(input("Enter number 3 "))
if a>b and a>c:
    print("a is largest, value is ",a)
elif b>c and b>a:
    print("b is largest, value is ",b)
elif c>a and c>b:
    print("c is largest, value is ",c)
else:
    if a==b and a==c:
        print("all are equal, values are ",a)
    elif a==c:
        print("a and c are equal, values are ",a)
    elif a==b:
        print("a and b are equal, values are ",a)
    elif b==c:
        print("b and c are equal, values are ",b)
    else:
        print("error")