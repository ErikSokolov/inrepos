foo=400
import random

a = []
b = []
c = []

i = 0
for i in range(10):
    a.append(random.randint(1,10))
    b.append(random.randint(1,10))
print(a,b)


i = 0
while i < 10:
    sum = a[i]-b[i] 
    c.append(sum) 
    i = i + 1
print(c)

