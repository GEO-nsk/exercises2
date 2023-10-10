list = []

with open('input2.txt', 'r', encoding='utf-8') as ptr:
    for itr in ptr:
        if itr[0:1] == 'A':
            list.append(itr)

with open('output2.txt', 'w', encoding='utf-8') as f:
    for itr in list:
        print(itr[:-1],file = f,)