list = []
new_list = []

with open('input10.txt', 'r', encoding='utf-8') as ptr:
    for i in ptr:
        list.append(i)

for i in range(1,len(list),2):
    new_list.append(list[i])

with open('simple/output10.txt', 'w', encoding='utf-8') as f:
    for i in new_list:
        print(i[:-1],file=f)