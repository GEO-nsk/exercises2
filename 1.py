with open('input.txt', 'r', encoding='utf-8') as ptr:
    for itr in ptr:
        print(itr)
        big_ptr = itr.upper()

with open('output.txt', 'w', encoding='utf-8') as f:
    print(big_ptr,file = f)