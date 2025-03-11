foo = 400
import random


a = []

for i in range(random.randint(1,10)):
    a.append(random.randint(1,100))
print(a)

half = int(len(a)/2)

makefront = a[half:half*2]
makeback = a[:half]

rev = makefront + makeback
print(rev)

copmakeback = makeback

print(makefront)

i = 0
while i < len(makefront):
    copmakeback.insert(0+i,makefront[i])
    i = i + 1
print(copmakeback)

