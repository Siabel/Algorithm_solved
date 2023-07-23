N,M = map(int,input().split())
lst = [n+1 for n in range(N)]

for _ in range(M):
    i,j = map(int,input().split())

    lst[i-1],lst[j-1] = lst[j-1],lst[i-1]

for n in range(N):
    print(lst[n], end = ' ')