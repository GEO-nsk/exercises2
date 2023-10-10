file_name = ''
ans = ''
count = 0
count_str = 0
str_number = '1'

while file_name != 'input4.txt':
    file_name = str(input('имя файла:'))
    if file_name != 'input4.txt':
        print('Такого файла нет')

str_number = str(input('номер строки:'))

with open(file_name, 'r', encoding='utf-8') as ptr:
    for itr in ptr:
        count += 1
        if str(count) == str_number:
            ans = itr

if count < int(str_number):
    print('Такой строки нет')

with open('output4.txt', 'w', encoding='utf-8') as f:
    print(ans,file = f)