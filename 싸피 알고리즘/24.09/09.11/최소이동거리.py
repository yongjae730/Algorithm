from heapq import heappop, heappush

def dijkstra(adj, V, start):
    # 노드 방문 여부를 기록하는 리스트
    visited = [False] * (V+1)
    # 최소 힙을 사용하여 (비용, 노드) 튜플을 저장
    mn_heap = [(0, start)]
    # 각 노드까지의 거리를 무한대로 초기화
    dist = [float('inf')] * (V+1)
    # 시작 노드까지의 거리는 0
    dist[start] = 0

    while mn_heap:
        # 현재까지의 거리와 노드를 힙에서 꺼냄
        cost, node = heappop(mn_heap)

        # 이미 방문한 노드인 경우 무시
        if visited[node]:
            continue

        # 현재 노드를 방문 처리
        visited[node] = True
        # 현재 노드와 연결된 모든 노드에 대해
        for nxt_node, nxt_cost in adj[node]:
            if not visited[nxt_node]:
                # 더 짧은 경로가 발견된 경우 거리 업데이트 및 힙에 추가
                if dist[nxt_node] > cost + nxt_cost:
                    dist[nxt_node] = cost + nxt_cost
                    heappush(mn_heap, (dist[nxt_node], nxt_node))
    return dist

T = int(input())
for tc in range(1, T + 1):
    # 노드와 엣지의 개수 입력
    V, E = map(int, input().split())
    # 인접 리스트를 초기화
    adj = [[] for _ in range(V + 1)]

    # 엣지 정보를 입력받아 인접 리스트에 추가
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    # 시작 노드 설정 (문제에 따라 변경 가능)
    start_node = 0
    # 다익스트라 알고리즘 실행
    dist = dijkstra(adj, V, start_node)

    # 결과 출력
    print(f'#{tc} {dist[-1]}')
