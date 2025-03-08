foo = 400
import random


a = []
b = []

for i in range(10):
    a.append(random.randint(1,10))
    b.append(random.randint(1,10))
print(a,b)

bar = 0

i = 0
while i < len(a)/2:
    swap = a[bar]
    swip = b[bar]
    b[bar] = swap
    a[bar] = swip
    bar = bar + 2
    i = i + 1
print(a,b)
