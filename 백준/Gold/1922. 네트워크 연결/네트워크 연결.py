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

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

n = int(input())
m = int(input())
parents = [0] * (n + 1)

edge = []
res = []

parents = [i for i in range(n + 1)]

for _ in range(m):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])

# w 를 기준으로 정렬
edge.sort(key=lambda x: x[2])

for f, t, w in edge:
    if find_set(f) != find_set(t):
        union(f, t)
        res.append(w)

print(sum(res))