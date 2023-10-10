list = []

with open('input11.txt', 'r') as list_of_numbers:
    for i in list_of_numbers:
        number = int(i[:-1])
        list.append(number)

list = sorted(list)
list_sorted = list[::-1]

with open('output11.txt', 'w') as f:
    for i in list_sorted:
        print(i,file=f)