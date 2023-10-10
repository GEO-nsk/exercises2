list_of_str = []
list_of_words= []
list_of_all_words = []
new_list_of_words = []
number_of_words = []
cnt = 0

with open('input13.txt', 'r', encoding='utf-8') as ptr:
    for itr in ptr:
        list_of_str.append(itr[:-1])

for itr in list_of_str:
    for x in itr.split():
        x = x.lower()
        list_of_all_words.append(x)
        if x not in list_of_words:
            list_of_words.append(x)

new_list_of_words = sorted(list_of_words)

for itr in new_list_of_words:
    cnt = list_of_all_words.count(itr)
    number_of_words.append(cnt)
    cnt = 0

with open('output13.txt', 'w', encoding='utf-8') as f:
    for itr in range(len(new_list_of_words)):
        print(new_list_of_words[itr], number_of_words[itr],file=f)