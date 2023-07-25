N = int(input())
M = int(input())

lst = [x for x in range(N,M+1)]

add_list = []

for i in range(0,101):
    if i**2 in lst:
        add_list.append(i**2)
        result = sum(add_list)

if add_list == []:
    print("-1")
else:
    print(result)
    print(min(add_list))