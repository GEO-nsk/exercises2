list = []

with open('input7.txt', 'r') as ptr:
    for itr in ptr:
        list.append(itr)

number1 = int(list[0])
number2 = int(list[1])
number3 = int(list[2])
ans = (number1/number2) + number3

with open('output7.txt', 'w') as f:
    print(ans,file = f,)