arr = [list(map(int, input().split())) for _ in range(9)]
max_v = 0
x, y = 0, 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_v:
            max_v = arr[i][j]
            x,y = i + 1, j + 1

print(max_v)
print(x, y)