noOfLines = int(input("Enter the number of lines : "))
for currLine in range(1,noOfLines):
    noOfStars = currLine*2-1
    noOfSpaces = noOfLines-currLine
    print(" "*noOfSpaces+"*"*noOfStars)
for currLine in range(noOfLines,0,-1):
    noOfStars = currLine*2-1
    noOfSpaces = noOfLines-currLine
    print(" "*noOfSpaces+"*"*noOfStars)