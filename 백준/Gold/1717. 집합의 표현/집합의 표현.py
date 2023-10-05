import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]

for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
    