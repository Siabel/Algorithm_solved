word = input()
word_lst = list(map(str,word))
word_length = len(word)


for i in range(0,word_length):
    if str.isupper(word_lst[i]) == True:
        word_lst[i] = str.lower(word_lst[i])
    elif str.islower(word_lst[i]) == True:
        word_lst[i] = str.upper(word_lst[i])
    
print(*word_lst,sep = '')