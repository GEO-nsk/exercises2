file_name = ''
ans = ''
count = 0
count_str = 0
str_number = '1'

while file_name != 'input4.txt':
    file_name = str(input('имя файла:'))
    if file_name != 'input4.txt':
        print('Такого файла нет')

with open(file_name, 'r', encoding='utf-8') as ptr:
    for i in ptr:
        count_str += 1

while True:
    str_number = str(input('номер строки:'))
    if int(str_number) > count_str:
        print('Такой строки нет')
    else:
        break

with open(file_name, 'r', encoding='utf-8') as ptr:
    for itr in ptr:
        count += 1
        if str(count) == str_number:
            ans = itr

with open('output4.txt', 'w') as f:
    print(ans,file = f)