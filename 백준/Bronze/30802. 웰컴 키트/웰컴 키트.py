n = int(input())
arr = list(map(int,input().split()))
t, p = map(int, input().split())

minT = 0
for i in range(len(arr)):
    if arr[i] % t == 0:
        minT += int(arr[i] / t)
    else:
        minT += (int(arr[i] / t) + 1)

print(minT)

minP = [int(sum(arr) / p), sum(arr) % p]
print(*minP)