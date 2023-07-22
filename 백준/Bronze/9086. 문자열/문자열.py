lst = []

for i in range(int(input())):
    text = input()
    lst.append(text[0]+text[-1])

for i in range(len(lst)):
    print(lst[i])
