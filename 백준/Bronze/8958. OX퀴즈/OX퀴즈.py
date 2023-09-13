T = int(input())

for _ in range(T):
    arr = list(input())
    res = 0
    cnt = 0

    for i in arr:
        if i == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0

    print(res)