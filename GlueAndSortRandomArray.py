foo = 400
import random

a = []
b = []

i = 0
for i in range(random.randint(1,10)):
    a.append(random.randint(1,10))
    b.append(random.randint(1,10))
print(a,b)

c = a + b
print(c)

i = 0
ii = 0
while ii < len(c)-1:
    i = 0
    while i < len(c)-1:
        if c[i] > c[i+1]:
            swap = c[i]
            swip = c[i+1]
            c[i] = swip
            c[i+1] = swap
        i = i + 1
    ii = ii + 1
print(c)




