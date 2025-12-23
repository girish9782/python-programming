count=0
sum=0
for i in range(60,171):
    count+=1
    sum+=i
    if i%9==0:
        print(i)
print(sum)
print(count)