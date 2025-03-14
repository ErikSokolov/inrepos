foo = 400
import random
import time


a = []

for i in range(random.randint(1,10)):
    a.append(random.randint(1,10))
print(a)

length = len(a)
copylength = length

i = 0
while i < length:
    a.pop() 
    time.sleep(1)
    i = i + 1
    print(a)
print(a)
