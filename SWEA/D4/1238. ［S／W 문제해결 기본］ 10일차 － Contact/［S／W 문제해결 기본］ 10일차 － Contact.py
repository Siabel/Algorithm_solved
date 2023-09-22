def contact(s):
    queue = [s]
    visited = [0] * 101
    visited[s] = 1

    max_number = s
    max_depth = 1

    while queue:
        now = queue.pop(0)

        # 갈 수 있는 지점 다 보기
        for to in graph[now]:
            if visited[to]:
                continue

            # 기존 방문보다 한번 더 감
            visited[to] = visited[now] + 1

            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to

            queue.append(to)
    return max_number

T = 10

for test_case in range(1, T + 1):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        f = arr[i]
        t = arr[i + 1]
        graph[f].append(t)
    result = contact(start)
    print(f'#{test_case}', result)