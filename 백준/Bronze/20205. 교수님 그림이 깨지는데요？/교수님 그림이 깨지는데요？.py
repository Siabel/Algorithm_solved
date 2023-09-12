n,k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for _ in range(k):

        for j in range(n):
            for _ in range(k):

                print(arr[i][j], end=' ')
        print()