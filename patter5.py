n=5
for i in range(1,n+1):
    temp=n
    for j in range(i):
        print(chr(65+temp-i),end='')
        temp+=1
    print()