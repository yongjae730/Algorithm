from heapq import heappop, heappush


def prim(adj, N, start):
    visited = [False] * (N + 1)
    mn_heap = [(0, start)]
    mst = []

    while mn_heap:
        cost, node = heappop(mn_heap)

        if visited[node]:
            continue
        visited[node] = True
        mst.append(cost)

        for nxt_node, nxt_cost in adj[node]:
            if not visited[nxt_node]:
                heappush(mn_heap, (nxt_cost, nxt_node))
    return mst


N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

start_node = 1
MST = prim(adj, N, start_node)
print(sum(MST))
