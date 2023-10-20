T = int(input())
for _ in range(1, T + 1):
    k = int(input())
    n = int(input())


    apart = [[0] * 15 for _ in range(15)]
    for i in range(15):
        for j in range(15):
            if i == 0:
                apart[i][j] += j + 1
            else:
                apart[i][j] = apart[i - 1][j]+apart[i][j - 1]

    print(apart[k][n - 1])