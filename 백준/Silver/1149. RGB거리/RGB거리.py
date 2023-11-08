n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

res = [[] for _ in range(n)]
res[0] = board[0]

for i in range(1,n):
    res[i] = [
        board[i][0] + min(res[i - 1][1],res[i - 1][2]),
        board[i][1] + min(res[i - 1][0],res[i - 1][2]),
        board[i][2] + min(res[i - 1][0],res[i - 1][1]),
    ]

print(min(res[n - 1]))