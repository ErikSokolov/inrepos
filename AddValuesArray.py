foo = 400
import random


a = []

for i in range(random.randint(1,10)):
    a.append(random.randint(1,10))
print(a)

length = len(a)
ca = a 

ii = 1
i = 0
while i < length:
    ca.insert(ii, 0)
    ii = ii + 2
    i = i + 1
print(ca)
