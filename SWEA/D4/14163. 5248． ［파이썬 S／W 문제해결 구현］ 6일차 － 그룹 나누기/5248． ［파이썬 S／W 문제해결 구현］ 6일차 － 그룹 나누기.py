def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])
 
def union(x, y):
    x = find_set(x)
    y = find_set(y)
 
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
 
    if rank[x] == rank[y]:
        rank[x] += 1
 
 
T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    edge = list(map(int, input().split()))
 
    parent = list(range(n+1))
    rank = [0] * (n+1)
 
    for i in range(m):
        x, y = edge[i*2], edge[i*2+1]
        union(x, y)

    for j in range(1, n+1):
        parent[j] = find_set(j)
 
    print(f'#{test_case}', len(set(parent)) - 1)