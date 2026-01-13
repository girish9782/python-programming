# list comprhehension is a concise and easy way to create a new list
newlist=[i for i in range(1,10)]
print(newlist)
newlist=[i**2 for i in range(1,10)]
print(newlist)
newlist=[i for i in range(1,10) if i%2==0]
print(newlist)
newlist=[i for i in range(1,10) if i%2!=0]
print(newlist)

new=[(i) for i in range(1,4) for j in range(5,7)]
print(new)
newlist=[]
for i in range(5,10):
    templist=[]


    templist.append(i)
    newlist.append(templist)
    print(newlist)

newlist=[]
for i in range(5,10):
    templist=[]


    templist.append(i)
    newlist.append(templist)
    print(newlist)

x=5
newlist=[]
for i in range(1,4):
    templist=[]
    for j in range(1,i+1):
        templist.append(x)
        x+=1
    newlist.append(templist)
    print("")
print(newlist)


newlist=[]
for i in range(1,5):
    templist=[]
    x=1
    for j in range(1,i+1):
        templist.append(x)
        x+=1
    newlist.append(templist)
    print("")
print(newlist)

