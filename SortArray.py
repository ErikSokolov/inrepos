foo=400
import random


a = []

for i in range(2):
    a.append(random.randint(1,10))
print(a)

if a[0] > a[1]:
    swap = a[0]
    swip = a[1]
    a[1] = swap
    a[0] = swip


    


print(a)

