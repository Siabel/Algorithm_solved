from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]

deq = deque([(0, 0)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

while deq:
    x, y = deq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                deq.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])