N,M = map(int,input().split())
lst = list(0 for n in range(N))

for _ in range(0,M):
    i,j,k = map(int,input().split())
    for n in range(i,j+1):
        lst[n-1] = k

for n in range(N):
    print(lst[n],end =' ')