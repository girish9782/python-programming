count=0
for i in range(400,249,-1):
    if i%11==0 and i%13==0:
        count+=1
print(count)