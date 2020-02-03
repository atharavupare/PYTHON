alpha="abcdefghijklmnopqrstuvwxyz"
noOfLines=int(input("Enter a value less than 26 : "))
for val in range(0,noOfLines+1):
    for no in range(0,val):
        print("",alpha[no],end=' ')
    print("")