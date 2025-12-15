for i in range(1,4+1):
    for j in range(1,i):
        print(j,end='')
    print()

for i in range(1,4+1):
    for j in range(i):
        print(i,end='')
    print()


for i in range(0,4+1):
    for j in range(i):
        print(chr(65+j),end='')
    print()



for i in range(0,4+1):
    for j in range(i):
        print(chr(64+i),end='')
    print()
temp=1
for i in range(1,4+1):
    for j in range(i):
        print(temp,end='')
        temp+=1
    print()

for i in range(4,0,-1):
    for j in range(i):
        print('#',end='')
    print()
n=4
for i in range(n):
    for j in range(n-i):
        print('#',end='')
    print()

n=4
for i in range(0,4+1):
    for j in range(1,n-i):
        print(j,end='')
    print()

n=4
for i in range(1,n):
    for j in range(i):
        print('*',end='')
    print()
   
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()


for i in range(1,4+1):
    for j in range():
        print('*',end='')
    print()
    
    