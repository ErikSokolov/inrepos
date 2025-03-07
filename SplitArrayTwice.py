foo = 400
import random


a = []

for i in range(8):
    a.append(random.randint(1,10))
print(a)

half = int(len(a)/2)
end = half*2
print(half)
print(end)
i = 0
for i in range(2):
    ping = a[:half]
    pong = a[half:end]
    half_bam  = int(len(ping)/2)
    end_bam = int(len(ping))
    half_bom = int(len(pong)/2)
    end_bam = int(len(pong))
    i = i + 1
    ii = 0
    for ii in range(1):
        bam = ping[:half_bam]
        bambam = ping[half_bam:end_bam]
        bom = pong[:half_bom]
        bombom = pong[half_bom:end_bam]
        ii = ii + 1
print(ping, pong, bam, bom, bambam, bombom)


    


