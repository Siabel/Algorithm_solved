import sys
input = sys.stdin.readline

board = []

for _ in range(8):
    arr = list(map(str,input()))
    board.append(arr)

res = 0
for i in range(8):  
    for j in range(8):
        if (i + j) % 2==0:
            if board[i][j]=='F':
                res += 1

print(res)