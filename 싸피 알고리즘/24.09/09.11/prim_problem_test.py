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


# 프림 알고리즘 함수 정의
def prim(adj, V, start):
    # 사이클 여부 방문 체크 배열
    visited = [False] * V  # 정점의 방문 여부
    # 최소힙
    mn_heap = [(0, start)]  # 최소힙을 사용하여 간선 선택하도록

    # 최소 신장 비용 트리를 저장할 배열
    mst = []

    # 시작 정점으로부터 연결 되어 있는 간선 정보중에
    # 가장 최소 비용의 간선을 선택하여
    # 인접되어 있는 정점을 방문하고 위 과정을 반복하는 방법
    while mn_heap:
        weight, node = heappop(mn_heap)

        # 이미 방문된 정점이라면 패스! (사이클x)
        if visited[node]:
            continue

        visited[node] = True  # 방문 표시
        mst.append(weight)  # 비용 값만 mst 배열에 추가

        # 해당 정점으로 부터 연결되어 있는 간ㄴ선 정보를 최소 힙에 추가!
        for nxt_node, nxt_weight in adj[node]:
            if not visited[nxt_node]:
                # 연결된 정점을 최소 힙에 추가
                heappush(mn_heap, (nxt_weight, nxt_node))

    return mst


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
MST = prim(adj, V, start_node)

print(MST)
print("총합 ", sum(MST))
