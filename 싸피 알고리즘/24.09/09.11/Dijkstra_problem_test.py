'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
from heapq import heappop, heappush


# 다익스트라 알고리즘 함수 정의
def dijkstra(adj, V, start):
    # 사이클 여부 방문 체크 배열
    visited = [False] * V  # 정점의 방문 여부
    # 최소힙
    mn_heap = [(0, start)]  # s -> x 최소 경로 비용, 방문하게 될 x정점)

    # 시작 정점으로 부터 모든 정점에 대해 최단 경로 비용을 계산한 배열
    dist = [float('inf')] * V
    dist[start] = 0  # 시작 -> 시작 : 비용 0

    # 현재까지 비용이 가장 작은 경로 정점x 를 뽑으면서 다음 최소 비용을 갱신
    # 인접되어 있는 정점을 방문하고 위 과정을 반복하는 방법
    while mn_heap:
        cost, node = heappop(mn_heap)

        # 이미 방문된 정점이라면 패스! (사이클x)
        if visited[node]:
            continue

        visited[node] = True  # 방문 표시
        # 해당 정점으로 부터 연결되어 있는 간선 정보를 최소 힙에 추가!
        for nxt_node, nxt_cost in adj[node]:
            if not visited[nxt_node]:
                # 최소 비용 거리를 갱신
                # s -> node : 최소비용 cost
                # node -> nxt_node : 비용 nxt_cost
                # s -> nxt_node : 임시 최소 비용 cost + nxt)_cost
                if dist[nxt_node] > cost + nxt_cost:
                    dist[nxt_node] = cost + nxt_cost
                    heappush(mn_heap, (dist[nxt_node], nxt_node))
    return dist


# 정점 수 V, 간선 수 E
V, E = map(int, input().split())

# 인접 리스트 초기화
adj = [[] for _ in range(V)]

# 간선의 정보를 입력 받기

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))  # u -> v : w
    # adj[v].append((u, w))  # v -> u : w

start_node = 0
# s 시작 정점에서 갈 수 있는 모든 노드에 대해 최소 경로 비용 : dist
dist = dijkstra(adj, V, start_node)

print(dist)
