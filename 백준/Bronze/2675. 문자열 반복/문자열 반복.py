T = int(input())

for _ in range(T):
    res = []
    n, arr = input().split()
    n = int(n)
    for i in range(len(arr)):
        res.append(arr[i] * n)

    print(''.join(res))