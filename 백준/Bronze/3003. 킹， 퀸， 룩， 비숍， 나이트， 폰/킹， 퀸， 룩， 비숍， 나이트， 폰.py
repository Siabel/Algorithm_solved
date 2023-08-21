arr = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(6):
    arr[i] = chess[i] - arr[i]

print(*arr)