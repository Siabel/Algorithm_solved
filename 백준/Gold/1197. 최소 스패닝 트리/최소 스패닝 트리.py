import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

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

v, e = map(int, input().split())

graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key=lambda x: x[2])

parents = [i for i in range(v + 1)]

cnt = 0
sum_weight = 0
for a, b, c in graph:
    if find_set(a) != find_set(b):
        cnt += 1
        sum_weight += c
        union(a, b)

        if cnt == v:
            break

print(sum_weight)