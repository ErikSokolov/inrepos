foo=400
import random

a = []
b = []

for i in range(1):
    a.append(random.randint(1,10))
    b.append(random.randint(1,10))
print(a,b)

c = a + b
print(c)
