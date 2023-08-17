n, m = map(int, input().split())
arr_1 = [list(map(int,input().split())) for _ in range(n)]

m, k = map(int, input().split())
arr_2 = [list(map(int,input().split())) for _ in range(m)]

result = [[0] * k for _ in range(n)]

for a in range(n):
    for b in range(m):
        for c in range(k):
            result[a][c] += arr_1[a][b] * arr_2[b][c]
        
for num in result:
    print(*num)