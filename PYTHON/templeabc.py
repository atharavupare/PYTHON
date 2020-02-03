alpha="abcdefghijklmnopqrstuvwxyz"
noOfLines=int(input("Enter a value less than 26 : "))
for curLine in range(0,noOfLines+1):
    for spaces in range(0,noOfLines-curLine+1):
        print("  ",end='')
    for no in range(0,curLine*2-1):
        print("",alpha[no],end='')
    print("")