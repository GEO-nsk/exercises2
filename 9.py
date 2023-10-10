list = []

mounth1 = 0
mounth2 = 0
mounth3 = 0
mounth4 = 0
mounth5 = 0
mounth6 = 0
mounth7 = 0
mounth8 = 0
mounth9 = 0
mounth10 = 0
mounth11 = 0
mounth12 = 0

with open('input9.txt', 'r') as ptr:
    for i in ptr:
        list.append(i)

for i in range(0,30):
    mounth1 += int(list[i])
for i in range(31,58):
    mounth2 += int(list[i])
for i in range(59,89):
    mounth3 += int(list[i])
for i in range(90,119):
    mounth4 += int(list[i])
for i in range(120,150):
    mounth5 += int(list[i])
for i in range(151,180):
    mounth6 += int(list[i])
for i in range(181,211):
    mounth7 += int(list[i])
for i in range(212,242):
    mounth8 += int(list[i])
for i in range(243,272):
    mounth9 += int(list[i])
for i in range(273,303):
    mounth10 += int(list[i])
for i in range(304,334):
    mounth11 += int(list[i])
for i in range(334,364):
    mounth12+= int(list[i])

with open('output9.txt', 'w') as f:
    print(mounth1,file=f)
    print(mounth2,file=f)
    print(mounth3,file=f)
    print(mounth4,file=f)
    print(mounth5,file=f)
    print(mounth6,file=f)
    print(mounth7,file=f)
    print(mounth8,file=f)
    print(mounth9,file=f)
    print(mounth10,file=f)
    print(mounth11,file=f)
    print(mounth12,file=f)
