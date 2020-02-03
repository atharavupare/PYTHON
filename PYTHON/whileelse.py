num = int(input("Enter a no.: "))
if num<0:
    print("Enter a positive number!")
else:
    while num>0:
        if num==6:
            break
        print(num)
        num-=1
    else:
        print("Loop is not terminated with break")