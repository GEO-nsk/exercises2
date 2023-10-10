file_name = ''
count = 0
ans = ''

while file_name != 'input4.txt':
    try:
        file_name = str(input('имя файла:'))

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
    except FileNotFoundError:
        print('Такого файла нет')