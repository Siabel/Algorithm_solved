n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            card = arr[i] + arr[j] + arr[k]
            if card > m:
                continue
            else:
                res = max(res, card)
print(res)