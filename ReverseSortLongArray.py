foo=400
import random

a = []

i=0
for i in range(random.randint(1,10)):
    a.append(random.randint(1,10))
print(a)

i = 0
ii = 0
while ii < len(a)-1:
    i = 0
    while i < len(a)-1:
        if a[i] < a[i + 1]:
            swap = a[i]
            swip = a[i + 1]
            a[i+1] = swap
            a[i] = swip
        i = i+1
    ii = ii+1
print(a)

