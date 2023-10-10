ans = ''

with open('input3.txt', 'r', encoding='utf-8') as ptr:
    for itr in ptr:
        ans += itr[-2:-1]

with open('output3.txt', 'w', encoding='utf-8') as f:
    print(ans,file = f,)