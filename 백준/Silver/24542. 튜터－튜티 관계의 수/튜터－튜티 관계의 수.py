import sys

input = sys.stdin.readline

def bfs(v):
    visited[v] = 1
    res.append(0)
    queue = []
    queue.append(v)

    while queue:
        p = queue.pop(0)
        for num in graph[p]:
            if visited[num] == 0:
                queue.append(num)
                visited[num] = 1
                res.append(0)
    

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1
visited = [0] * (n + 1)
res = []
for i in range(1, n + 1):
    bfs(i)
    cnt *= len(res)
    res = []

print(cnt % 1000000007)