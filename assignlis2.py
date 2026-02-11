numbers=[0,1,0,3,12]
a=[]
for i in numbers:
    if i==0:
        numbers.append(i)
        numbers.remove(i)

    
print(numbers)