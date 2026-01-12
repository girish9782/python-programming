for i in range(1,4):
    for j in range(1,10):
        t=j+i-1
        if t%2!=0:
            print("*",end="")
        else:
            print(" ",end="")
    print("")


for i in range(1,5):
    for j in range(1,i+1):
        t=j+i-1
        if t%2!=0:
            print("1",end="")
        else:
            print("0",end="")
    print("")


