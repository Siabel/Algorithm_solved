a=[]
for i in range(1,29):
    a.append(int(input()))
a.sort()
for i in range(1,31):
    if(i in a):
        continue
    else:
        print(i)