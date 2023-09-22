import heapq

def dijkstra(insu, graph):
    pq = []
    # 출발점 인수네 집 좌표로 초기화
    heapq.heappush(pq, (0, insu))
    
    # 최대값을 비교하기 위해서 가장 작은 수로 설정
    dist = [-1] * (n + 1)

    while pq:
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        time, node = heapq.heappop(pq)

        if dist[node] == -1:
            dist[node] = time
            for v, w in graph[node]:
                cur_time = time + w
                heapq.heappush(pq, (cur_time, v))

    return dist


T = int(input())

for test_case in range(1, T + 1):
    # n은 집 개수, m은 간선 개수, x는 인수의 집
    n, m, x = map(int, input().split())

    # 인접리스트 2개
    # 인수네 집 기준으로 노드까지 갈때와 노드 기준으로 인수네집으로 올때를 각각 구하고 더하기 위해서
    graph1 = [[] for _ in range(n + 1)]
    graph2 = [[] for _ in range(n + 1)]

    for _ in range(m):
        # f 번 집에서 t 번 집으로 갈때 걸리는 time
        f, t, time = map(int, input().split())
        
        # 왕복으로 왔다갔다 하는 시간을 비교하기 위해 그래프 2개를 반대방향으로 만듬
        graph1[f].append((t, time))
        graph2[t].append((f, time))

    # 각 거리를 갈때, 올때 기준으로 나눠서 함수를 호출
    dist1 = dijkstra(x, graph1)
    dist2 = dijkstra(x, graph2)
    # 결과값을 저장할 result
    result = 0
    
    # 각 index 별로 갈때와 올때 값이 저장되어 있으므로 같은 index 값을 더해줌
    # 다 더해준 것과 마지막으로 저장된 result 까지 비교해서 가장 큰 값을 찾기
    for i in range(1, n + 1):
        result = max(result, dist1[i] + dist2[i])

    print(f'#{test_case}', result)
