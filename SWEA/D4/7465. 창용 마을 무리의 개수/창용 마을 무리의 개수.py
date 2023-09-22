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

T = int(input())

for test_case in range(1, T + 1):
    # 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르자
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        f, t = map(int, input().split())
        edge.append([f, t])

    # 사이클 발생 여부를 union find 로 해결
    parents = [i for i in range(V+1)]

    # 현재 방문한 정점 수
    cnt = 0
    res = 0
    for f, t in edge:
        union(f, t)

    for j in range(1, V + 1):
        if parents[j] == j:
            res += 1

    print(f'#{test_case}', res)