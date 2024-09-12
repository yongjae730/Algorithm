'''
7 11
4 6 51
5 0 60
2 4 46
2 6 25
3 5 18
0 6 51
1 2 21
0 2 31
3 4 34
4 5 40
0 1 32
'''
from heapq import heappop, heappush


# 벨만포드 알고리즘 함수 정의
# 모든 간선에 대해 모든 정점의 수 만큼 반복 최소 경로 비용 갱신 처리
def bellman_ford(adj, V, start):
    # 간선 배열[(시작점, 끝점, 가중치)]
    edges = []
    for u in range(V):  # 시작점 v
        for v, w in adj[u]:  # 끝점 u
            edges.append((u, v, w))
    # 최소 비용을 저장한 dist 배열

    dist = [float('inf')] * V
    dist[start] = 0  # 시작 정점의 최소 비용은 0
    # 정점의 갯수만큼 반복
    for _ in range(V - 1):
        # 모든 간선에 대해
        for u, v, w in edges:
            # 시작 정점 -> u -> v 까지의 거리가 최소가 되도록 갱신
            # s -> v 까지의 거리보다 시작정점 -> u -> v 가 작다면 갱신
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    # 음수 사이클이 존재하는 경우(유무파악)
    # 한번 더 해당 최소 경로비용을 갱신 시도! -> 갱신되었다 -> 음의 사이클이 존재한다!
    for u, v, w in edges:
        # 시작 정점 -> u -> v 까지의 거리가 최소가 되도록 갱신
        # 음의 사이클이 존재한다!
        if dist[v] > dist[u] + w:
            return -1  # 음의 사이클이 존재하므로 -1 반환

    return dist


# 정점 수 V, 간선 수 E
V, E = map(int, input().split())

# 인접 리스트 초기화
adj = [[] for _ in range(V)]

# 간선의 정보를 입력 받기

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))  # u -> v : w
    adj[v].append((u, w))  # v -> u : w

start_node = 0
# s 시작 정점에서 갈 수 있는 모든 노드에 대해 최소 경로 비용 : dist
dist = bellman_ford(adj, V, start_node)

print(dist)
