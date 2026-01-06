for i in range(1,4):
    temp=1
    for j in range(4,0,-1):

        print(j,end=" ")
        temp+=1
    print("")

for i in range(5,1,-1):
    for j in range(1,4):

        print(i,end=" ")
        temp+=1
    print("")

temp=1
for i in range(1,4):
    for j in range(1,4):

        print(temp,end=" ")
        temp+=1
    print("")



for i in range(1,5):
    temp=7
    for j in range(1,5):

        print(temp,end=" ")
        temp-=1
    print("")


for i in range(1,4):
    temp=65
    for j in range(1,4):

        print(temp,end=" ")
        temp+=1
    print("")

for i in range(1,4):
    ch=0
    for j in range(1,4):

        print(chr(65+ch),end=" ")
        ch+=1
    print("")

for i in range(1,4):
    for j in range(1,i+1):

        print("*",end=" ")
        temp+=1
    print("")

for i in range(1,4):
    
    for j in range(1,5-i+1):

        print("*",end=" ")
        temp+=1
    print("")


for i in range(1,5):
    temp=2
    for j in range(1,5-i+1):

        print(temp,end=" ")
        temp+=1
    print("")

for i in range(1,5):
    temp=0
    for j in range(1,i+1):

        print(chr(65+temp),end=" ")
        temp+=1
    print("")
 



temp=0
for i in range(1,5):
   
    for j in range(1,i+1):

        print(chr(65+temp),end=" ")
        temp+=1
    print("")


for i in range(1,5):
    temp=0
    for j in range(1,5-i+1):

        print(i+temp,end=" ")
        temp+=1
    print("")

 

x=4
for i in range(1,5):
    temp=x
    for j in range(1,5-i+1):

        print(temp,end=" ")
        temp+=1
    x+=1
    print("")


for i in range(1,6):
    
    
    x=1
    for j in range(1,6-i+1):
         if (j%2!=0):
           print(1,end=" ")
         else:
           print(0,end=" ")
    print("")

x=1
for i in range(1,4):
    
    
  
    for j in range(1,4-i+1):
       print(chr(64+x),x,end=" ")
       x+=1
    print("")

x=1
for i in range(1,6):
    
    

    for j in range(1,6-i+1):
         if (j%2!=0):
           print(x,end=" ")
         else:
           print(x+2,end=" ")
    x+=1
    print("")





