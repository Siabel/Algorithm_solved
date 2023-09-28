n, k = map(int, input().split())
arr = list(map(int, input().split()))

temp = sum(arr[:k])
res = temp

for i in range(k, n):
    temp += arr[i] - arr[i - k]
    if res < temp:
        res = temp

print(res)