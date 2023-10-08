n = int(input())
arr = []
leng_arr = [[] for _ in range(51)]
res = []

for _ in range(n):
    arr.append(input())

for i in arr:
    leng_arr[len(i)].append(i)

for lst in leng_arr:
    if lst:
        lst.sort()
        for j in lst:
            if j not in res:
                res.append(j)

for a in res:
    print(a)