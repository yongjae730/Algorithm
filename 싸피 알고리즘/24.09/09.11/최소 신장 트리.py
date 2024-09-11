from heapq import heappush, heappop

def prim(V, start):
    # 노드 방문 여부를 기록하는 리스트
    visited = [False] * (V+1)

    # 최소 힙을 사용하여 (비용, 노드) 튜플을 저장
    mn_heap = [(0, start)]

    # 최소 신장 트리의 가중치를 저장할 리스트
    mst = []
    while mn_heap:
        # 현재까지의 비용과 노드를 힙에서 꺼냄
        cost, node = heappop(mn_heap)

        # 이미 방문한 노드인 경우 무시
        if visited[node]:
            continue

        # 현재 노드를 방문 처리하고, MST에 추가
        visited[node] = True
        mst.append(cost)

        # 현재 노드와 연결된 모든 노드에 대해
        for nxt_node, nxt_cost in adj[node]:
            if not visited[nxt_node]:
                # 다음 노드와의 엣지를 힙에 추가
                heappush(mn_heap, (nxt_cost, nxt_node))

    return mst

T = int(input())

for tc in range(1, T + 1):
    # 노드와 엣지의 개수 입력
    V, E = map(int, input().split())
    # 인접 리스트를 초기화
    adj = [[] for _ in range(V+1)]

    # 엣지 정보를 입력받아 인접 리스트에 추가
    for _ in range(E):
        v, u, w = map(int, input().split())
        adj[v].append((u, w))
        adj[u].append((v, w))

    # 시작 노드 설정
    start = 0
    # Prim 알고리즘 실행
    result = prim(V, start)

    # MST의 총 가중치 출력
    print(f'#{tc} {sum(result)}')
