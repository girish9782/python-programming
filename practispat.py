x=1
for i in range(1,6):
    temp=x
    for j in range(1,6-i+1):
        print(temp ,end=" ")
        temp+=1
    x+=2
    print(" ")
