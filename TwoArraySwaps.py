foo=400
import random


a=[]
b=[]

for i in range(10):
    a.append(random.randint(1,10))
    b.append(random.randint(1,10))
print(a,b)


i = 0
while i < len(a):
    swip = a[i] 
    swap = b[i] 
    a[i] = swap
    b[i] = swip
    i = i + 1
print(a,b)

    
