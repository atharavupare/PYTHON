num = int(input("Enter a no.: "))
if num<0:
    print("Enter a positive number!")
else:
    for val in range(num,0,-1):
        if val==6:
            break
        print(val)
    else:
        print("Loop is not terminated with break")