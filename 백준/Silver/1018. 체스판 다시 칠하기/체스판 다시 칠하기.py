n,m = map(int, input().split())
cnt_lst = []

board = [list(input()) for _ in range(n)]

for i in range(n-7):
    for j in range(m-7):
        cnt_w = 0
        cnt_b = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        cnt_b += 1
                    if board[a][b] != 'B':
                        cnt_w += 1
                else:
                    if board[a][b] != 'B':
                        cnt_b += 1
                    if board[a][b] != 'W':
                        cnt_w += 1
                        
        cnt_lst.append(min(cnt_w, cnt_b))

print(min(cnt_lst))