list = []

with open('input8.txt', 'r') as ptr:
    for itr in ptr:
        if '100' not in itr:
            list.append(itr[:-1])

with open('input8.txt', 'w') as f:
    for itr in list:
        print(itr,file=f)


