string_list = list(map(str,input()))

for a in range(len(string_list)):
   string_list[a] = string_list[a].upper()

dictionary = {string : 0 for string in string_list}

for i in dictionary:
    for j in range(len(string_list)):
        if i == string_list[j]:
          dictionary[i] += 1

high_value = max(list(dictionary.values()))
high_key = [k for k, v in dictionary.items() if v == high_value]

if len(high_key) > 1:
   print("?")
else:
   print(*high_key)