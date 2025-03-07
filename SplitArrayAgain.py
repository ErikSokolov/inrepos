foo = 400
import random


a = []

i = 0
for i in range(random.randint(1,10)):
    a.append(random.randint(1,10))
print(a)

length = len(a)
print(length)

start = int(length/2)
end = start*2
print(start,end)

firstarray = a[:start]
print(firstarray)

lastarray = a[start:end]
print(lastarray)
