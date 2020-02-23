def fileOpen(filename):
    fd = open(filename)
    data=fd.readline()
    count = 0
    while data!='':
        if(count%2!=0):
            print(data)
            data=fd.readline()
            count+=1
        else:
            continue
    print("\n Number of Lines",count)
    fd.close()

if __name__ == "__main__":
    filename = input("Enter the Filename/PATH : ")
    fileOpen(filename)
