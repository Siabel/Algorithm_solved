import sys
input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

n = int(input())
planets = [list(map(int, input().split())) for _ in range(n)]

edges = []
res = []

parents = [i for i in range(n + 1)]

# 주어진 배열에서 대각선 기준 한쪽 간선만 넣기
for i in range(n):
    for j in range(i + 1, n):
        edges.append((i, j, planets[i][j]))

# w 를 기준으로 정렬
edges.sort(key=lambda x: x[2])

# kruskal 알고리즘
# 사이클을 생성하지 않는다면 union
for f, t, cost in edges:
    if find_set(f) != find_set(t):
        union(f, t)
        res.append(cost)

print(sum(res))